from channels import Group

def ws_connect(message):
    print("Someone connected.")
    path = message['path']                                                      # i.e. /sensor/

    if path == b’/sensor/':
        print("Adding new user to sensor group")
        Group(“sensor").add(message.reply_channel)                             # Adds user to group for broadcast
        message.reply_channel.send({                                            # Reply to individual directly
           "text": "You're connected to sensor group :) ",
        })
    else:
        print("Strange connector!!")
