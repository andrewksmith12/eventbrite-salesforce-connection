import requests
import creds
import json
from simple_salesforce import Salesforce
SANDBOX_URL = creds.SF_SANDBOX_URL
PROD_URL = creds.SF_PROD_URL
USERNAME = creds.SF_USERNAME
PASSWORD = creds.SF_PASSWORD
PROD_PASSWORD = creds.SF_PROD_PASSWORD
SANDBOX_SECURITY_TOKEN = creds.SF_SANDBOX_SECURITY_TOKEN
PROD_SECURITY_TOKEN = creds.SF_PROD_SECURITY_TOKEN
DOMAIN = "test"

# Sandbox sf Object
sf = Salesforce(instance=SANDBOX_URL, username=USERNAME, password=PASSWORD, security_token=SANDBOX_SECURITY_TOKEN, domain=DOMAIN)
# Prod sf object
#sf = Salesforce(instance=PROD_URL, username=USERNAME, password=PROD_PASSWORD, security_token=PROD_SECURITY_TOKEN, domain=DOMAIN)

# event = requests.get('https://www.eventbriteapi.com/v3/events/141374389605', headers=webhook.AUTH_HEADER_EB, params={"expand":"category","expand":"promotional_code","expand":"promo_code"})
# eventData = event.json()
# sf_respond = sf.Campaign.create({'Name':eventData['name']['text'],'Event_URL__c':eventData['url'], 'StartDate':eventData['start']['local'], 'EndDate':eventData['end']['local'], 'Type':'Training Workshop, Small (default)', 'Status':'Open', 'IsActive':True, 'Description':eventData['description']['text'], 'EventbriteSync__EventbriteId__c':eventData['id'], 'RecordTypeId':'012f4000000JcuJAAS'})
# print(sf_respond)

# accountQueryResult = sf.query("SELECT Id, Name from Account WHERE Name = '{ebOrg}'".format(ebOrg='Hogwarts School of Wizardry'))
# print(json.dumps(accountQueryResult, indent=2))
# print(accountQueryResult['records'][0]['Id'])

# sfCampaign = sf.query("SELECT Id FROM Campaign WHERE EventbriteSync__EventbriteId__c = '{ebEventID}'".format(ebEventID='141374389605'))
# print(json.dumps(sfCampaign, indent=2))
# print(sfCampaign['records'][0]["Id"])

# sfResult = sf.CampaignMember.create({'CampaignId':sfCampaign['records'][0]["Id"], 'ContactId':'0038A00000YfgVEQAZ'})
# print(sfResult['id'])


createAccountResult = sf.Account.create({'Name':'Andrew Corp2'})
print(createAccountResult)
print(createAccountResult['id'])

#things_to_do = dir(sf)

# data = sf.query("SELECT ")

# data = sf.query("SELECT Name, Email, Primary_Affiliation_text__c FROM Contact WHERE Email = 'headmaster@hogwarts.edu'")

# sf.Contact.create({'LastName':'Smith','Email':'example@example.com'})

# sf.Contact.create({'LastName':'Smith','Email':'example@example.com'})

# contact = sf.Contact.get('0038A00000YfgVEQAZ')

# contact = sf.Contact.get_by_custom_id('My_Custom_ID__c', '22')

# sfresult = sf.Contact.update('0038A00000YfgVEQAZ',{'LastName': 'Jones', 'FirstName': 'John'})
# sfresult = 204 (succeded, no content) 
# sf.Contact.delete('0038A00000YfgVEQAZ')