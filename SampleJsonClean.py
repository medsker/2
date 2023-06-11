import json
##Load Sample json
#f = open('sample.json')
#data = json.load(f)
with open('sample.json') as f:
    data = json.load(f)
f.close()


def who_is_driver():
    '''This function asks for a name of a driver.'''
    driver_name = ''
    while driver_name not in ['Jim', 'Joe']:
        driver_name = input("What is the driver's name?")
    return driver_name

def where_is_driver(name):
    '''This function checks for the location of a driver.'''
    driver_location = driver_location = {
    'Jim': {'lon': -75.14667, 'lat': 40.008667},
    'Joe': {'lon': -74.14667, 'lat': 40.009668}
    }
    if name in driver_location:
        location = driver_location[name]
        return name, location['lon'], location['lat']

def where_is_delivery(driver_name, driver_lon, driver_lat):
    '''This function takes output from the where_is_driver function to find
    deliveries near the driver. If it finds a delivery, it returns a delivery
    manifest for the driver.'''
    for x in data:
        if x['position']['lon'] == driver_lon and x['position']['lat'] == driver_lat:
            print ("Driver " + driver_name + " is Nearby " + x['id'])
            delivery_id = x['id']
            delivery_position =  x['position']
            desired_delivery = x['desired_delivery']
            driver_manifest = [
                {
                    'driver':driver_name,
                    'id':delivery_id,
                    'position':delivery_position, 
                    'desired_delivery':desired_delivery
                }
            ]
            print ('Assign ' + driver_name + " the following manifest. \n")
            return driver_manifest
        else:
            #print ("Driver " + driver_name + " is Far Away")
            continue
            
# Specify the name of the driver, this will respond back
# with a location, if found.
d = who_is_driver()
#Check for the location of a driver specified above & set variables for name and location
#the name and location is used as parameters in the where_is_delivery function
driver_name,driver_lon,driver_lat = where_is_driver(d)
#This allows me to print float data types as strings
#res = float(driver_lat), float(driver_lon)
print (f"Driver {driver_name} is located at the following coordinates:\n{driver_lon}, {driver_lat}")
print ("\nChecking to see if there is a delivery near {driver_name}... \n") 
# Look for locations of deliveries that are close to driver
# assign the driver a delivery if nearby 
where_is_delivery_result = where_is_delivery(driver_name,driver_lon,driver_lat)
print (where_is_delivery_result)