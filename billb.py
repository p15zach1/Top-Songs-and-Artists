import sys
import json
import requests
import billboard

def billb(num, s_a):

	if(s_a == 'songs'):

		songs = billboard.ChartData('hot-100')

		output = ""
		i = 0
		while i<int(num):
			output += str(i+1) + " - " + songs[i].title + " -- " + songs[i].artist + "\n"
			print(str(i+1) + " - " + songs[i].title + " -- " + songs[i].artist)
			i += 1

	if(s_a == "artists"):

		artists = billboard.ChartData('artist-100')

		output = ""
		i = 0
		while i<int(num):
			output += str(i+1) + " - " + artists[i].artist + "\n"
			print(str(i+1) + " - " + artists[i].artist)
			i += 1

	return output
		
