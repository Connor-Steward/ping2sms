from twilio.rest import TwilioRestClient
import mail_pull2
import time


# Have to make individual API call for each unique phonenumber,
# Paid Twilio No = +61**********

def send_txt_connor():
    account_sid = "Twilio Acc SID"
    auth_token = "Twilio Acc auth token"
    client = TwilioRestClient(account_sid, auth_token)
    msg = mail_pull2.clean_data()
    _ = client.messages.create(body=msg, to="+61411111111", from_="+61422222222")  # Use _ for dummy variable
    time.sleep(2)
    print(_.sid)


def send_txt_yusuf():
    account_sid = "Twilio Acc SID"
    auth_token = "Twilio Acc auth token"
    client = TwilioRestClient(account_sid, auth_token)
    msg = mail_pull2.clean_data()
    _ = client.messages.create(body=msg, to="+61411111111", from_="+61422222222")  # Use _ for dummy variable
    time.sleep(2)
    print(_.sid)

def send_txt_damian():
    account_sid = "Twilio Acc SID"
    auth_token = "Twilio Acc auth token"
    client = TwilioRestClient(account_sid, auth_token)
    msg = mail_pull2.clean_data()
    _ = client.messages.create(body=msg, to="+61411111111", from_="+61422222222")  # Use _ for dummy variable
    time.sleep(2)
    print(_.sid)

def send_txt_richard():
    account_sid = "Twilio Acc SID"
    auth_token = "Twilio Acc auth token"
    client = TwilioRestClient(account_sid, auth_token)
    msg = mail_pull2.clean_data()
    _ = client.messages.create(body=msg, to="+61411111111", from_="+61422222222")  # Use _ for dummy variable
    time.sleep(2)
    print(_.sid)

