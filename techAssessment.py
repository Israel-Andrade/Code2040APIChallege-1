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


#The Endpoint to our next challenge 
url_reverse = 'http://challenge.code2040.org/api/reverse'
#The URL to post our JSON object
url_validate = 'http://challenge.code2040.org/api/reverse/validate'

def reverseString(url_reverse, url_validate, token):
	"""Obtain a string value from our url_reverse endpoint and 
	return the string reversed to the url_validate"""
	#Dictionary with the key being our token
	payload = {
		'token': token
	}
	#Post method to the endpoint which will return a string 
	r = requests.post(url_reverse, data = payload)
	#Work will be converted to a string returned by the post method
	word = str(r.content)
	#Reverse the string word
	reversed_word = word[::-1]
	#Dictionary that will be used in our post method
	#The key values will be the token for our challenge
	#And the string word reversed
	payload = {
		'token': token,
		'string': reversed_word
	}
	r = requests.post(url_validate, data = payload)
	print(r.content)
reverseString(url_reverse, url_validate, token)