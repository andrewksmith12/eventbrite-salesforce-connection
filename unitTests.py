from unittest import TestCase
from main import AUTH_HEADER_EB, getSalesforce, createEvent, processOrder, format_soql
import creds
import requests

TEST_EVENT_URL = "https://www.eventbriteapi.com/v3/events/151257855317/"
TEST_ORDER_URL = "https://www.eventbriteapi.com/v3/orders/1689902917/"
TEST_ORDER_EXCEPTION_URL = "https://www.eventbriteapi.com/v3/orders/1689899509/"
TEST_EMAIL = "APITESTEMAIL@example.com"

class TestApplication(TestCase):
    def validateSalesforceCreds(self):
        #Ensure API authentication is working. If no error, pass. 
        sf = getSalesforce()
    def validateEventbriteCreds(self):
        #Ensure API authentication is working. If no error, pass. 
        authHeader = AUTH_HEADER_EB
        r = requests.get("https://www.eventbriteapi.com/v3/users/me", headers=AUTH_HEADER_EB)
        self.assertEqual(r.status_code==200)
    def validateCreateEvent(self):
        #Ensure Event Creation function is working. Create a test event in salesforce given an eventbrite API url and then delete it. 
        eventID = createEvent(TEST_EVENT_URL)
        sf = getSalesforce()
        sf.Campaign.delete(eventID)
    def validateProcessOrder(self):
        eventID = createEvent(TEST_EVENT_URL)
        processOrder(TEST_ORDER_URL)
        sf = getSalesforce()
        createdContact = sf.query(format_soql("SELECT Id FROM Contact WHERE Email = '{email}'".format(email=TEST_EMAIL)))
        # if createdContact['totalSize'] ==1:
        #     sf.
        sf.query()
    def validateProcessOrderException(self):
        eventID = createEvent(TEST_EVENT_URL)
        processOrder(TEST_ORDER_EXCEPTION_URL)
        sf = getSalesforce()
        sf.query()
        