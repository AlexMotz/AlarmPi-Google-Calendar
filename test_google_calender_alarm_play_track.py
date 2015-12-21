#These are the imports google said to include
import gdata.calendar.service
import gdata.service
import atom.service
import gdata.calendar
import gdata.calendar
import atom
import getopt
import sys
import string
import time

import xe #for the time comparator
from feed.date.rfc3339 import tf_from_timestamp #also for the comparator
from datetime import datetime #for the time on the rpi end
from apscheduler.scheduler import Scheduler #this will let us check the calender on a regular interval
import os, random #to play the mp3 later

#this is more stuff google told me to do, but essentially it handles the login credentials
calendar_service = gdata.calendar.service.CalendarService()
calendar_service.email = 'youremail@yourdomain' #your email
calendar_service.password = 'yourgcalpassword' #your password
calendar_service.source = 'Google-Calendar_Python_Sample-1.0'
calendar_service.ProgrammaticLogin()

def FullTextQuery(calendar_service, text_query='wake'):
	print 'Full text query for events on Primary Calendar: \'%s\'' % ( text_query,)
	query = gdata.calendar.service.CalendarEventQuery('default', 'private', 'full', text_query)
	feed = calendar_service.CalendarQuery(query)
	for i, an_event in enumerate(feed.entry):
		for a_when in an_event.when:
			print "---"
			print an_event.title.text ,"Number:",i,"Event Time:",time.strftime('%d-%m-%Y %H:%M',time.localtime(tf_from_timestamp(a_when.start_time))),"Current Time:",time.strftime('%d-%m-%Y %H:%M')

			if time.strftime('%d-%m-%Y %H:%M',time.localtime(tf_from_timestamp(a_when.start_time))) == time.strftime('%d-%m-%Y %H:%M'):
				print "Comparison: Pass"
				print "---"

				#songfile = random.choice(os.listdir("/home/pi/alarmclock/test_MP3s/")) #chooses the .mp3 file
				#print "File Selected:", songfile
				#command ="mpg321" + " " + "/home/pi/alarmclock/test_MP3s/" + "'"+songfile+"'"+ " -g 100" #plays the MP3 in it's entierty. As long as the song is longer than a minute then will only trigger once in the minute that start of the "wake" event

				print "Sounding The Alarm: ", time
				execfile("sound_the_alarm.py")

				print command
				os.system(command) #runs the bash command
			else:
				print "Comparison:Fail" #the "wake" event's start time != the system's current time

def callable_func():
	os.system("clear") #this is more for my benefit and is in no way necesarry
	print "------------start-----------"
	FullTextQuery(calendar_service)
	print "-------------end------------"

scheduler = Scheduler(standalone=True)
scheduler.add_interval_job(callable_func,seconds=5)
scheduler.start() #runs the program indefinatly on an interval of 5 seconds
