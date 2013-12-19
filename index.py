import plivo


message_params = {
      'src':plivo_number,
      'dst':destination_number,
      'text':text,
    }

p = plivo.RestAPI(PLIVO_AUTH_ID, PLIVO_AUTH_TOKEN)

print p.send_message(message_params) 
