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

#Our endpoint to receive a specific word (needle) and an array of strings (haystack)
url_haystack = 'http://challenge.code2040.org/api/haystack'
#The URL to post our JSON object
url_validate = 'http://challenge.code2040.org/api/haystack/validate'

def findTheNeedle(url_haystack, url_validate, token):
	"""Find a specific string in an array of string values. Locate and return
	the index the string"""
	#Dictionary with the key being our token
	payload = {
		'token': token
	}
	#Our post method to the endpoint which will return a string word and
	#an array of strings
	r = requests.post(url_haystack, data=payload)
	#Empty dictionary to store JSON object from the post method
	my_dict = {}
	my_dict = r.json()
	#Storing the array of strings
	haystack = my_dict['haystack']
	#Storing the string word 
	needle = my_dict['needle']
	#Variable to keep track of the current index
	index = 0
	#A for loop to transverse through the array of strings
	#to locate the target word
	for hay in haystack:
		if(hay == needle):
			payload = {
				'token': token,
				'needle': index
			}
			r = requests.post(url_validate, data=payload)
			print r.content
			return
		index += 1
findTheNeedle(url_haystack, url_validate, token)

#Our endpoint to receive a the prefix string and an array of words
url_prefix = 'http://challenge.code2040.org/api/prefix'
#The URL to post our JSON object
url_validate = 'http://challenge.code2040.org/api/prefix/validate'


def removePrefix(url_prefix, url_validate, token):
	"""Return an array containing only the strings that do not start with the
	prefix """
	#This is a dictionary holding my token key
	payload = {
		'token': token
	}

	#Sending a post request with a dictionary holding my token
	r = requests.post(url_prefix, data=payload)
	#Initialize dictionary to the dictionary obtained by the post request
	my_dict = r.json()
	#Initialize a variable called prefix the key value of prefix which should hold the string prefix
	prefix = my_dict['prefix']
	#Obtain the length the prefix
	length_of_prefix = len(prefix)
	#Initialize this array to the array of string I got back from the post request
	my_array = my_dict["array"]
	#Create a new array to hold all the string values that do not start
	#with the prefix
	new_array = []
	#array will transverse through the array of string and
	#checking the condition where a word in the array 
	#does not start with the prefix
	for word in my_array:
		if not (word[:length_of_prefix] == prefix):
			new_array.append(str(word))


	#Initializing a new dictinary to hold the token and new array 
	#without words starting with the prefix
	payload = {
		'token': token,
		'array': new_array
	}
	r = requests.post(url_validate, json=payload)
	print r.content
#Calling the function and passing in three argumnets which consists of
#Our prefix url to obtain our dictionary, url to validate our dictionary, and 
#our token
removePrefix(url_prefix, url_validate, token)