import unittest
from main import AUTH_HEADER_EB, getSalesforce, createEvent, processOrder, format_soql, requests

TEST_EVENT_URL = "https://www.eventbriteapi.com/v3/events/151257855317/"
TEST_EMAIL = "APITESTEMAIL@example.com"

class TestApplication(unittest.TestCase):
    def testSalesforceCreds(self):
        #Ensure API authentication is working. If no error, pass. 
        sf = getSalesforce()
    def testEventbriteCreds(self):
        #Ensure API authentication is working. If no error, pass. 
        authHeader = AUTH_HEADER_EB
        r = requests.get("https://www.eventbriteapi.com/v3/users/me", headers=AUTH_HEADER_EB)
        self.assertEqual(r.status_code, 200)
    def testCreateEvent(self):
        #Ensure Event Creation function is working. Validate SF account has create/delete permissions.  
        eventID = createEvent(TEST_EVENT_URL)
        sf = getSalesforce()
        sf.Campaign.delete(eventID)
    def testProcessOrder(self):
        eventID = createEvent(TEST_EVENT_URL)
        sf = getSalesforce()
        processOrder()
        sf.Campaign.delete(eventID)

if __name__ == '__main__':
    unittest.main()