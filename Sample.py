import json

def load_json(file_path):
    '''Load JSON data from a file.'''
    with open(file_path) as f:
        return json.load(f)

def who_is_driver():
    '''Ask for the name of a driver.'''
    driver_name = input("What is the driver's name? ")
    if driver_name in ['Jim', 'Joe']:
        return driver_name
    return None

def where_is_driver(name, location_data):
    '''Check the location of a driver.'''
    if name in location_data:
        location = location_data[name]
        return name, location['lon'], location['lat']
    return None

def where_is_delivery(driver_name, driver_lon, driver_lat, delivery_data):
    '''Find deliveries near the driver and return a delivery manifest.'''
    for delivery in delivery_data:
        if delivery['position']['lon'] == driver_lon and delivery['position']['lat'] == driver_lat:
            print(f"Driver {driver_name} is nearby {delivery['id']}")
            driver_manifest = {
                'driver': driver_name,
                'id': delivery['id'],
                'position': delivery['position'],
                'desired_delivery': delivery['desired_delivery']
            }
            print(f"Assign {driver_name} the following manifest:\n{driver_manifest}")
            return [driver_manifest]
    print(f"No nearby deliveries found for {driver_name}.")
    return []

# Load sample JSON data
data = load_json('sample.json')

# Driver location data
driver_location = {
    'Jim': {'lon': -75.14667, 'lat': 40.008667},
    'Joe': {'lon': -74.14667, 'lat': 40.009668}
}

# Specify the name of the driver
driver_name = who_is_driver()

# Check if a valid driver name was entered
if driver_name is not None:
    # Check the location of the driver
    driver_location_info = where_is_driver(driver_name, driver_location)
    if driver_location_info is not None:
        driver_name, driver_lon, driver_lat = driver_location_info
        print(f"Driver {driver_name} is located at the following coordinates:\n{driver_lon}, {driver_lat}")
        print(f"\nChecking to see if there is a delivery near {driver_name}...\n")
        # Look for deliveries near the driver
        driver_manifest = where_is_delivery(driver_name, driver_lon, driver_lat, data)
        #print(driver_manifest)
    else:
        print(f"Location not found for driver {driver_name}.")
else:
    print("Invalid driver name entered.")
