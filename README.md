# FastAPI Chatroom API

This is a simple chatroom backend built using FastAPI. It allows users to send messages to a specific chatroom (Room 1) using HTTP POST requests.

- Users can send messages with a username and message.
- If no username is provided, it will default to random strings.
- Messages are stored in a Python dictionary.
- Data is not saved permanently. Once the server stops, all messages are lost.
- Use only for temporary messages
- Messages only appear/updated when API request is sent





# Dependencies

- fastapi
- uvicorn
- requests
- pydantic



# Run

uvicorn main:app --reload


