#this is for the ticket created webook

if #attendee email exists in salesforce

    if #primary affilaition matches
        #Update FName/LName to match eventbrite registration, add demographic info if not blank in Eventbrite. Add as campaign member in salesforce

    else 
        if #primary affiliation on eventbrite blank
            #Update FName/LName, Add as a campaign member in Salesforce

        else 
            if #the primary affiliation exist as an organization on salesforce
                #Update FName/LName, Title, primary affiliation, and  demographic info if not blank in eventbrite. 

            else 
                #Create new Account (Organization) in Salesforce for primary affiliation. 
                #Update FName/LName, Title, primary affiliation, and  demographic info if not blank in eventbrite. 

else
    if #a contact exists in salesforce with the same name
        if #the primary affilaition matches
            #Update FName/LName, Email, Title, add demographic Info if present in eventbrite. 
        else
            if #primary affiliation is blank
                #Create a New contact: FName/LName, email, Title, demographic info if present in eventbrite.

            else
                if #primary affiliation exist as an account in salesforce
                    #Create a new Contact record: FName/LName, Email, title, primary affiliation, demographic info if present in eventbrite. 

                else
                    #Create a new account in salesforce for primary affiliation
                    #Create a new Contact record: FName/LName, Email, title, primary affiliation, demographic info if present in eventbrite. 
    else
        if #primary affiliation exist in salesforce
            #Create a new contact record: FName/LName, Email, Title, Primay Affiliation, demographic info if present in Eventbrite
        else
            #create a new account for primary affiliation
            #Create a new contact record: FName/LName, Email, Title, Primay Affiliation, demographic info if present in Eventbrite
