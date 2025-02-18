from twilio.rest import Client

import requests 

url = 'http://hackathons.masterschool.com:3030/whatsapp/getMessages/'

header = 'accept: application/json'

response = request.get(url, headers= header)

if response.status_code = 200



account_sid = ''
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  content_sid='',
  content_variables='{"1":"12/1","2":"3pm"}',
  to='whatsapp:+491737523673'
)


def get_user_responses():
    pass

exports.handler = (context, event, callback) => {
  // No need to import Twilio; it is globally available in Functions
  const response = new Twilio.Response();

  response
    // Set the status code to 200 OK
    .setStatusCode(200)
    // Set the response body
    .setBody('This is fine');

  return callback(null, response);
};

print(message.sid)

