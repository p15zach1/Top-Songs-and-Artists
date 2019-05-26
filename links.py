import sys
import json
import requests
from bs4 import BeautifulSoup
import webbrowser

def getLastfmLink(name, s_a, ret):
	lastfm = requests.get("http://ws.audioscrobbler.com/2.0/?method=chart.gettoptracks&api_key=e37c2ae808a631dfe7f545a52da52932&format=json").json()

	if(name[3] == " "):
		name = name[4:]
	else:
		name = name[5:]
	artist = ""
	if(s_a == 'songs'):
		song = ""
		check = False
		songFlag = True
		for row in name:
			if(row != "-" and songFlag == True and check == False):
				song += row
			elif(row != "-" and songFlag == True and check == True):
				song += row
				check = False
			elif(songFlag == False):
				artist += row
			elif(row == "-" and songFlag == True and check == False):
				check = True
			elif(row == "-" and songFlag == True and check == True):
				songFlag = False

	elif(s_a == "artists"):
		for row in name:
			artist += row

	if(s_a == "songs"):
		song = song.replace("+", "%252B")
		song = song.replace(" ", "+")
		song = song.replace("!", "%21")
		song = song.replace("\"", "%22")
		song = song.replace("%", "%25")
		song = song.replace("'", "%27")
		song = song.replace("[", "%5B")
		song = song.replace("]", "%5D")
		song = song.replace("++", "+")
		if(song[0] == "+"):
			song = song[1:]
		if(song[-1] == "+"):
			song = song[0:-1]

	artist = artist.replace("+", "%252B")
	artist = artist.replace(" ", "+")
	artist = artist.replace("!", "%21")
	artist = artist.replace("\"", "%22")
	artist = artist.replace("%", "%25")
	artist = artist.replace("'", "%27")
	artist = artist.replace("[", "%5B")
	artist = artist.replace("]", "%5D")
	artist = artist.replace("++", "+")
	if(artist[0] == "+"):
		artist = artist[1:]
	if(artist[-1] == "+"):
		artist = artist[0:-1]

	if(s_a == "songs"):
		lastfmLink = "https://www.last.fm/music/" + artist + "/_/" + song

	elif(s_a == "artists"):
		lastfmLink = "https://www.last.fm/music/" + artist

	if(ret is True):
		return lastfmLink
	webbrowser.open_new(lastfmLink)

def getYoutubeLink(name, s_a):
	if(s_a == "songs"):
		link = getLastfmLink(name, s_a, True)
		page = requests.get(link)
		pageParser = BeautifulSoup(page.text, 'html.parser')
		x = pageParser.find_all('a', attrs={'class':'image-overlay-playlink-link js-playlink'})
		#youtubeLink = pageParser.find_all('data-youtube-url')
		txt = str(x)
		youtubeLink = ""
		counter = 0
		for row in txt:
			if(row == "h" and counter == 0):
				counter += 1
			elif(row == "r" and counter == 1):
				counter += 1
			elif(row == "e" and counter == 2):
				counter += 1
			elif(row == "f" and counter == 3):
				counter += 1
			elif(row == "=" and counter == 4):
				counter += 1
			elif(row == "\"" and counter == 5):
				counter += 1
			elif(row != "\"" and counter == 6):
				youtubeLink += row
			else:
				counter = 0
		if(youtubeLink != ""):
			print(youtubeLink)
		else:
			searchQuery = link[26:]
			searchQuery = searchQuery.replace("/_/", "+")
			searchQuery = searchQuery.replace("+&+", "+")
			youtubeLink = "https://www.youtube.com/results?search_query=" + searchQuery

	elif(s_a == "artists"):
		if(name[3] == " "):
			name = name[4:]
		else:
			name = name[5:]
		artist = ""
		for row in name:
			artist += row

		artist = artist.replace("+", "%252B")
		artist = artist.replace(" ", "+")
		artist = artist.replace("!", "%21")
		artist = artist.replace("\"", "%22")
		artist = artist.replace("%", "%25")
		artist = artist.replace("'", "%27")
		artist = artist.replace("[", "%5B")
		artist = artist.replace("]", "%5D")
		artist = artist.replace("++", "+")
		artist = artist.replace("&", "+")
		if(artist[0] == "+"):
			artist = artist[1:]
		if(artist[-1] == "+"):
			artist = artist[0:-1]

		youtubeLink = "https://www.youtube.com/results?search_query=" + artist

	print(youtubeLink)
	webbrowser.open_new(youtubeLink)

def getSpotifyLink(name, s_a):
	if(name[3] == " "):
		name = name[4:]
	else:
		name = name[5:]
	artist = ""
	if(s_a == "songs"):
		song = ""
		check = False
		songFlag = True
		for row in name:
			if(row != "-" and songFlag == True and check == False):
				song += row
			elif(row != "-" and songFlag == True and check == True):
				song += row
				check = False
			elif(songFlag == False):
				artist += row
			elif(row == "-" and songFlag == True and check == False):
				check = True
			elif(row == "-" and songFlag == True and check == True):
				songFlag = False

		song = song.replace(" ", "%20")

	elif(s_a == "artists"):
		for row in name:
			artist += row
	
	artist = artist.replace(" ", "%20")

	if(s_a == "songs"):
		spotifyLink = "https://open.spotify.com/search/results/" + song + artist
	elif(s_a == "artists"):
		spotifyLink = "https://open.spotify.com/search/results/" + artist

	webbrowser.open_new(spotifyLink)

def getItunesLink(name, s_a, prev):
	if(name[3] == " "):
		name = name[4:]
	else:
		name = name[5:]
	artist = ""
	if(s_a == "songs"):
		song = ""
		check = False
		songFlag = True
		for row in name:
			if(row != "-" and songFlag == True and check == False):
				song += row
			elif(row != "-" and songFlag == True and check == True):
				song += row
				check = False
			elif(songFlag == False):
				artist += row
			elif(row == "-" and songFlag == True and check == False):
				check = True
			elif(row == "-" and songFlag == True and check == True):
				songFlag = False

		song = song.replace(" ", "+")

	elif(s_a == "artists"):
		for row in name:
			artist += row

	artist = artist.replace(" ", "+")

	if(s_a == "songs"):
		results = requests.get("https://itunes.apple.com/search?term=" + song + "+" + artist + "&limit=1").json()
		if(prev == False):
			itunesLink = results['results'][0]['trackViewUrl']
		else:
			itunesLink = results['results'][0]['previewUrl']

	elif(s_a == "artists"):
		results = requests.get("https://itunes.apple.com/search?term=" + artist + "&limit=1").json()
		itunesLink = results['results'][0]['artistViewUrl']
		
	print(itunesLink)
	webbrowser.open_new(itunesLink)


