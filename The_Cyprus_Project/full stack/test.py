from flask.wrappers import Response
import requests
BASE = "http://127.0.0.1:5000/"
response = requests.post(
    BASE + "/add_admin", data={"password": "admin", "username": "admin", "author": "king", "date": ""})
print(response)
