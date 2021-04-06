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


things_to_do = dir(sf)
print(sf.query("SELECT Name, Email, Primary_Affiliation_text__c FROM Contact WHERE Email = 'headmaster@hogwarts.edu'"))