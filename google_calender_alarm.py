from datetime import datetime
import os, random, string, sys

from apscheduler.schedulers.blocking import BlockingScheduler
import gdata.calendar.service


# Configuration
ALARM_EVENT_NAME = 'wake'
MP3_FOLDER = '/Users/username/path/to/mp3/collection'
GOOGLE_EMAIL = 'username@gmail.com'
GOOGLE_PASSWORD = 'password'
FREQUENCY_CHECK = 5 # in seconds

calendar_service = gdata.calendar.service.CalendarService()
calendar_service.email = GOOGLE_EMAIL
calendar_service.password = GOOGLE_PASSWORD
calendar_service.ProgrammaticLogin()

def full_text_query(calendar_service, text_query):
    print 'Full text query for {} events on Primary Calendar:'.format(text_query)
    query = gdata.calendar.service.CalendarEventQuery('default', 'private', 'full', text_query)
    feed = calendar_service.CalendarQuery(query)
    today = datetime.today()
    for i, event in enumerate(feed.entry):
        for e in event.when:
            alarm = e.start_time[:-13]
            now = today.strftime('%Y-%m-%dT%H:%M')
            print "Number:", i, "Event Time:", alarm, "Current Time:", now

            if alarm == now:
                print "Comparison: Pass\n---"
                #song_file = random.choice(os.listdir(MP3_FOLDER))
                #print "File Selected: {}".format(song_file)
                #command = "mpg123 '{}/{}'".format(MP3_FOLDER, song_file)
                print "Sounding The Alarm: ", time
                command = execfile("sound_the_alarm.py")
                os.system(command)

            else:
                print "Comparison: Fail"

def callable_func():
    os.system("clear")
    print "------------start-----------"
    full_text_query(calendar_service, text_query=ALARM_EVENT_NAME)
    print "-------------end------------"

scheduler = BlockingScheduler()
scheduler.add_job(callable_func, 'interval', seconds=FREQUENCY_CHECK)
scheduler.start()
