from requests.models import Response
import main
import requests
import flask
import simple_salesforce
from threading import Thread
import time

def processor(request):
    requestJSON = {
        "api_url": "https://www.eventbriteapi.com/v3/orders/1694679905/",
        "config": {
            "action": "order.placed",
            "endpoint_url": "https://us-central1-technofly.cloudfunctions.net/test-env-technofly",
            "user_id": "520204566129",
            "webhook_id": "8371572"
        }
        }
    task = Thread((requests.async.post('https://us-central1-technofly.cloudfunctions.net/test-env-technofly', json=requestJSON)), daemon=True)
    task.run()
    #print(task)
    #task.start()
    time.sleep(1)
    print("done")
    #return Response(200)

processor("gjrn")