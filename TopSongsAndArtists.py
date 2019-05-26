import tkinter
from tkinter import *
from tkinter.ttk import *
from functools import partial
from PIL import Image, ImageTk
from io import BytesIO
import requests
import spotify
import lastfm
import billb
import links
import math

def clickedSongs():
	top = tkinter.Toplevel()
	top.title("Top Songs")
	width, height = top.winfo_screenwidth(), top.winfo_screenheight()
	top.geometry('%dx%d+0+0' % (width,height))
	#top.iconbitmap("")

	label = tkinter.Label(top, text="Top Songs\n", font=("Arial Bold Italics", 50), fg="blue").place(x=width/2.55, y=0)

	dailyButton = tkinter.Button(top, text="Daily Rankings", font=("Arial Bold Italics", 40), bg="blue", fg="white", command=dailyRank).place(x=width/2.7, y=height/4)
	weeklyButton = tkinter.Button(top, text="Weekly Rankings", font=("Arial Bold Italics", 40), bg="blue", fg="white", command=weeklyRank).place(x=width/2.83, y=height/2.2)

	backButton = tkinter.Button(top, text="Go Back", font=("Arial Bold Italics", 40), bg="blue", fg="white", command=top.destroy).place(x=width/2.4, y=height/1.5)

#########################################################################################################

def clickedArtists():
	top = tkinter.Toplevel()
	top.title("Top Artists")
	width, height = top.winfo_screenwidth(), top.winfo_screenheight()
	top.geometry('%dx%d+0+0' % (width,height))
	#top.iconbitmap("")

	label = tkinter.Label(top, text="Top Artists\n", font=("Arial Bold Italics", 50), fg="blue").place(x=width/2.56, y=0)

	global combo
	combo = Combobox(top, font=("Arial Bold Italics", 30), width=2)
	combo['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
	combo.current(9)
	combo.place(x=width/2.15, y=height/8)

	lastfmButton = tkinter.Button(top, text="Last.fm Rankings", font=("Arial Bold Italics", 40), bg="blue", fg="white", command=partial(topArtists, 'L')).place(x=width/2.8, y=height/4.5)
	billboardButton = tkinter.Button(top, text="Billboard Rankings", font=("Arial Bold Italics", 40), bg="blue", fg="white", command=partial(topArtists, 'B')).place(x=width/2.87, y=height/2.75)
	bothButton = tkinter.Button(top, text="Both Rankings", font=("Arial Bold Italics", 40), bg="blue", fg="white", command=partial(topArtists, "LB")).place(x=width/2.7, y=height/2)

	backButton = tkinter.Button(top, text="Go Back", font=("Arial Bold Italics", 40), bg="blue", fg="white", command=top.destroy).place(x=width/2.39, y=height/1.5)

#########################################################################################################

def dailyRank():
	dailyWindow = tkinter.Toplevel()
	dailyWindow.title("Top Songs of the Day")
	width, height = dailyWindow.winfo_screenwidth(), dailyWindow.winfo_screenheight()
	dailyWindow.geometry('%dx%d+0+0' % (width,height))
	#top.iconbitmap("")

	label = tkinter.Label(dailyWindow, text="Top Songs of the Day\n", font=("Arial Bold Italics", 50), fg="blue").place(x=width/3.4, y=0)

	global combo
	combo = Combobox(dailyWindow, font=("Arial Bold Italics", 40), width=2)
	combo['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
	combo.current(9)
	combo.place(x=width/2.17, y=height/8)

	global daily_weekly
	daily_weekly = 'daily'

	spotifyButton = tkinter.Button(dailyWindow, text="Spotify Rankings", font=("Arial Bold Italics", 40), bg="blue", fg="white", command=partial(topSongs, "S")).place(x=width/2.81, y=height/4.5)
	lastfmButton = tkinter.Button(dailyWindow, text="Last.fm Rankings", font=("Arial Bold Italics", 40), bg="blue", fg="white", command=partial(topSongs, "L")).place(x=width/2.85, y=height/2.75)
	bothButton = tkinter.Button(dailyWindow, text="Both Rankings", font=("Arial Bold Italics", 40), bg="blue", fg="white", command=partial(topSongs, "SL")).place(x=width/2.7, y=height/2)

	backButton = tkinter.Button(dailyWindow, text="Go Back", font=("Arial Bold Italics", 40), bg="blue", fg="white", command=dailyWindow.destroy).place(x=width/2.4, y=height/1.5)

#########################################################################################################

def weeklyRank():
	weeklyWindow = tkinter.Toplevel()
	weeklyWindow.title("Top Songs of the Week")
	width, height = weeklyWindow.winfo_screenwidth(), weeklyWindow.winfo_screenheight()
	weeklyWindow.geometry('%dx%d+0+0' % (width,height))
	#top.iconbitmap("")

	label = tkinter.Label(weeklyWindow, text="Top Songs of the Week\n", font=("Arial Bold Italics", 50), fg="blue").place(x=width/3.55, y=0)

	global combo
	combo = Combobox(weeklyWindow, font=("Arial Bold Italics", 40), width=2)
	combo['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
	combo.current(9)
	combo.place(x=width/2.17, y=height/8)

	global daily_weekly
	daily_weekly = 'weekly'

	spotifyButton = tkinter.Button(weeklyWindow, text="Spotify Rankings", font=("Arial Bold Italics", 40), bg="blue", fg="white", command=partial(topSongs, "S")).place(x=width/2.81, y=height/4.5)
	billboardButton = tkinter.Button(weeklyWindow, text="Billboard Rankings", font=("Arial Bold Italics", 40), bg="blue", fg="white", command=partial(topSongs, "B")).place(x=width/2.93, y=height/2.75)
	bothButton = tkinter.Button(weeklyWindow, text="Both Rankings", font=("Arial Bold Italics", 40), bg="blue", fg="white", command=partial(topSongs, "SB")).place(x=width/2.7, y=height/2)

	backButton = tkinter.Button(weeklyWindow, text="Go Back", font=("Arial Bold Italics", 40), bg="blue", fg="white", command=weeklyWindow.destroy).place(x=width/2.4, y=height/1.5)

#########################################################################################################

def topSongs(option):
	songsWindow = tkinter.Toplevel()
	songsWindow.title("Songs Search Results")
	width, height = songsWindow.winfo_screenwidth(), songsWindow.winfo_screenheight()
	songsWindow.geometry('%dx%d+0+0' % (width,height))

	num = combo.current() + 1
	header2 = ""

	if(daily_weekly == 'daily'):
		if option == "S":
			results = spotify.spotify(num, 'daily')
			header = "Spotify"

		elif option == "L":
			results = lastfm.lastfm(num, 'songs')
			header = "Last.fm"

		elif option == "SL":
			results = spotify.spotify(num, 'daily')
			header = "Spotify"
			results2 = lastfm.lastfm(num, 'songs')
			header2 = "Last.fm"
	elif(daily_weekly == 'weekly'):
		if option == "S":
			results = spotify.spotify(num, 'weekly')
			header = "Spotify"
		elif option == "B":
			results = billb.billb(num, 'songs')
			header = "Billboard"
		elif option == "SB":
			results = spotify.spotify(num, 'weekly')
			header = "Spotify"
			results2 = billb.billb(num, "songs")
			header2 = "Billboard"

	label = tkinter.Label(songsWindow, text=header, font=("Arial Bold Italics", 40), fg="blue").place(x=0, y=0)

	songsList = [None] * (num+1)
	for i in range(num+1):
		songsList[i] = ""
	counter = 0
	check = False
	for row in repr(results):
		if(row != "\\" and row != "n" and row != "\""):
			songsList[counter] += row
		elif(row == "\\"):
			check = True
		elif(row == "n" and check == True):
			counter += 1
			check = False
		elif(row == "n" and check == False):
			songsList[counter] += row

	dic={}
	i=0
	for i in range(num):
		dic[i] = tkinter.Button(songsWindow, text=songsList[i], font=("Arial Bold Italics", 15), bg="blue", fg="white", command=partial(Links, songsList[i], "songs")).place(x=0, y=(height/15)*(i/1.6+1))

	if(option == "SL" or option == "SB"):

		label2 = tkinter.Label(songsWindow, text=header2, font=("Arial Bold Italics", 40), fg="blue").place(x=width/1.8, y=0)
		songsList2 = [None] * (num+1)
		for i in range(num+1):
			songsList2[i] = ""
		counter = 0
		check = False
		for row in repr(results2):
			if(row != "\\" and row != "n" and row != "\""):
				songsList2[counter] += row
			elif(row == "\\"):
				check = True
			elif(row == "n" and check == True):
				counter += 1
				check = False
			elif(row == "n" and check == False):
				songsList2[counter] += row

		dic={}
		i=0
		for i in range(num):
			dic[i] = tkinter.Button(songsWindow, text=songsList2[i], font=("Arial Bold Italics", 15), bg="blue", fg="white", command=partial(Links, songsList2[i], "songs")).place(x=width/1.8, y=(height/15)*(i/1.6+1))

	backButton = tkinter.Button(songsWindow, text="Go Back", font=("Arial Bold Italics", 40), bg="blue", fg="white", command=songsWindow.destroy).place(x=width/2.4, y=height/1.2)


#########################################################################################################

def topArtists(option):
	artistsWindow = tkinter.Toplevel()
	artistsWindow.title("Artists Search Results")
	width, height = artistsWindow.winfo_screenwidth(), artistsWindow.winfo_screenheight()
	artistsWindow.geometry('%dx%d+0+0' % (width,height))

	num = combo.current() + 1
	header2 = ""

	if(option == "L"):
		results = lastfm.lastfm(num, 'artists')
		header = "Last.fm"
	elif(option == "B"):
		results = billb.billb(num, 'artists')
		header = "Billboard"
	elif(option == "LB"):
		results = lastfm.lastfm(num, 'artists')
		header = "Last.fm"
		results2 = billb.billb(num, 'artists')
		header2 = "Billboard"

	label = tkinter.Label(artistsWindow, text=header, font=("Arial Bold Italics", 40), fg="blue").place(x=0, y=0)

	artistsList = [None] * (num+1)
	for i in range(num+1):
		artistsList[i] = ""
	counter = 0
	check = False
	for row in repr(results):
		if(row != "\\" and row != "n" and row != "\""):
			artistsList[counter] += row
		elif(row == "\\"):
			check = True
		elif(row == "n" and check == True):
			counter += 1
			check = False
		elif(row == "n" and check == False):
			artistsList[counter] += row

	dic={}
	i=0
	artistsList[0] = artistsList[0][1:]
	for i in range(num):
		dic[i] = tkinter.Button(artistsWindow, text=artistsList[i], font=("Arial Bold Italics", 15), bg="blue",fg="white", command=partial(Links, artistsList[i], "artists")).place(x=0, y=(height/15)*(i/1.6+1))

	if(option == "LB"):
		label2 = tkinter.Label(artistsWindow, text=header2, font=("Arial Bold Italics", 40), fg="blue").place(x=width/1.8, y=0)

		artistsList2 = [None] * (num+1)
		for i in range(num+1):
			artistsList2[i] = ""
		counter = 0
		check = False
		for row in repr(results2):
			if(row != "\\" and row != "n" and row != "\""):
				artistsList2[counter] += row
			elif(row == "\\"):
				check = True
			elif(row == "n" and check == True):
				counter += 1
				check = False
			elif(row == "n" and check == False):
				artistsList2[counter] += row

		dic={}
		i=0
		artistsList2[0] = artistsList2[0][1:]
		for i in range(num):
			dic[i] = tkinter.Button(artistsWindow, text=artistsList2[i], font=("Arial Bold Italics", 15), bg="blue",fg="white", command=partial(Links, artistsList2[i], "artists")).place(x=width/1.8, y=(height/15)*(i/1.6+1))

	backButton = tkinter.Button(artistsWindow, text="Go Back", font=("Arial Bold Italics", 40), bg="blue",fg="white", command=artistsWindow.destroy).place(x=width/2.4, y=height/1.2)

#########################################################################################################

def Links(name, s_a):
	LinksWindow = tkinter.Toplevel()
	LinksWindow.title("Links")
	width, height = LinksWindow.winfo_screenwidth(), LinksWindow.winfo_screenheight()
	LinksWindow.geometry('%dx%d+0+0' % (width,height))

	label = tkinter.Label(LinksWindow, text=name, font=("Arial Bold Italics", 40), fg="blue").pack()

	'''response = requests.get("https://www.last.fm/static/images/lastfm_avatar_twitter.66cd2c48ce03.png")
	image = Image.open(BytesIO(response.content)).resize((300,300), Image.ANTIALIAS)
	photo = ImageTk.PhotoImage(image)

	response2 = requests.get("https://www.sketchappsources.com/resources/source-image/youtube-logo.png")
	image2 = Image.open(BytesIO(response2.content)).resize((300,300), Image.ANTIALIAS)
	photo2 = ImageTk.PhotoImage(image2)

	response3 = requests.get("https://ih0.redbubble.net/image.451904145.7578/pp,550x550.u2.jpg")
	image3 = Image.open(BytesIO(response3.content)).resize((300,300), Image.ANTIALIAS)
	photo3 = ImageTk.PhotoImage(image3)

	response4 = requests.get("http://chittagongit.com/images/itunes-icon-flat/itunes-icon-flat-0.jpg")
	image4 = Image.open(BytesIO(response4.content)).resize((300,300), Image.ANTIALIAS)
	photo4 = ImageTk.PhotoImage(image4)'''

	image = Image.open("lastfm.png").resize((300,300), Image.ANTIALIAS)
	photo = ImageTk.PhotoImage(image)

	image2 = Image.open("youtube.jpg").resize((300,300), Image.ANTIALIAS)
	photo2 = ImageTk.PhotoImage(image2)

	image3 = Image.open("spotify.jpg").resize((300,300), Image.ANTIALIAS)
	photo3 = ImageTk.PhotoImage(image3)

	image4 = Image.open("itunes.png").resize((300,300), Image.ANTIALIAS)
	photo4 = ImageTk.PhotoImage(image4)

	if(s_a == "songs"):
		l = tkinter.Button(LinksWindow, image=photo, command=partial(links.getLastfmLink, name, 'songs', False)).place(x=0, y=height/3)
		l2 = tkinter.Button(LinksWindow, image=photo2, command=partial(links.getYoutubeLink, name, 'songs')).place(x=width/4, y=height/3)
		l3 = tkinter.Button(LinksWindow, image=photo3, command=partial(links.getSpotifyLink, name, 'songs')).place(x=width/1.805, y=height/3)
		l4 = tkinter.Button(LinksWindow, image=photo4, command=partial(links.getItunesLink, name, 'songs', False)).place(x=width/1.243, y=height/3)
		previewButton = tkinter.Button(LinksWindow, text="Preview Song", font=("Arial Bold Italics", 30), bg="blue",fg="white", command=partial(links.getItunesLink, name, 'songs', True)).place(x=width/2.47, y=height/8)
		label = tkinter.Label(LinksWindow, text="provided courtesy of iTunes", font=("Arial Bold Italics", 10), fg="blue").place(x=width/2.3, y=height/5)

	elif(s_a == "artists"):
		l = tkinter.Button(LinksWindow, image=photo, command=partial(links.getLastfmLink, name, 'artists', False)).place(x=0, y=height/3)
		l2 = tkinter.Button(LinksWindow, image=photo2, command=partial(links.getYoutubeLink, name, 'artists')).place(x=width/4, y=height/3)
		l3 = tkinter.Button(LinksWindow, image=photo3, command=partial(links.getSpotifyLink, name, 'artists')).place(x=width/1.805, y=height/3)
		l4 = tkinter.Button(LinksWindow, image=photo4, command=partial(links.getItunesLink, name, 'artists', False)).place(x=width/1.243, y=height/3)

	ref = l #reference so the image wont get deleted
	ref2 = l2
	ref3 = l3
	backButton = tkinter.Button(LinksWindow, text="Go Back", font=("Arial Bold Italics", 40), bg="blue",fg="white", command=LinksWindow.destroy).place(x=width/2.4, y=height/1.2)
	l4.image = photo4

#########################################################################################################

window = tkinter.Tk()

window.title("Song and Artist Popularity")
width, height = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry('%dx%d+0+0' % (width,height))
#window.iconbitmap("")

scrollbar = Scrollbar(window)
#scrollbar.pack(side='right',fill='y')

label = tkinter.Label(window, text="Top\nSongs and Artists", font=("Arial Bold Italics", 50), fg="blue").place(x=width/3, y=0)

songsButton = tkinter.Button(window, text="Top Songs", font=("Arial Bold Italics", 40), bg="blue",fg="white", command=clickedSongs).place(x=width/2.45, y=height/4)

artistsButton = tkinter.Button(window, text="Top Artists", font=("Arial Bold Italics", 40), bg="blue",fg="white", command=clickedArtists).place(x=width/2.47, y=height/2.2)

#txt = tkinter.Entry(window, width=12).pack()

quitButton = tkinter.Button(window, text="Quit", font=("Arial Bold Italics", 40), bg="blue",fg="white", command=window.destroy).place(x=width/2.22, y=height/1.5)

window.mainloop()
#########################################################################################################
