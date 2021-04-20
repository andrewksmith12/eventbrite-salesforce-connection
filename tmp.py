import smtplib
gmail_user = "teamtechnofly@gmail.com"
gmail_password = "jvrkiludpjmrqdiz"
email_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
email_server.ehlo()
email_server.login(gmail_user, gmail_password)
message = """Subject: Error in Create Campaign Member
Hello There, this is an email sent via python3"""
email_server.sendmail(from_addr=gmail_user, to_addrs="andrewkeithsmith12@gmail.com", msg=message)