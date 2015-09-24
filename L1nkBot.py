import requests
import threading
import time
import os

token = open(os.path.join(".", "token.txt"), "r").read()
url = "https://api.telegram.org/" + "bot" + token + "/"
update_url = url + "getUpdates"
send_message_url = url + "sendMessage"

def get_message():
    return requests.get(update_url).json()

def get_chat_id(message):
    return message[u"result"][0][u"message"][u"from"][u"id"]

def get_update_id(message):
    return message[u"result"][0][u"update_id"]

def get_updates_message(payload = {"offset": 0}):
    return requests.get(update_url, payload).json()

update_id = get_update_id(get_message())
print update_id
while True:   
    print "running"
    message = get_updates_message({"offset": update_id})   
    if message[u"result"] != []:
        print "new message: \n"
        print message
        chat_id = get_chat_id(message)        
        print "CHAT ID: " + str(chat_id)
        print "UPDATE ID: " + str(update_id)
        payload = {"chat_id": chat_id, "text": "HIII"}
        r = requests.post(send_message_url, payload)
        print "Response: "
        print r
        update_id += 1
    time.sleep(2)
