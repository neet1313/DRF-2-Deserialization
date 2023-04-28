import requests
import json

URL='http://127.0.0.1:8000/student/'

data={
    'name': 'Henal',
    'roll': 1,
    'city': 'Mumbai'
}

json_data = json.dumps(data)
r = requests.post(url = URL, data=json_data)