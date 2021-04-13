andrewDict = {}
andrewDict['Hello'] = "world"
for i in andrewDict:
    print(i)
    print(andrewDict[i])


 sf.CampaignMember.create(
        {'CampaignId':'campaignID',
        'ContactId':'contactID',
        'EventbriteSync__EventbriteId__c':'attendee['id']',
        'Eventbrite_Attendee_ID__c':'attendee['id']',
        'Eventbrite_Fee__c':'attendee['costs']['eventbrite_fee']['major_value']',
        'Total_Paid__c':'attendee['costs']['base_price']',
        'Ticket_Type__c':'attendee['ticket_class_name']',
        'Status':'attendee['status']',
        'Identifies_as_BIPOC__c':'pocAnswer',
        'Race__c':'raceAnswer',
        'Race_self_describe__c':'raceFreeResponse',
        'Comments__c':'otherQuestions'})