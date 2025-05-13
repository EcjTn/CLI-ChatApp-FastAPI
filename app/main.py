from fastapi import FastAPI, Path, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(docs_url=None, redoc_url=None)

chatroom1 = {}
chatroom2 = {}
message_counter1 = 0  # Global counter for message IDs
message_counter2 = 0  # Global counter for message IDs


class MessageFormat(BaseModel):
    username: str
    message: str


@app.post("/messages/room/1")
async def send_msg(msg: MessageFormat):

    global message_counter1
    message_counter1 += 1

    if msg.username == "":
        msg.username = "Anonymous"



    chatroom1[message_counter1] = {
        "username": msg.username,
        "message": msg.message
    }
    return "Welcome to Room 1", chatroom1




@app.post("/messages/room/2")
async def send_msg(msg: MessageFormat):

    global message_counter2
    message_counter2 += 1

    if msg.username == "":
        msg.username = "Anonymous"



    chatroom2[message_counter2] = {
        "username": msg.username,
        "message": msg.message
    }
    return "Welcome to Room 2", chatroom2







@app.get("/messages/room/")
def showRooms():
    return {
        "Room 1": chatroom1,
        "Room 2": chatroom2
    }
