**Welcome to the Alarm Pi Google calendar scheduler code.**

It's (will be) "A Spoken Weather And News Clock" for your Raspberry Pi via an event in you google calendar called "wake"

Please feel free to take it, and do what you will with it.

If you just simply want your alarm clock to go off at a specified time
using a cron job you will need everything below but stop before the crontab command.

  *required packages:*

    sudo apt-get install python-feedparser mpg123 festival

  **YOU MUST USE RAMFS to avoid wear on your card and to enable Google Voice.**

    sudo mkdir -p /mnt/ram
    echo "ramfs /mnt/ram ramfs nodev,nosuid,noexec,nodiratime,size=64M 0 0" | sudo tee -a /etc/fstab

  **and finally to set your alarm for 733AM Mon-Fri**

    crontab -e 33 7 * * 1-5 sudo python /home/pi/sound_the_alarm.pi

  ****************************************************************

I wanted a way to re-purpose a service I use everyday (that way I wouldn’t have to modify my workflow) as an Alarm Clock. I landed on Google calendar because I can add events from pretty much every device I interact with on a daily basis, and upon searching found out that developing using the python API wasn’t that hard at all.

  *To kick things off, you’ll need to download and install the Google Data Library.*
      https://developers.google.com/gdata/articles/python_client_lib#linux

    I’ll be using this version: https://gdata-python-client.googlecode.com/files/gdata-2.0.17.tar.gz

   Unzip the .tar.gz and from the top top level directory it creates, install the setup.py file. Then run the tests/run_data_tests.py to see if it all works. Mine does fine but it if yours doesn’t, go through Google Data Library guide written by google (link above) to get yourself up and running.

   The brunt of this program comes down to a single boolean statement, but first we have to set that up. The API produces an rfc3339 time, and that’s a lot of irrelevant information for this application.

  *To convert the time I’m using something found on stackoverflow.*

    http://stackoverflow.com/questions/1941927/convert-an-rfc-3339-time-to-a-standard-python-timestamp
    http://home.blarg.net/~steveha/pyfeed.html

****************************************************************
****************************************************************
****************************************************************

**COMMANDS I USED**

I had some trouble getting everything working the first time around. So I made a composite list of all the commands that I used. This way it will be much easier for you to setup.

*** If you wish to use Ivona voice from Amazon you must get a beta test account at:

https://www.ivona.com/us/account/speechcloud/creation/

1. Open an account
2. Generate credentials
3. Put accesskey and secretkey in config file
  ****************************************************************
**Section 1: Basic Setup**

  ***Make sure RaspberryPi is uptodate***

    sudo apt-get update
    sudo apt-get upgrade

    sudo raspi-config
    *Select the Internationalization Option, then set your timezone*

  ***Insure Python and the Setup Tools are installed***

      sudo apt-get install python
      sudo apt-get install python-setuptools

  ****************************************************************
  **Section 2: Installing packages and required libraries**

  ***Install mpg123 command line MP3 Player***

    sudo apt-get install python-feedparser mpg123 festival pyvona

  ***Allow writing to Ram for Voice Announcements, etc...***
  *If we don't do this we will eventually SD card will fail due to reading/writing all the time*

    sudo mkdir -p /mnt/ram echo "ramfs /mnt/ram ramfs nodev,nosuid,noexec,nodiratime,size=64M 0 0" | sudo tee -a /etc/fstab

  ***Install the Google Data Library***

    wget https://gdata-python-client.googlecode.com/files/gdata-2.0.18.tar.gz
    tar zxvf gdata-2.0.18.tar.gz
    cd gdata-2.0.18/
    sudo python setup.py install

  *Check if gdata-python-client is setup correctly*

    ./tests/run_data_tests.py
    cd ..

  ***Install PyFeed***

    wget http://www.blarg.net/~steveha/pyfeed-0.7.4.tar.gz
    tar zxvf pyfeed-0.7.4
    cd pyfeed-0.7.4/
    sudo python setup.py install
    cd ..

  ***Install XE***

    wget http://www.blarg.net/~steveha/xe-0.7.4.tar.gz
    tar zxvf xe-0.7.4.tar.gz
    cd xe-0.7.4/
    sudo python setup.py install
    cd ..

  ***Install APScheduler 3.0.5***

    wget https://pypi.python.org/packages/source/A/APScheduler/APScheduler-3.0.5.tar.gz
    tar zxvf APScheduler-3.0.5.tar.gz
    cd APScheduler-3.0.5.tar.gz
    sudo python setup.py install
    cd ..

  ***Install Pyvona***

    wget https://pypi.python.org/packages/source/p/pyvona/pyvona-0.25.tar.gz
    tar zxvf pyvona-0.25.tar.gz
    cd pyvona-0.25.tar.gz
    sudo python setup.py install
    cd ..
  ****************************************************************
**Section 3: Download alarm clock code from repo**

  ***Download/GitClone Code from Repo***

    git clone https://github.com/AlexMotz/AlarmPi-Google-Calendar
