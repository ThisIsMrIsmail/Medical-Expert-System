import requests
import json

BASE = "http://127.0.0.1:5000"

user_data = {
    "headache": True,
    "back_pain": True,
    "chest_pain": False,
    "cough": True,
    "fainting": True,
    "sore_throat": False,
    "fatigue": False,
    "restlessness": True,
    "low_body_temp": False,
    "fever": True,
    "sunken_eyes": False,
    "nausea": False,
    "blurred_vision": False
    # "blurred_vision": True
}

response = requests.post(
    url=BASE + "/api",
    headers={"Content-Type": "application/json"},
    data=json.dumps(user_data),
)

print( response.json() )

# curl -X POST http://127.0.0.1:5000/api -H 'Content-Type: application/json' -d '{"name": "hello", "age": 22}'
# curl -X POST https://medicales.vercel.app/api -H 'Content-Type: application/json' -d '{"name": "hello", "age": 22}'