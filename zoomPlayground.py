import requests
import zoomCreds
import json
BASE_URL = "https://api.zoom.us/v2/"

authHeader = {'authorization': 'Bearer {jwt}'.format(jwt=zoomCreds.JWT)}

r = requests.get(BASE_URL+"users", headers=authHeader)
print(json.dumps(r, indent=2))