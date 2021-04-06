import requests
import json
import creds
API_KEY = creds.API_KEY
BASE_URL = 'https://www.eventbriteapi.com/v3/'

auth_header = {
    'Authorization' : 'Bearer {token}'.format(token=API_KEY)
}

MISSION_CAPITAL_ORG_ID = "286088072639"
CEO_Coaching_Cohort_1_Event_ID = "132583327301"
orderidtest = '1656541919'
exampleAttendeeID='2310392373'
#promotional_code

# Valid Paths: events/event_id/attendees, organizations/orgID/events,

r = requests.get(BASE_URL + 'attendees/2310392373'.format(orderidtest=orderidtest), headers=auth_header, params={"expand":"promotional_code"})

data = r.json()

print(json.dumps(data, indent=2))