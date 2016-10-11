import requests

# http://www.giantbomb.com/api/game/3030-4725/?api_key=0bcdc2b6d79c75d47c698db492d71d613f8e1458&format=json&field_list=genres,name

# api_key = 'test_712fa0882781b9202ab506d0c1e889cd36176d1d'
r = requests.get('https://myttc.ca/finch_station.json')

data = r.json()
# text_data = str(r.json())
# print data
# print ""
# print "-"*10
# print ""
# print data['stops']

stops = data["stops"]

# print stops

# print data.keys()

# for key in stops:
#    print repr(key)

# print stops


name_elements = [element['name'] for element in data['stops']]
# route_name_elements = [element['name'] for element in data['stops']['routes']]

for stop in data['stops']:
    for route in stop['routes']:
        print route['name']
        print '------------'
        for stop_time in route['stop_times']:
            print stop_time['shape'] + ' ' + stop_time['departure_time']
print name_elements
# print route_name_elements
