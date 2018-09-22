
# -*- coding: utf-8 -*-

from pyicloud import PyiCloudService
import geopy.distance
import webbrowser
import time

chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
url = 'https://www.youtube.com/watch?v=9AifNHo4hTk'
api = PyiCloudService('vipultanwr@gmail.com','Tanwar@1993')

s1 = 'Hello Vipul, Welcome home…'
s2 = 'Playing your favorite songs from youtube…'

while True:
	
	loc = api.iphone.location()
	Mac_Coordinates = (72.86594258879559,19.07454662319946)
	Phone_Coordinates = (loc['longitude'],loc['latitude'])
	webbrowser.get(chrome_path).open(url)
	loc = api.iphone.location()

	Mac_Coordinates = (72.86594258879559,19.07454662319946)
	Phone_Coordinates = (loc['longitude'],loc['latitude'])

	print geopy.distance.vincenty(Mac_Coordinates, Phone_Coordinates).m
	
	break
