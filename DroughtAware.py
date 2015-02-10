import math


#constants used, and conversion factors
gal_per_cy = 201.974026

SF_annual_rainfall2014 = 25.45 #inches of rain that fell in SF in 2014 per ggweather.com
SF_area = 231.89 # square miles of city and county of SF

def rain_gallons(rainfall, area):
    # calculates total gallons of rain that fell in a region based on the area in sq. miles and rainfall in inches. Uses yards as an intermediate measure.
    area_sq_yds = area * 3097600
    rain_yds = rainfall / 36
    rainfall_cy = rain_yds * area_sq_yds
    rainfall_gal = rainfall_cy * gal_per_cy
    return rainfall_gal



u_shower_length = float(input("How long (in minutes) do you typically shower?"))
u_shower_f = float(input("How many times per week do you shower, on average?"))
gpm = 2.1 #gallons per minute of an average shower head


def annual_shower_gal(length, frequency, gpm):
    # calculates the number of gallons the user uses to shower every year
    gal_per_shower = length * gpm
    print ("Did you know you use about " + str(gal_per_shower) + " gallons of water every time you shower?")
    annual_gallons = gal_per_shower * 52.0 * frequency
    return annual_gallons


# calculates the number of gallons the user uses to shower every year

def u_collection_area(shower_gallons, rainfall):
    #calculates the area of a hypothetical rain collector that the user would need to have to harvest enough water every year from rain just to shower. Again, uses cubic yards (cy) as an intermediate measure
    shower_cy = shower_gallons / gal_per_cy
    rain_yds = rainfall / 36
    collection_area = shower_cy / rain_yds * 9 #comes out in square feet
    collector_side_length = math.sqrt(collection_area)
    print ("If you were to collect all the water you needed to shower for 2014 from the rain in San Francisco, you would need to build a %s square foot collector. This is equivalent to a square with a %s foot side length" %s (collection_area, collector_side_length))
    return collection_area


#def city_collection_area(collector_area, rainfall, population):
    # provides the size of rain collector needed to shower all the people in that
    

SF_rain_gallons = rain_gallons(SF_annual_rainfall2014, SF_area)
annual_shower_gal(u_shower_length, u_shower_f, gpm)
u_collection_area(annual_shower_gal, SF_annual_rainfall2014)
