Welcome to the Alarm Pi Google Calender scheduler code.

It's (will be) "A Spoken Weather And News Clock" for your Raspberry Pi via an event in you google calender called "wake"

Please feel free to take it, and do what you will with it.

If you just simply want your alarm clock to go off at a specified time
using a cron job you will need everything below but stop before the crontab command.
*required packages:

  sudo apt-get install python-feedparser mpg123 festival

** YOU MUST USE RAMFS to avoid wear on your card and to enable Google Voice.

  sudo mkdir -p /mnt/ram

  echo "ramfs       /mnt/ram ramfs   nodev,nosuid,noexec,nodiratime,size=64M   0 0" | sudo tee -a /etc/fstab

*** and finally to set your alarm for 733AM Mon-Fri

  crontab -e 33 7 * * 1-5 sudo python /home/pi/sound_the_alarm.pi

  ****************************************************************

  I wanted a way to re-purpose a service I use everyday (that way I wouldn’t have to modify my workflow) as an Alarm Clock. I landed on Google Calender because I can add events from pretty much every device I interact with on a daily basis, and upon searching found out that developing using the python API wasn’t that hard at all.

  To kick things off, you’ll need to download and install the Google Data Library.
      https://developers.google.com/gdata/articles/python_client_lib#linux

  I’ll be using this version: https://gdata-python-client.googlecode.com/files/gdata-2.0.17.tar.gz

   Unzip the .tar.gz and from the top top level directory it creates, install the setup.py file. Then run the tests/run_data_tests.py to see if it all works. Mine does fine but it if yours doesn’t, go through Google Data Library guide written by google (link above) to get yourself up and running.

  The brunt of this program comes down to a single boolean statement, but first we have to set that up. The API produces an rfc3339 time, and that’s a lot of irrelevant information for this application.

  To convert the time I’m using something found on stackoverflow.

  http://stackoverflow.com/questions/1941927/convert-an-rfc-3339-time-to-a-standard-python-timestamp
  http://home.blarg.net/~steveha/pyfeed.html
