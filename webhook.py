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

def getSalesforce():
    sf = Salesforce(instance=SANDBOX_URL, username=USERNAME, password=PASSWORD, security_token=SANDBOX_SECURITY_TOKEN, domain=DOMAIN)
    return sf

def createEvent(api_url):
    sf = getSalesforce()
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



def processOrder(api_url):
    sf = getSalesforce()
    r = requests.get(api_url, headers=AUTH_HEADER_EB, params={"expand":"category","expand":"promotional_code","expand":"promo_code"})
    order = r.json()
    r = requests.get(api_url+"/attendees", headers=AUTH_HEADER_EB, params={"expand":"category","expand":"promotional_code","expand":"promo_code"})
    attendees = r.json()
    for attendee in attendees['attendees']:
        print("Checking for a match for "+attendee['profile']['name'])
        queryResult = sf.query("SELECT Id, Email, npsp__Primary_Affiliation__c, Primary_Affiliation_text__c FROM Contact WHERE Email = '{attendeeEmail}'".format(attendeeEmail=attendee['profile']['email']))
        if queryResult['totalSize'] == 0:
            print("Attendee not found in db by email search. Checking if organization name exists...")
            accountQueryResult = sf.query("SELECT Id, Name from Account WHERE Name = '{ebOrg}'".format(ebOrg=attendee['company']))
            if accountQueryResult['totalSize'] ==0:
                print("No matching company")
            if accountQueryResult['totalSize'] ==1:
                print("Account Found, searching by name...")
                personQueryResult = sf.query("SELECT Id, Name, Primary_Affiliation_text__c FROM Contact WHERE Name='{ebName}' AND Primary_Affiliation_text__c='{ebCompany}".format(ebName=attendee['name'], ebCompany=attendee['company']))
                print("Match found! Updating Contact Email...")
                sf.Contact.update(personQueryResult['records'][0]['Id'], {'Email':attendee['profile']['email']})
            print(json.dumps(accountQueryResult, indent=2))
            #queryResult = sf.query("SELECT Id, Email, npsp__Primary_Affiliation__c")
        if queryResult['totalSize'] == 1:
            print("Found 1 result")
            print("Checking if primary affiliation is an exact match....")
            if queryResult['records'][0]['Primary_Affiliation_text__c'] == "Hogwarts School of Wizardry": #attendee['profile']['company']:
                print("Matches Primary Affiliation! Updating records...")
                result = sf.Contact.update(queryResult['records'][0]['Id'], {'Email':attendee['profile']['email'], 'FirstName':attendee['profile']['first_name'], 'LastName':attendee['profile']['last_name']})
                print(result.json())







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
    # if (action == "order.created"):
    #     processOrder(requestJSON['api_url'])
    #     return Response(status=200)
    return Response(status=200)

@app.route('/', methods=['GET'])
def respondGet():
    return "App is running! Ready to recieve POST requests from Eventbrite."

if __name__ == '__main__':
   app.run()

# processOrder(BASE_URL+"orders/1656541919")