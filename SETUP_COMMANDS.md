***I had some trouble getting everything working the first time around.
So I made a composite list of all the commands that I used.
This way it will be much easier for you to setup.***

**Section 1: Basic Setup**
***Make sure RaspberryPi is uptodate***
sudo apt-get update
sudo apt-get upgrade

sudo raspi-config
*Select the Internationalization Option, then set your timezone*

***Insure Python and the Setup Tools are installed***
sudo apt-get install python
sudo apt-get install python-setuptools

**Section 2: Installing packages and required libraries**
***Install mpg123 command line MP3 Player***
sudo apt-get install python-feedparser mpg123 festival

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

**Section 3: Download alarmclock code from repo**
***Download/GitClone Code from Repo***
git clone https://github.com/AlexMotz/AlarmPi-Google-Calendar
