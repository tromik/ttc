import requests, time

r = requests.get('https://myttc.ca/finch_station.json')

data = r.json()

stops = data["stops"]

name_elements = [element['name'] for element in data['stops']]


for stop in data['stops']:
    for route in stop['routes']:
        print ''
        print ''
        print ''
        route_name = route['name']
        print route_name
        print '-'*25
        for stop_time in route['stop_times']:
            stop_time_shape = stop_time['shape']
            stop_time_departure_time = stop_time['departure_time']
            stop_time_departure_timestamp = stop_time['departure_timestamp']
            # stop_time_departure_datetime = time.strftime("%D %H:%M", time.localtime(int(stop_time_departure_timestamp)))
            print stop_time_shape + ' | ' + stop_time_departure_time # + ' | ' + stop_time_departure_datetime
