from twilio.rest import Client
from decouple import config  # Only if using environment variables

# Use environment variables for sensitive information
account_sid = config('TWILIO_ACCOUNT_SID')  # Replace with your actual Account SID
auth_token = config('TWILIO_AUTH_TOKEN')      # Replace with your actual Auth Token
twilio_phone_number = config('TWILIO_PHONE_NUMBER')  # Your Twilio phone number
test_phone_number = '+1234567890'  # Replace with a valid recipient phone number

# Initialize the Twilio client
client = Client(account_sid, auth_token)

try:
    # Send a test message
    message = client.messages.create(
        body='This is a test message from Twilio!',
        from_=twilio_phone_number,  # Your Twilio number
        to=test_phone_number         # The recipient's number
    )
    print(f'Message sent successfully! SID: {message.sid}')
except Exception as e:
    print(f'Failed to send message: {e}')
