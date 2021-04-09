import creds
import requests
from flask import Flask, request, Response
import json
from simple_salesforce import Salesforce
# Eventbrite API Authentication Imports
API_KEY = creds.EB_API_KEY
BASE_URL = 'https://www.eventbriteapi.com/v3/'
AUTH_HEADER_EB = {
    'Authorization' : 'Bearer {token}'.format(token=API_KEY)
}
# Salesforce API Authentication Imports
SANDBOX_URL = creds.SF_SANDBOX_URL
PROD_URL = creds.SF_PROD_URL
USERNAME = creds.SF_USERNAME
PASSWORD = creds.SF_PASSWORD
PROD_PASSWORD = creds.SF_PROD_PASSWORD
SANDBOX_SECURITY_TOKEN = creds.SF_SANDBOX_SECURITY_TOKEN
PROD_SECURITY_TOKEN = creds.SF_PROD_SECURITY_TOKEN
DOMAIN = "test"

# Create Flask App Instance. 
app = Flask(__name__)


API_KEY = creds.EB_API_KEY
BASE_URL = 'https://www.eventbriteapi.com/v3/'
AUTH_HEADER_EB = {
    'Authorization' : 'Bearer {token}'.format(token=API_KEY)
}


def createEvent(api_url):
    sf = Salesforce(instance=SANDBOX_URL, username=USERNAME, password=PASSWORD, security_token=SANDBOX_SECURITY_TOKEN, domain=DOMAIN)
    event = requests.get(api_url, headers=AUTH_HEADER_EB, params={"expand":"category","expand":"promotional_code","expand":"promo_code"})
    eventData = event.json()
    sf_respond = sf.Campaign.create(
        {'Name':eventData['name']['text'], 
        'Event_URL__c':eventData['url'], 
        'StartDate':eventData['start']['local'], 
        'EndDate':eventData['end']['local'], 
        'Type':'Training Workshop, Small (default)', 
        'Status':'Open', 'IsActive':True, 
        'Description':eventData['description']['text'], 
        'EventbriteSync__EventbriteId__c':eventData['id'], 
        'RecordTypeId':'012f4000000JcuJAAS'})
    print(sf_respond)


## Main function that is invoked when the webhook is invoked. 
## Eventbrite API sends a POST request to the webhook. POST data is stored in request, convert it to JSON. The keys of the dict are 'api_url' which contains the URL with the data. 
## and config, which is a dictionary that contains the action (i.e order.created), user_id, endpoint_url (webhook address), and 'webhook_id'
@app.route('/', methods=['POST'])
def respond():
    requestJSON = request.json #Convert request object to dictionary
    action = requestJSON['config']['action']
    if (action == "event.published"):
        createEvent(requestJSON['api_url'])
        return Response(status=200)
    return Response(status=200)


if __name__ == '__main__':
   app.run()
