import requests, json

x = requests.get('https://discover.data.vic.gov.au/api/3/action/datastore_search?resource_id=afb52611-6061-4a2b-9110-74c920bede77')
y = json.loads(x.content)

sites = y['result']['records']

for site in sites:
    address = f"{site['Site_streetaddress']}, {site['Suburb']}, {site['Site_state']} {site['Site_postcode']}"
    try:
        z = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key=AIzaSyBvvSGm6NlVs7kqn4AoizZW_z0vi7-p14Q')
        data = json.loads(z.content)

        location = data['results'][0]['geometry']['location']

        site['location'] = location
        print(f"{site['Site_title']} done")
    except:
        print("Error")

with open('exposuresites.json', 'w') as fp:
    json.dump(sites, fp)

# site = sites[0]

# address = f"{site['Site_streetaddress']}, {site['Suburb']}, {site['Site_state']} {site['Site_postcode']}"
# z = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key=AIzaSyBvvSGm6NlVs7kqn4AoizZW_z0vi7-p14Q')
# data = json.loads(z.content)

# location = data['results'][0]['geometry']['location']

# print(location)
