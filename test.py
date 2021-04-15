import main
import json
import requests
eventList = ["136466040601", "137489437609", "136012612385", "149906679915", "144704734757", "148367736895", "148684261629", "136009757847", "149178313351", "149960466793", "141374778769", "150621160947", "132578855927", "136015085783", "136014315479", "139708432683", "150825066835", "145939824945", "136016090789", "150629279229", "144673525409", "132583058497", "150631180917", "150630717531", "132578908083", "144704748799", "150638575033", "149915205415", "150625670435", "149914212445", "144674456193", "144704768859", "150625850975", "149902457285", "150601628525", "144674887483", "144704778889", "144704800955"]
for eventID in eventList:
    print("Processing Event ID: "+eventID)
    api_url = "https://www.eventbriteapi.com/v3/events/"+eventID+"/orders"
    print(api_url)
    r = requests.get(api_url, headers=main.AUTH_HEADER_EB, params={"expand":["category","promotional_code"]})
    r = r.json()
    for order in r['orders']:
        print("Processing order: "+order['id']+" in event: "+eventID)
        main.processOrder(order['resource_uri'])