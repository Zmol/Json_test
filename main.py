from urllib.request import urlopen
import json
import locale
#from dmi_open_data import DMIOpenDataClient, Parameter, ClimateDataParameter

with urlopen("https://dmigw.govcloud.dk/v2/oceanObs/collections/observation/items?api-key=9fa0f284-8e62-43ba-afad-031b3e6b532e&stationId=22331&period=latest-week") as response:
    source = response.read()


data_json = json.loads(source)
#print(json.dumps(data_json, indent=2))


#print(type(data_json["features"]))
#for feature in data_json['features']:
#    print(feature['properties'])

data = []

for feature in data_json['features']:
    tmp = {}
    tmp[feature["properties"]["observed"]] = feature["properties"]["value"]
    data.append(tmp)


print(data)
