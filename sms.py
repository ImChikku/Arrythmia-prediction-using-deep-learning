def main():
    """
    Send an SMS message for testing purposes.
    """
    phone = '+919344240352' # <-- Enter your own phone number here
    smsmsg = 'Test message using the Textbelt web API.'
    apikey = 'AC6cec03edff83947ab119fa6f1f0ab7fc' # <-- Change to your API key, if desired

    # Attempt to send the SMS message.
    if send_textbelt_sms(phone, smsmsg, apikey):
        print('SMS message successfully sent!')
    else:
        print('Could not send SMS message.')
