#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import json
import decimal
import ConfigParser
import time

Config=ConfigParser.ConfigParser()
try:
    Config.read('alarm.config')
except:
    raise Exception('Sorry, Failed reading alarm.config file.')

location = Config.get('weather_yahoo','location')

if Config.get('weather_yahoo','metric') == str(1):
    metric = '%20and%20u%3D\'c\''
else:
    metric = ''

try:
    weather_api = urllib.urlopen("https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%3D" + location + metric + "&format=json")
    response = weather_api.read()
    response_dictionary = json.loads(response)

    current = response_dictionary['query']['results']['channel']['item']['condition']['temp']
    current_low = response_dictionary['query']['results']['channel']['item']['forecast'][0]['low']
    current_high = response_dictionary['query']['results']['channel']['item']['forecast'][0]['high']
    conditions = response_dictionary['query']['results']['channel']['item']['condition']['text']
    forecast_conditions = response_dictionary['query']['results']['channel']['item']['forecast'][0]['text']
    wind = response_dictionary['query']['results']['channel']['wind']['speed']
    wind_chill = response_dictionary['query']['results']['channel']['wind']['chill']
    sunrise = response_dictionary['query']['results']['channel']['astronomy']['sunrise']
    sunset = response_dictionary['query']['results']['channel']['astronomy']['sunset']



    if wind != '':
      print response_dictionary ['query']['results']['channel']['wind']['speed']
      wind = round(float(wind),1)

#    print current
#    print current_low
#    print current_high
#    print conditions
#    print wind


    if conditions != forecast_conditions:
        conditions = conditions + ' becoming ' + forecast_conditions 
    weather_yahoo = 'Weather for today is ' + str(conditions) + ' currently ' + str(current) + ' degrees with a low of ' + str(current_low) + ' and a high of ' + str(current_high) + '.  '

# Wind uses the Beaufort scale
    if Config.get('weather_yahoo','metric') == str(1) and Config.get('weather_yahoo','wind') == str(1):
        if wind < 1:
            gust = 'It is calm'
        if wind > 1:
            gust = 'With Light Air'
        if wind > 5:
            gust = 'With a light breeze'
        if wind > 12:
            gust = 'With a gentle breeze'
        if wind > 20:
            gust = 'With a moderate breeze'
        if wind > 29:
            gust = 'With a fresh breeze'
        if wind > 39:
            gust = 'With a strong breeze'
        if wind > 50:
            gust = 'With High winds at ' + wind + 'kilometres per hour'
        if wind > 62:
            gust = 'With Gale force winds at ' + wind + 'kilometres per hour'
        if wind > 75:
            gust = 'With a strong gale at ' + wind + 'kilometres per hour'
        if wind > 89:
            gust = 'With Storm winds at ' + wind + 'kilometres per hour'
        if wind > 103:
            gust = 'With Violent storm winds at ' + wind + 'kilometres per hour'
        if wind > 118:
            gust = 'With Hurricane force winds at ' + wind + 'kilometres per hour'
        if wind == '':
            gust = ''
        weather_yahoo = weather_yahoo + str(gust) + '.  '

    if Config.get('weather_yahoo','wind_chill') == str(1) and wind > 5 and int(time.strftime("%m")) < 4 or wind > 5 and int(time.strftime("%m")) > 10:
        weather_yahoo = weather_yahoo + ' And a windchill of ' + str(wind_chill) + '.  '

except Exception:
    weather_yahoo = 'Failed to connect to Yahoo Weather.  '

if Config.get('main','debug') == str(1):
  print weather_yahoo
