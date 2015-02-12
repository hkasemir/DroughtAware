import math


#constants used, and conversion factors
gal_per_cy = 201.974026
sq_feet_per_sq_mile = 27878400
SF_annual_rainfall2014 = 25.45 #inches of rain that fell in SF in 2014 per ggweather.com
SF_area = 231.89 # square miles of city and county of SF
SF_population = 837442
average_bath_gallons = 36 #found here: http://water.usgs.gov/edu/qa-home-percapita.html
gpm = 2.5 #gallons per minute of an average shower head

def rain_gallons(rainfall, area):
    # calculates total gallons of rain that fell in a region based on the area in sq. miles and rainfall in inches. Uses yards as an intermediate measure.
    area_sq_yds = area * 3097600
    rain_yds = rainfall / 36
    rainfall_cy = rain_yds * area_sq_yds
    rainfall_gal = rainfall_cy * gal_per_cy
    return rainfall_gal

def u_bath_f():
    input_f = input("How many baths do you take in a typical week?")
    try:
        float_input_f = float(input_f)
    except ValueError as e:
        float_input_f = False
    return float_input_f

def float_check_bath_f():
    bath_frequency = u_bath_f()
    while bath_frequency == False:
        print ("Sorry, that's not a number, please type in a digit (like 5, for example):")
        bath_frequency = u_bath_f()
    return bath_frequency

def u_shower_length():
    input_length = input("How long (in minutes) do you typically shower?")
    try:
        float_length = float(input_length)
    except ValueError as e:
        float_length = False
    return float_length

def float_check_shower_length():
    length = u_shower_length()
    while length == False:
        print ("Sorry, that's not a number, please type in a digit (like 5, for example):")
        length = u_shower_length()
    return length

def u_shower_f():
    input_f = input("How many times per week do you shower, on average?")
    try:
        float_f = float(input_f)
    except ValueError as e:
        float_f = False
    return float_f  
    
def float_check_shower_f():
    shower_frequency = u_shower_f()
    while shower_frequency == False:
        print ("Sorry, that's not a number, please type in a digit (like 5, for example):")
        shower_frequency = u_shower_f()
    return shower_frequency

def annual_shower_gal(length, frequency, gpm):
    # calculates the number of gallons the user uses to shower every year
    gal_per_shower = length * gpm
    print ("Did you know you use about " + str(gal_per_shower) + " gallons of water every time you shower?")
    annual_gallons = gal_per_shower * 52.0 * frequency
    return annual_gallons

def u_bath_gal(bath, bath_gallons):
    annual_bath_gallons = bath * bath_gallons * 52
    print ("Did you know you use about " + str(bath_gallons) + " gallons of water every time you take a bath? This adds up to " + str(annual_bath_gallons) + " gallons per year!")
    return annual_bath_gallons

def u_collection_area(gallons, rainfall):
    #calculates the area of a hypothetical rain collector that the user would need to have to harvest enough water every year from rain just to shower. Again, uses cubic yards (cy) as an intermediate measure
    shower_cy = gallons / gal_per_cy
    rain_yds = rainfall / 36
    collection_area = round(shower_cy / rain_yds * 9, 2) #comes out in square feet
    collector_side_length = round(math.sqrt(collection_area), 2)
    print ("If you were to collect all the water you needed to bathe and/or shower for 2014 from the rain in San Francisco, you would need to build a " + str(collection_area) +" square foot collector. This is equivalent to a square with a " + str(collector_side_length) + " foot side length")
    return collection_area


def city_collection_area(collector_area, population):
    # provides the size of rain collector needed to shower all the people in that region
    city_ca = round(collector_area / sq_feet_per_sq_mile * population, 2) # collector area in square miles
    city_collection_side_length = round(math.sqrt(city_ca), 2)
    print("If everyone in San Francisco were to use the same amount of water as you, the city would need a " + str(city_ca) + " sqaure mile colloector. This means a square collector with a " + str(city_collection_side_length) + " mile side length!")
    
    
SF_rain_gallons = rain_gallons(SF_annual_rainfall2014, SF_area)
    
def bath_or_shower():
    # asks if the user bathes or showers more
    habit = input("Do you typically bathe, shower, or both?").lower()
    return habit

user_habit = bath_or_shower()

while user_habit != "bathe" and \
   user_habit != "shower" and \
   user_habit != "both":
    print ("Sorry, you're answer wasn't 'bathe', 'shower', or 'both'. Please try again:")
    user_habit = bath_or_shower()


if user_habit == "bathe":
    bath_f = float_check_bath_f()
    u_gallons = u_bath_gal(bath_f, average_bath_gallons)
    u_collector = u_collection_area(u_gallons, SF_annual_rainfall2014)
    SF_city_collector = city_collection_area(u_collector, SF_population)
        
elif user_habit == "shower":
    shower_length = float_check_shower_length()
    shower_f = float_check_shower_f()
        
    u_gallons = annual_shower_gal(shower_length, shower_f, gpm)
    u_collector = u_collection_area(u_gallons, SF_annual_rainfall2014)
    SF_city_collector = city_collection_area(u_collector, SF_population)
        
elif user_habit == "both":
    shower_length = float_check_shower_length()
    shower_f = float_check_shower_f()
        
    shower_gal = annual_shower_gal(shower_length, shower_f, gpm)
        
    bath_f = float_check_bath_f()
    bath_gal = u_bath_gal(bath_f, average_bath_gallons)
    
    u_gallons = shower_gal + bath_gal
    u_collector = u_collection_area(u_gallons, SF_annual_rainfall2014)
    SF_city_collector = city_collection_area(u_collector, SF_population)

else:
    print ("Sorry, couldn't use your input")
    