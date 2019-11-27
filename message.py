def vmessage(body,vphone):
    from twilio.rest import Client
    # Your Account Sid and Auth Token from twilio.com / console
    account_sid = 'Axxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    auth_token = 'bxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

    client = Client(account_sid, auth_token)

    ''' Change the value of 'from' with the number
    received from Twilio and the value of 'to'
    with the number in which you want to send message.'''
    message = client.messages.create(
                                from_='mobile no.',
                                body =body,
                                to = str(vphone)
                            )

    print("Message sent to the visitor")
    return 0

def hmessage(body,hphone):
    from twilio.rest import Client
    # Your Account Sid and Auth Token from twilio.com / console
    account_sid = 'Axxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    auth_token = 'bxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

    client = Client(account_sid, auth_token)

    ''' Change the value of 'from' with the number
    received from Twilio and the value of 'to'
    with the number in which you want to send message.'''
    message = client.messages.create(
                                from_='+1*******68',
                                body = body,
                                to = str(hphone)
                            )

    print("Message sent to the Host")
    return 0

