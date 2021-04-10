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
sf = Salesforce(instance=SANDBOX_URL, username=USERNAME, password=PASSWORD, security_token=SANDBOX_SECURITY_TOKEN, domain=DOMAIN)

personQueryResult = sf.query("SELECT Id, Name, Primary_Affiliation_text__c FROM Contact WHERE Name='{ebName}' AND Primary_Affiliation_text__c='{ebCompany}'".format(ebName='Albus Dumbledore', ebCompany='Hogwarts School of Wizardry'))

print(personQueryResult)