import subprocess
from crontab import CronTab

users_cron = CronTab(user='pi')
iter = users_cron.find_command('sudo python /home/pi/alarmpi/sound_the_alarm.py')
#disable the alarm
for job in iter:
	if job.is_enabled():
		subprocess.call("sudo kill $(ps aux | grep sound_the_alarm.py | awk '{ print $2 }')", shell=True)
		subprocess.call("sudo kill $(ps aux | grep mpg | awk '{ print $2 }')", shell=True)
	else:
		job.enable(True)
		subprocess.call('sudo python sound_the_alarm.py', shell=True)
users_cron.write()
