import sys
import json
import requests
from bs4 import BeautifulSoup

def spotify(num, d_w):

	if(d_w == 'daily'):
		dailySpotify = requests.get('https://spotifycharts.com/regional')
		dS = BeautifulSoup(dailySpotify.text, 'html.parser')
		dSSongs = dS.find_all('strong')
		dStopS = dSSongs[0:int(num)]
		dSArtists = dS.find_all('span')
		dStopA = dSArtists[1:int(num)+1]

		for i, row in enumerate(dStopS):
			song = str(row)
			song = song.replace("<strong>", "")
			song = song.replace("</strong>", "")
			song = song.replace("&amp;", "&")
			dStopS[i] = song

		for i, row in enumerate(dStopA):
			artist = str(row)
			artist = artist.replace("<span>", "")
			artist = artist.replace("</span>", "")
			artist = artist.replace("by", "--")
			artist = artist.replace("&amp;", "&")
			dStopA[i] = artist

		output = ""
		for i in range(len(dStopS)):
			output += str(i+1) + " - " + dStopS[i] + " " + dStopA[i] + "\n"
			print(str(i+1) + " - " + dStopS[i] + " " + dStopA[i])

	elif(d_w == 'weekly'):
		weeklySpotify = requests.get('https://spotifycharts.com/regional/global/weekly/latest')
		wS = BeautifulSoup(weeklySpotify.text, 'html.parser')
		wSresults = wS.find_all('td', attrs={'class':'chart-table-track'})
		wSSongs = wS.find_all('strong')
		wStopS = wSSongs[0:int(num)]
		wSArtists = wS.find_all('span')
		wStopA = wSArtists[1:int(num)+1]

		for i, row in enumerate(wStopS):
			song = str(row)
			song = song.replace("<strong>", "")
			song = song.replace("</strong>", "")
			song = song.replace("&amp;", "&")
			wStopS[i] = song

		for i, row in enumerate(wStopA):
			artist = str(row)
			artist = artist.replace("<span>", "")
			artist = artist.replace("</span>", "")
			artist = artist.replace("by", "--")
			artist = artist.replace("&amp;", "&")
			wStopA[i] = artist

		output = ""
		for i in range(len(wStopS)):
			output += str(i+1) + " - " + wStopS[i] + " " + wStopA[i] + "\n"
			print(str(i+1) + " - " + wStopS[i] + " " + wStopA[i])

	sys.stdout.flush()
	return output


