import requests
import json
import random
import string
import os


letras = string.ascii_letters
letras += string.digits

usrPicked = input("Enter username: ")

if usrPicked == "":
    for x in range(15):
        usrPicked += random.choice(letras)

roomPicked = input('Enter Room number(1/2): ')
while True:
    msgPicked = input("Your message: ")


    url = f"http://127.0.0.1:8000/messages/room/{roomPicked}"


    data = {
     "username": usrPicked,
        "message": msgPicked
    }

    os.system("cls")

    response = requests.post(url, json=data)

    response_data = response.json()



    chatroom = response_data[1]
    
    for msg_id in sorted(chatroom):
        msg = chatroom[msg_id]
        print(f"[{msg_id}] {msg['username']}: {msg['message']}")


