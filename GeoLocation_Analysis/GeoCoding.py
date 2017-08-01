# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 14:36:48 2016

@author: nsuri
"""

# geopy coding
from geopy.geocoders import Nominatim

geolocator = Nominatim()
location = geolocator.geocode("175 5th Avenue NYC")
#location = geolocator.geocode("1023 Muller Pkwy Bloomington Monroe 53 IN Indiana 47403 United States USA")
#print(location.address)
#print(location.latitude, location.longitude)

# https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyA28fBMyP8-mU28v-0ODxM5GclWd74F3hw

#https://maps.googleapis.com/maps/api/geocode/json?address=1023+Muller+Pkwy,+Bloomington,+ IN ,+Indiana,+ 47403,+ United States,+ USA&key=AIzaSyA28fBMyP8-mU28v-0ODxM5GclWd74F3hw

#1023+Muller+Pkwy,+Bloomington,+ IN ,+Indiana,+ 47403,+ United States,+ USA

import geocoder
#g = geocoder.google('1023+Muller+Pkwy,+Bloomington,+ IN ,+Indiana,+ 47403,+ United States,+ USA')
#g = geocoder.google('1023,,Muller,Pkwy,,,,,Bloomington,Monroe,53,IN,Indiana,47403,United,States,USA')
g = geocoder.google("1263,Deerfield,Pkwy,Apt,103,,,,,,,Buffalo,Grove,Lake,,,IL,Illinois,USA,United,States")
print g.latlng
print g.lat
print g.lng
print g.address
print g.country_long