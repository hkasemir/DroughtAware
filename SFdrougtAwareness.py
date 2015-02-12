from math import sqrt

GALLONS_PER_CUBIC_YARD = 201.974026
SQ_FT_PER_SQ_MILE = 27878400
SQ_YARDS_PER_SQ_MILE = 3097600
INCHES_PER_YARD = 36
# Inches of rain that fell in SF in 2014 per ggweather.com
SF_RAINFALL_2014 = 25.45 
# Square miles of city and county of SF
SF_AREA = 231.89
SF_POPULATION = 837442
# Average gallons in a full bath tub found here:
# http://water.usgs.gov/edu/qa-home-percapita.html
AVERAGE_BATH_GALLONS = 36 
# Gallons per minute of an average shower head
SHOWERHEAD_GPM = 2.5 


def rain_gallons(rainfall, area):
    # calculates total gallons of rain that fell in a region based on the area
    # in sq. miles and rainfall in inches. Uses yards as an intermediate
    # measure.
    area_sq_yds = area * SQ_YARDS_PER_SQ_MILE
    rain_yds = rainfall / INCHES_PER_YARD
    rainfall_cy = rain_yds * area_sq_yds
    rainfall_gal = rainfall_cy * GALLONS_PER_CUBIC_YARD
    return rainfall_gal

def user_bath_frequency():
    input_frequency = input("How many baths do you take in a typical week?: ")
    try:
        float_frequency = float(input_frequency)
    except ValueError as e:
        float_frequency = False
    return float_frequency

def float_check_bath_frequency():
    bath_frequency = user_bath_frequency()
    while bath_frequency == False:
        print ("Sorry, that's not a number, please type in a digit " \
               "(like 5, for example): ")
        bath_frequency = user_bath_frequency()
    return bath_frequency

def user_shower_length():
    input_length = input("How long (in minutes) do you typically shower?: ")
    try:
        float_length = float(input_length)
    except ValueError as e:
        float_length = False
    return float_length

def float_check_shower_length():
    length = user_shower_length()
    while length == False:
        print ("Sorry, that's not a number, please type in a digit " \
               "(like 5, for example): ")
        length = user_shower_length()
    return length

def user_shower_frequency():
    input_frequency = input("How many times per week do you shower," \
                            "on average?: ")
    try:
        float_frequency = float(input_frequency)
    except ValueError as e:
        float_frequency = False
    return float_frequency

def float_check_shower_frequency():
    shower_frequency = user_shower_frequency()
    while shower_frequency == False:
        print ("Sorry, that's not a number, please type in a digit " \
               "(like 5, for example): ")
        shower_frequency = user_shower_frequency()
    return shower_frequency

def annual_shower_gallons(length, frequency, gpm):
    # calculates the number of gallons the user uses to shower every year
    gal_per_shower = length * gpm
    print ("Did you know you use about " + str(gal_per_shower) + \
           " gallons of water every time you shower?")
    annual_gallons = gal_per_shower * 52.0 * frequency
    return annual_gallons

def user_bath_gallons(frequency, bath_gallons):
    annual_bath_gallons = frequency * bath_gallons * 52
    print ("Did you know you probably use about " + str(bath_gallons) + \
           " gallons of water every time you take a bath? This adds up to " + \
           str(annual_bath_gallons) + " gallons per year!")
    return annual_bath_gallons

def user_collection_area(gallons, rainfall):
    # Calculates the area of a hypothetical rain collector that the user would
    # need to have to harvest enough water every year from rain just to shower.
    # Again, uses cubic yards (cy) as an intermediate measure
    shower_cy = gallons / GALLONS_PER_CUBIC_YARD
    rain_yds = rainfall / INCHES_PER_YARD
    # connection_area comes out in square feet
    collection_area = round(shower_cy / rain_yds * 9, 2) 
    collector_side_length = round(sqrt(collection_area), 2)
    print ("If you were to collect all the water you needed to bathe and/or" \
           " shower for 2014 from the rain in San Francisco, you would need" \
           " to build a " + str(collection_area) +" square foot collector. " \
           "This is equivalent to a square with a " + \
           str(collector_side_length) + " foot side length.")
    return collection_area


def city_collection_area(collector_area, population):
    # Provides the size of rain collector needed to shower all the people in \
    # that region
    # city_ca is the collector area in square miles
    city_ca = round(collector_area / SQ_FT_PER_SQ_MILE * population, 2) 
    city_collection_side_length = round(sqrt(city_ca), 2)
    print("If everyone in San Francisco were to use the same amount of water" \
          " as you, the city would need a " + str(city_ca) + " sqaure mile" \
          " colloector. This means a square collector with a " + \
          str(city_collection_side_length) + " mile side length!")
   
def bath_or_shower():
    # Asks if the user typically bathes or showers
    habit = input("Do you typically bathe, shower, or both?: ").lower()
    return habit


SF_rain_gallons = rain_gallons(SF_RAINFALL_2014, SF_AREA)

user_habit = bath_or_shower()

while user_habit not in ["bathe", "shower", "both"]:
    print ("Sorry, you're answer wasn't 'bathe', 'shower', or 'both'. " \
           "Please try again: ")
    user_habit = bath_or_shower()

if user_habit == "bathe":
    bath_frequency = float_check_bath_frequency()
    user_gallons = user_bath_gallons(bath_frequency, AVERAGE_BATH_GALLONS)
    user_collector = user_collection_area(user_gallons, SF_RAINFALL_2014)
    SF_city_collector = city_collection_area(user_collector, SF_POPULATION)
        
elif user_habit == "shower":
    shower_length = float_check_shower_length()
    shower_frequency = float_check_shower_frequency()     
    user_gallons = annual_shower_gallons(shower_length, shower_frequency,
                                         SHOWERHEAD_GPM)
    user_collector = user_collection_area(user_gallons, SF_RAINFALL_2014)
    SF_city_collector = city_collection_area(user_collector, SF_POPULATION)
        
elif user_habit == "both":
    shower_length = float_check_shower_length()
    shower_frequency = float_check_shower_frequency()
    shower_gal = annual_shower_gallons(shower_length, shower_frequency,
                                       SHOWERHEAD_GPM)
    bath_frequency = float_check_bath_frequency()
    bath_gal = user_bath_gallons(bath_frequency, AVERAGE_BATH_GALLONS)
    user_gallons = shower_gal + bath_gal
    user_collector = user_collection_area(user_gallons, SF_RAINFALL_2014)
    SF_city_collector = city_collection_area(user_collector, SF_POPULATION)