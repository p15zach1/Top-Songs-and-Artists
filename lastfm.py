import sys
import json
import requests

api_key = "e37c2ae808a631dfe7f545a52da52932"
secret_key = "71ccde1abe84fdc067f6b6d5da995a4c"

def lastfm(num, s_a):

	if(s_a == 'songs'):
		lastfm = requests.get("http://ws.audioscrobbler.com/2.0/?method=chart.gettoptracks&api_key=" + api_key + "&format=json").json()

		output = ""
		i = 0
		while i<int(num):
			output += str(i+1) + " - " + lastfm['tracks']['track'][i]['name'] + " -- " + lastfm['tracks']['track'][i]['artist']['name'] + "\n"
			print(i+1, lastfm['tracks']['track'][i]['name'], "--", lastfm['tracks']['track'][i]['artist']['name'])
			i += 1

	elif(s_a == 'artists'):
		lastfm = requests.get("http://ws.audioscrobbler.com/2.0/?method=chart.gettopartists&api_key=" + api_key + "&format=json").json()

		output = ""
		i = 0
		while i<int(num):
			output += str(i+1) + " - " + lastfm['artists']['artist'][i]['name'] + "\n"
			print(i+1, lastfm['artists']['artist'][i]['name'])
			i += 1

	return output
