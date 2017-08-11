# Raspberry PI 3


## Raspbery PI for IOT (Gregor)

## Hardware

see hardware page we have

## Instalation (Jon)

Describe how to install the two different os and list advantages,
disadvantages ov approach

### Instalation of Dexter (Jon)

### Instalation with NOOBS (Jon)

Prepare SD CARD

1. Download Noobs https://www.raspberrypi.org/downloads/noobs/ Takes >26 min
2. Format SD card with Disk Utility
   https://www.raspberrypi.org/learning/noobs-install/elcapitan/ MS-DOS (FAT) 
3. Copy Files, Drag all files from the NOOBS folder onto the sd card

##Configure

### Prepare OS

## Update

	sudo apt-get upgrade
	sudo apt-get update
	sudo apt-get install emacs

	curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
	
add to ~/.bash_profile	
	
	export PATH="/home/pi/.pyenv/bin:$PATH"
	eval "$(pyenv init -)"
	eval "$(pyenv virtualenv-init -)"

source 

### Update to Python 3.6.1

see how we do this in osx/linux can this be done on raspbery?
if not document update from source with altinstall

### Install scientific Libraries

check if they are already installed

* numpy
* matplotlib
* scipy
* scikitlearn

### cloudmesh.pi (Jon)

two ways to install pi and source

### Install VNC

describe how to install and configure VNC


## Sensors (Jon)

### Grove Sensors (Jon)

we already have draft

### Non Grove Sensors (Jon)

Elegoo as example




## Notes To integrates


### Connecting

Hostnames:

* raspberrypi.local 
* raspberrypi.

change

recovery.cmdline

forgot what these were:

	runinstaller quiet ramdisk_size=32768 root=/dev/ram0 init=/init vt.cur_default=1 elevator=deadline
	silentinstall runinstaller quiet ramdisk_size=32768 root=/dev/ram0 init=/init vt.cur_default=1 elevator=deadline
	

Connect the cable
	
You will see the activity LEDs flash while the OS installs.  Depending on your SD-Card this can take up to 40-60 minutes.



## VLC on OSX

* [http://www.videolan.org/vlc/index.en_GB.html](http://www.videolan.org/vlc/index.en_GB.html)
* [http://get.videolan.org/vlc/2.2.6/macosx/vlc-2.2.6.dmg](http://get.videolan.org/vlc/2.2.6/macosx/vlc-2.2.6.dmg)
* [http://www.mybigideas.co.uk/RPi/RPiCamera/](http://www.mybigideas.co.uk/RPi/RPiCamera/)
* 
## Camera on Pi

	sudo apt-get install vlc
	
* [https://www.raspberrypi.org/learning/getting-started-with-picamera/worksheet/](https://www.raspberrypi.org/learning/getting-started-with-picamera/worksheet/)
* [https://www.hackster.io/bestd25/pi-car-016e66](https://www.hackster.io/bestd25/pi-car-016e66)

## Streaming video

* [https://blog.miguelgrinberg.com/post/stream-video-from-the-raspberry-pi-camera-to-web-browsers-even-on-ios-and-android](https://blog.miguelgrinberg.com/post/stream-video-from-the-raspberry-pi-camera-to-web-browsers-even-on-ios-and-android)

## Linux Commandline

* [http://www.computerworld.com/article/2598082/linux/linux-linux-command-line-cheat-sheet.html](http://www.computerworld.com/article/2598082/linux/linux-linux-command-line-cheat-sheet.html)


## Enable SPI

go to the configuration interfaces and enable
   
## RTIMUlib2

  git clone https://github.com/RTIMULib/RTIMULib2.git
  cd RTIMULib

Add the following two lines to /etc/modules

	i2c-bcm2708
	i2c-dev

reboot

	ls /dev/i2c-*
	sudo apt-get install i2c-tools

	sudo i2cdetect -y 1
     	     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
	00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
	10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
	20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
	30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
	40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
	50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
	60: -- -- -- -- -- -- -- -- 68 -- -- -- -- -- -- -- 
	70: -- -- -- -- -- -- -- --

![Pinout](images/rasp3.png)

create a file /etc/udev/rules.d/90-i2c.rules and add the line:

    KERNEL=="i2c-[0-7]",MODE="0666"

note: does not work

instead we do

    sudo chmod 666 /dev/i2c-1 


Set the I2C bus speed to 400KHz by adding to /boot/config.txt:

    dtparam=i2c1_baudrate=400000

reboot. In terminal change directories to

	cd /home/pi/github/RTIMULib2/RTIMULib/IMUDrivers
	
and open

	emacs RTIMUDefs.h

In RTIMUDefs.h change

    #define MPU9250_ID 0x71

To

    #define MPU9250_ID 0x73



	cd /home/pi/github/RTIMULib2/RTIMULib

In terminal

	mkdir build
	cd build
	cmake ..
	make -j4
	sudo make install
	sudo ldconfig

## Compile RTIMULib Apps

	cd /home/pi/github/RTIMULib2/Linux/RTIMULibCal
	make clean; make -j4
   	sudo make install
   	cd /home/pi/github/RTIMULib2/Linux/RTIMULibDrive
   	make clean; make -j4
   	sudo make install
   	cd /home/pi/github/RTIMULib2/Linux/RTIMULibDrive10
   	make clean; make -j4
   	sudo make install
   	cd /home/pi/github/RTIMULib2/Linux/RTIMULibDrive11
   	make clean; make -j4
   	sudo make install


   	cd /home/pi/github/RTIMULib2/Linux/RTIMULibDemo    
   	qmake clean
   	make clean
   	qmake
   	make -j4
   	sudo make install
   	cd /home/pi/github/RTIMULib2/Linux/RTIMULibDemoGL
   	qmake clean
   	make clean
   	qmake
   	make -j4
   	sudo make install



## Camera

* [Camera Tutorial](https://www.raspberrypi.org/learning/getting-started-with-picamera/worksheet/)  

.

	sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
	sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev

	sudo apt-get install libxvidcore-dev libx264-dev

	sudo pip install virtualenv virtualenvwrapper
	sudo rm -rf ~/.cache/pip

copy into ~/.profile:

     echo -e "\n# virtualenv and virtualenvwrapper" >> ~/.profile
     echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.profile
     echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.profile

source ~/.profile

	mkvirtualenv cv -p python3

workon cv

comandline has (cv) in front


	pip install numpy

	wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.1.0.zip
	wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.1.0.zip
	unzip opencv.zip
	unzip opencv_contrib.zip

## Lessons and Projects

* [Gui](https://www.raspberrypi.org/learning/getting-started-with-guis/worksheet/)  
* [Solder](https://www.raspberrypi.org/learning/getting-started-with-guis/)  
* [PI Camera Line Follower](https://www.raspberrypi.org/blog/an-image-processing-robot-for-robocup-junior/)  
* [Pi car flask](https://circuitdigest.com/microcontroller-projects/web-controlled-raspberry-pi-surveillance-robot)

