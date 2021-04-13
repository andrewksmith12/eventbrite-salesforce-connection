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

attendee = {}
api_output = {'pagination': {'object_count': 1, 'page_number': 1, 'page_size': 50, 'page_count': 1, 'has_more_items': False}, 'attendees': [{'costs': {'base_price': {'display': '$209.90', 'currency': 'USD', 'value': 20990, 'major_value': '209.90'}, 'eventbrite_fee': {'display': '$9.47', 'currency': 'USD', 'value': 947, 'major_value': '9.47'}, 'gross': {'display': '$225.00', 'currency': 'USD', 'value': 22500, 'major_value': '225.00'}, 'payment_fee': {'display': '$5.63', 'currency': 'USD', 'value': 563, 'major_value': '5.63'}, 'tax': {'display': '$0.00', 'currency': 'USD', 'value': 0, 'major_value': '0.00'}}, 'resource_uri': 'https://www.eventbriteapi.com/v3/orders/1659644669/attendees/2314922795/', 'id': '2314922795', 'changed': '2021-03-23T15:37:27Z', 'created': '2021-03-23T15:37:27Z', 'quantity': 1, 'variant_id': None, 'profile': {'first_name': 'Raney', 'last_name': 'McKool', 'addresses': {'bill': {'postal_code': '78704'}}, 'company': 'Todos Juntos Learning Center', 'name': 'Raney McKool', 'email': 'raney@todosjuntoslc.org', 'job_title': 'Operations Director'}, 'barcodes': [{'status': 'unused', 'barcode': '16596446692314922795001', 'created': '2021-03-23T15:37:30Z', 'changed': '2021-03-23T15:37:30Z', 'checkin_type': 0, 'is_printed': False, 'qr_code_url': 'https://www.eventbriteapi.com/qrcode/16596446692314922795001/?sig=AHTu1yYrsKf-3LxNci4Qqhq70d4wb1XXjQ'}], 'answers': [{'answer': 'Email', 'question': 'How did you hear about this event?', 'type': 'text', 'question_id': '38655171'}, {'answer': 'No', 'question': 'Do you identify as black, indigenous, and/or a person of color? ', 'type': 'multiple_choice', 'question_id': '38655173'}, {'answer': 'Arab, Middle Eastern, or North African | White or Caucasian', 'question': 'What is your race? Check all that apply.', 'type': 'multiple_choice', 'question_id': '38655175'}], 'checked_in': False, 'cancelled': False, 'refunded': False, 'affiliate': 'oddtdteb', 'guestlist_id': None, 'invited_by': None, 'status': 'Attending', 'ticket_class_name': 'Member Ticket', 'delivery_method': 'electronic', 'event_id': '132582739543', 'order_id': '1659644669', 'ticket_class_id': '230905845'}]}

accountID = '0018A00000dGK0rQAG'


if "promotional_code" in attendee.keys():
    sf.Opportunity.create({'AccountId':accountID, 'npsp__Primary_Contact__c':contactID, 'EventbriteSync__Buyer__c':buyerID, 'amount':attendee['costs']['gross']['major_value'], 'stage':'posted', 'CloseDate':attendee['created'], 'CampaignId':campaignID, 'Order_Number__c':attendee['order_id'], 'Ticket_Type__c':attendee['ticket_class_name'], 'RecordTypeId':'012f4000000JdASAA0' 'Coupon_Code__c':attendee['promotional_code']['code']})
else:




#  result = sf.Contact.create({'Email':attendee['profile']['email'], 'FirstName':attendee['profile']['first_name'], 'LastName':attendee['profile']['last_name'], 'npsp__Primary_Affiliation__c':attendee['profile']['companyID']})
# print(result)
# newContactID = result['id']

# createAccountResult = sf.Account.create({'Name':'Andrew Corp2'})
# print(createAccountResult)
# print(createAccountResult['id'])

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