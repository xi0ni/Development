from twilio.rest import Client

# in this part you have to replace account_sid
# auth_token, twilio_number, recipient_number with your actual credential

account_sid = "US683a36a8b445f2a5acd710a7dcb9650e"
auth_token = "928f9bc52825c8de7b508223fba29945"
twilio_number = "+18885929304"
recipient_number = "+16465930397"

# Create Twilio client
client = Client(account_sid, auth_token)

# Send SMS
# in body part you have to write your message
message = client.messages.create(
    body="This is a new message", from_=twilio_number, to=recipient_number
)

print(f"Message sent with SID: {message.sid}&")
