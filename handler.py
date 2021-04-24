import requests
import threading
import time
from flask import Flask, request, Response
def makeRequest(data):
    try:
        requests.post("https://us-central1-technofly.cloudfunctions.net/test-env-technofly", json=data)
    finally:
        print("done")

def handler(request):
    print("Recieved request, printing json")
    data = request.get_json()
    print(data)
    x = threading.Thread(target=makeRequest, args=(data,), daemon=True)
    print("daemon created")
    x.start()
    print("started")
    time.sleep(1)
    print("1 second done. ")
    return Response(status=200)
