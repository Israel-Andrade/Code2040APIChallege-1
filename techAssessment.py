import requests
import json
import math
import datetime
import time

#The registration endpoint for our API
url = 'http://challenge.code2040.org/api/register'
token = '03cbcbfd47031937a28ff8bb5eccb71a'
github ='https://github.com/IsraelAndrade22/Code2040APIChallege'

def apiRegistration(url_endpoint, token, github_url):
	"""Request post method to register to our endpoint. The medthod will have two parameteres,
	our url for the registration endpoint and json dictionary"""

	payload = {
	'token': token,
	'github': github_url
	}
	r = requests.post(url_endpoint, data = payload)
	print(r.text)
apiRegistration(url, token, github)
