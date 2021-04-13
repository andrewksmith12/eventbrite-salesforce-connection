import requests
import json
import creds
import subprocess
API_KEY = creds.EB_API_KEY
BASE_URL = 'https://www.eventbriteapi.com/v3/'

auth_header = {
    'Authorization' : 'Bearer {token}'.format(token=API_KEY)
}

MISSION_CAPITAL_ORG_ID = "286088072639"
CEO_Coaching_Cohort_1_Event_ID = "132583327301"
orderidtest = '1656541919'
exampleComplexOrder = '1659644669'
exampleAttendeeID='2310392373'
#promotional_code

# Valid Paths: events/event_id/attendees, organizations/orgID/events,

r = requests.get(BASE_URL + 'orders/1677388583/attendees'.format(orgID=MISSION_CAPITAL_ORG_ID), headers=auth_header, params={"expand":"category","expand":"promotional_code"})
r = r.json()
aks = json.dumps(r, indent=2)
print(aks)
subprocess.run("pbcopy", universal_newlines=True, input=aks)


#print(json.dumps(data, indent=2)