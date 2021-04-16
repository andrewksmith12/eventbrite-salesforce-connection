import requests
import creds
import json
from simple_salesforce import Salesforce, format_soql
SANDBOX_URL = creds.SF_SANDBOX_URL
PROD_URL = creds.SF_PROD_URL
USERNAME = creds.SF_USERNAME
PASSWORD = creds.SF_PASSWORD
PROD_PASSWORD = creds.SF_PROD_PASSWORD
SANDBOX_SECURITY_TOKEN = creds.SF_SANDBOX_SECURITY_TOKEN
PROD_SECURITY_TOKEN = creds.SF_PROD_SECURITY_TOKEN
DOMAIN = "test"

# Sandbox sf Object
sf = Salesforce(instance=SANDBOX_URL, username=creds.SF_SANDBOX_USERNAME, password=PROD_PASSWORD, security_token=SANDBOX_SECURITY_TOKEN, domain=DOMAIN)
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


# accountID = '0018A00000dGK0rQAG'
# campaignID = '7018A000000U2c9QAC'
# contactID = '0038A00000ZVhpbQAD'
# buyerID = '0038A00000ZVhpbQAD'
# attendee = {'costs': {'base_price': {'display': '$0.00', 'currency': 'USD', 'value': 0, 'major_value': '0.00'}, 'eventbrite_fee': {'display': '$0.00', 'currency': 'USD', 'value': 0, 'major_value': '0.00'}, 'gross': {'display': '$0.00', 'currency': 'USD', 'value': 0, 'major_value': '0.00'}, 'payment_fee': {'display': '$0.00', 'currency': 'USD', 'value': 0, 'major_value': '0.00'}, 'tax': {'display': '$0.00', 'currency': 'USD', 'value': 0, 'major_value': '0.00'}}, 'resource_uri': 'https://www.eventbriteapi.com/v3/orders/1679046901/attendees/2344603415/', 'id': '2344603415', 'changed': '2021-04-08T16:40:22Z', 'created': '2021-04-08T16:40:22Z', 'quantity': 1, 'variant_id': None, 'profile': {'first_name': 'Julie', 'last_name': 'Candoli', 'addresses': {}, 'company': 'Foundation Communities', 'name': 'Julie Candoli', 'email': 'julie.candoli@foundcom.org', 'job_title': 'Director of Institutional Giving'}, 'barcodes': [{'status': 'unused', 'barcode': '16790469012344603415001', 'created': '2021-04-08T16:40:24Z', 'changed': '2021-04-08T16:40:24Z', 'checkin_type': 0, 'is_printed': False, 'qr_code_url': 'https://www.eventbriteapi.com/qrcode/16790469012344603415001/?sig=AHTu1yajawIe18aZ57GKVRtPDCaqQqDj5Q'}], 'answers': [{'answer': 'MSDF email', 'question': 'How did you hear about this event?', 'type': 'text', 'question_id': '40969885'}, {'answer': 'No', 'question': 'Do you identify as black, indigenous, and/or a person of color? ', 'type': 'multiple_choice', 'question_id': '40969887'}, {'answer': 'White or Caucasian', 'question': 'What is your race? Check all that apply.', 'type': 'multiple_choice', 'question_id': '40969889'}], 'checked_in': False, 'cancelled': False, 'refunded': False, 'affiliate': 'ebdsoporgprofile', 'guestlist_id': None, 'invited_by': None, 'status': 'Attending', 'ticket_class_name': 'Member Ticket', 'delivery_method': 'electronic', 'event_id': '144674887483', 'order_id': '1679046901', 'ticket_class_id': '251835763', 'promotional_code': {'resource_uri': 'https://www.eventbriteapi.com/v3/events/144674887483/discounts/398818038/', 'id': '398818038', 'promotion': '100.00% - MSDF100', 'promotion_type': 'discount', 'code': 'MSDF100', 'percent_off': '100.00'}}
# pocAnswer = ""
# raceAnswer = ""
# raceFreeResponse = ""
# otherQuestions = ""

# response = sf.CampaignMember.create(
#     {'CampaignId':campaignID,
#     'ContactId':contactID,
#     'EventbriteSync__EventbriteId__c':attendee['id'],
#     'Eventbrite_Attendee_ID__c':attendee['id'],
#     'Eventbrite_Fee__c':attendee['costs']['eventbrite_fee']['major_value'],
#     'Total_Paid__c':attendee['costs']['base_price']['major_value'],
#     'Ticket_Type__c':attendee['ticket_class_name'],
#     'Status':attendee['status'],
#     'Identifies_as_BIPOC__c':pocAnswer,
#     'Race__c':raceAnswer,
#     'Race_self_describe__c':raceFreeResponse,
#     'Comments__c':otherQuestions})
# print(response)




# attendee = {'costs': {'base_price': {'display': '$0.00', 'currency': 'USD', 'value': 0, 'major_value': '0.00'}, 'eventbrite_fee': {'display': '$0.00', 'currency': 'USD', 'value': 0, 'major_value': '0.00'}, 'gross': {'display': '$0.00', 'currency': 'USD', 'value': 0, 'major_value': '0.00'}, 'payment_fee': {'display': '$0.00', 'currency': 'USD', 'value': 0, 'major_value': '0.00'}, 'tax': {'display': '$0.00', 'currency': 'USD', 'value': 0, 'major_value': '0.00'}}, 'resource_uri': 'https://www.eventbriteapi.com/v3/orders/1679046901/attendees/2344603415/', 'id': '2344603415', 'changed': '2021-04-08T16:40:22Z', 'created': '2021-04-08T16:40:22Z', 'quantity': 1, 'variant_id': None, 'profile': {'first_name': 'Julie', 'last_name': 'Candoli', 'addresses': {}, 'company': 'Foundation Communities', 'name': 'Julie Candoli', 'email': 'julie.candoli@foundcom.org', 'job_title': 'Director of Institutional Giving'}, 'barcodes': [{'status': 'unused', 'barcode': '16790469012344603415001', 'created': '2021-04-08T16:40:24Z', 'changed': '2021-04-08T16:40:24Z', 'checkin_type': 0, 'is_printed': False, 'qr_code_url': 'https://www.eventbriteapi.com/qrcode/16790469012344603415001/?sig=AHTu1yajawIe18aZ57GKVRtPDCaqQqDj5Q'}], 'answers': [{'answer': 'MSDF email', 'question': 'How did you hear about this event?', 'type': 'text', 'question_id': '40969885'}, {'answer': 'No', 'question': 'Do you identify as black, indigenous, and/or a person of color? ', 'type': 'multiple_choice', 'question_id': '40969887'}, {'answer': 'White or Caucasian', 'question': 'What is your race? Check all that apply.', 'type': 'multiple_choice', 'question_id': '40969889'}], 'checked_in': False, 'cancelled': False, 'refunded': False, 'affiliate': 'ebdsoporgprofile', 'guestlist_id': None, 'invited_by': None, 'status': 'Attending', 'ticket_class_name': 'Member Ticket', 'delivery_method': 'electronic', 'event_id': '144674887483', 'order_id': '1679046901', 'ticket_class_id': '251835763', 'promotional_code': {'resource_uri': 'https://www.eventbriteapi.com/v3/events/144674887483/discounts/398818038/', 'id': '398818038', 'promotion': '100.00% - MSDF100', 'promotion_type': 'discount', 'code': 'MSDF100', 'percent_off': '100.00'}}
# accountID = '0018A00000dGK0rQAG'
# campaignID = '7018A000000U166QAC'
# contactID = '0038A00000ZVhpbQAD'
# buyerID = '0038A00000ZVhpbQAD'

# if "promotional_code" in attendee.keys():
#     sf.Opportunity.create({'AccountId':accountID, 'npsp__Primary_Contact__c':contactID, 'EventbriteSync__Buyer__c':buyerID, 'amount':attendee['costs']['gross']['major_value'], 'StageName':'posted', 'CloseDate':attendee['created'], 'CampaignId':campaignID, 'Order_Number__c':attendee['order_id'], 'Ticket_Type__c':attendee['ticket_class_name'], 'RecordTypeId':'012f4000000JdASAA0', 'Coupon_Code__c':attendee['promotional_code']['code'], 'Name':'testName'})
# else:
#     sf.Opportunity.create({'AccountId':accountID, 'npsp__Primary_Contact__c':contactID, 'EventbriteSync__Buyer__c':buyerID, 'amount':attendee['costs']['gross']['major_value'], 'StageName':'posted', 'CloseDate':attendee['created'], 'CampaignId':campaignID, 'Order_Number__c':attendee['order_id'], 'Ticket_Type__c':attendee['ticket_class_name'], 'RecordTypeId':'012f4000000JdASAA0', 'Name':'testName'})




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


# result = sf.Contact.create(
#     {'Email':attendee['profile']['email']+"3", 
#     'FirstName':attendee['profile']['first_name']+"3", 
#     'LastName':attendee['profile']['last_name']+"3", 
#     'Title':attendee['profile']['job_title']+"3"})
# contactID = result['id']
# result = sf.Opportunity.create({'AccountId':"", 'npsp__Primary_Contact__c':contactID, 'EventbriteSync__Buyer__c':contactID, 'amount':attendee['costs']['gross']['major_value'], 'StageName':'posted', 'CloseDate':attendee['created'], 'CampaignId':campaignID, 'Order_Number__c':attendee['order_id'], 'Ticket_Type__c':attendee['ticket_class_name'], 'RecordTypeId':'012f4000000JdASAA0', 'Name':'tempName'})
# print(result)

# sf.Payment.create({})
# result = sf.Opportunity.create({'AccountId':'0017h00000XpNWPAA3', 'npsp__Primary_Contact__c':'0037h00000RkN8TAAV', 'EventbriteSync__Buyer__c':'0037h00000RkN8TAAV', 'StageName':'posted', 'CloseDate':"2021-03-25T19:23:04Z", 'CampaignId':'7017h000000xOe6AAE', 'Order_Number__c':'1686870425', 'Ticket_Type__c':"Nonmember Ticket", 'RecordTypeId':'012f4000000JdASAA0', 'Name':'tempName', 'amount':'20.00'})
# print(result)
# opID = result['id']
# result = sf.npe01__OppPayment__c.create({'npe01__Opportunity__c':opID, 'npe01__Paid__c':True, 'Payment_Contact__c':'0038A00000ZVhpbQAD', 'Ready_for_Invoice__c':True, 'npe01__Payment_Amount__c':'50.00'})
#print(result)
# sfCM = sf.query("SELECT Id FROM CampaignMember WHERE Eventbrite_Attendee_ID__c = '{ebAttendee}'".format(ebEventID=attendee['event_id']))
searchterm = "Mobile Loaves & Fishes, Inc."
qs = sf.quick_search(format_soql("{{Mobile Loaves & Fishes, Inc.}}"))
print(qs)