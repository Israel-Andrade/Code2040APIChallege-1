"""The modules used were requests to access the post method"""
import requests
"""The json module to use json dictionary"""
import json
from requests.utils import quote

"""The registration endpoint for our API"""
url = 'http://challenge.code2040.org/api/register'

"""Our dictionary entitled payload with two keys. Our token which hold the value for our api t
	oken and github key which holds our github URL"""

payload = {
	'token': '03cbcbfd47031937a28ff8bb5eccb71a',
	'github': 'https://github.com/IsraelAndrade22/Code2040APIChallenge'
}

"""Request post method to register to our endpoint. The medthod will have two parameteres,
   our url for the registration endpoint and json dictionary"""

r = requests.post(url, data = payload)
print(r.text)
