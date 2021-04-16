from unittest import TestCase
from main import AUTH_HEADER_EB, getSalesforce
import creds
import requests

class TestApplication(TestCase):
    def validateSalesforceCreds(self):
        #Ensure API authentication is working. If no error, pass. 
        sf = getSalesforce()
    def validateEventbriteCreds(self):
        authHeader = AUTH_HEADER_EB
        r = requests.get("https://www.eventbriteapi.com/v3/users/me", headers=AUTH_HEADER_EB)
        self.assertEqual(r.status_code==200)