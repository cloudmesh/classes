

# ESP8266 Other



## Linux

	$ pip install esptool 
	$ pip install pyserial 
	$ pip install adafruit-ampy 
	? install lua 
	? install picocom

## Miniterm

	$ python -m serial.tools.miniterm -h

<http://pyserial.readthedocs.io/en/latest/tools.html#module-serial.tools.miniterm>

## Picocom

	$ picocom /dev/tty.wchusbserial1410 -b115200 ./probe.py

## Ampy

	$ ampy -p /dev/tty.wchusbserial1410 -b115200 run test.py

[https://drive.google.com/file/d/0BwAgplGeEjGPTnB5UXJnMzRMemc/view>](https://drive.google.com/file/d/0BwAgplGeEjGPTnB5UXJnMzRMemc/view)

```
usage: esptool.py [-h] [--port PORT] [--baud BAUD]
                  {load_ram,dump_mem,read_mem,write_mem,write_flash,run,
                  image_info,make_image,elf2image,read_mac,chip_id,flash_id,
                  read_flash,verify_flash,erase_flash,version}
                  ...

esptool.py v1.3 - ESP8266 ROM Bootloader Utility

positional arguments:
  {load_ram,dump_mem,read_mem,write_mem,write_flash,run,image_info,
  make_image,elf2image,read_mac,chip_id,flash_id,read_flash,
  verify_flash,erase_flash,version}
                        Run esptool {command} -h for additional help
    load_ram            Download an image to RAM and execute
    dump_mem            Dump arbitrary memory to disk
    read_mem            Read arbitrary memory location
    write_mem           Read-modify-write to arbitrary memory location
    write_flash         Write a binary blob to flash
    run                 Run application code in flash
    image_info          Dump headers from an application image
    make_image          Create an application image from binary files
    elf2image           Create an application image from ELF file
    read_mac            Read MAC address from OTP ROM
    chip_id             Read Chip ID from OTP ROM
    flash_id            Read SPI flash manufacturer and device ID
    read_flash          Read SPI flash content
    verify_flash        Verify a binary blob against flash
    erase_flash         Perform Chip Erase on SPI flash
    version             Print esptool version

optional arguments:
  -h, --help            show this help message and exit
  --port PORT, -p PORT  Serial port device
  --baud BAUD, -b BAUD  Serial port baud rate used when flashing/reading
```  


## esptool


```
$ esptool.py -p /dev/tty.wchusbserial1440 chip_id
$ esptool.py -p /dev/tty.wchusbserial1440 read_mac
```
```
cfg.ssid=“DoitWiFi”; cfg.pwd=“12345678”
```
http://192.168.4.1/

	esptool –port /dev/tty.wchusbserial1460 write_flash 0x00000 doit_integer_car_512k_20150701.bin

	esptool –port /dev/tty.wchusbserial1460 write_flash 0x00000 doit_integer_webserver_512k_20150701.bin
	
	esptool –port /dev/tty.wchusbserial1460 erase_flash

	esptool v1.3 Connecting.... Running Cesanta flasher stub... Erasing
flash (this may take a while)... Erase took 10.6 seconds

[http://micropython.org/live/](http://micropython.org/live/)

## Micropython

Download image from

micropython.org

Flash

```
$ esptool.py –port /dev/tty.wchusbserial1410 write_flash –flash_size=detect 0 esp8266-20170108-v1.8.7.bin
```

reset the chip
start 

	$ picocom /dev/tty.wchusbserial1410 -b115200

terminal

	$ picocom /dev/tty.wchusbserial1410


Run Code

test.py:

	print('Count to 10:')
	for i in range(1,11):
   		print(i)

Running:

	ampy --port /serial/port run test.py

* /serial/port is the path or name of the serial port connected to the MicroPython board.

Copy a file to the board

	$ ampy --port /serial/port put test.py

Copy a Directory to the board

	$ ampy --port /serial/port put adafruit_driver

Copy a file or directory from the board

	$ ampy --port /serial/port get boot.py

| comand | execute                                |
|--------|----------------------------------------|
| mkdir  | ampy --port /serial/port mkdir foo     |
| ls     | ampy --port /serial/port ls            |
| rm     | ampy --port /serial/port rm test.py    |
| rmdir  | ampy --port /serial/port rmdir test    |



Boot see:

[https://learn.adafruit.com/micropython-basics-load-files-and-run-code/boot-scripts ](https://learn.adafruit.com/micropython-basics-load-files-and-run-code/boot-scripts )

## Lua

	> pin =1 
	> gpio.mode(pin, gpio.OUTPUT) 
	> gpio.write(pin, gpio.HIGH) 
	> gpio.write(pin, gpio.LOW) 	
	> gpio.write(pin, gpio.LOW)
	> gpio.write(pin, gpio.LOW) 
	> pin=2 
	> gpio.mode(pin, gpio.OUTPUT) 
	> gpio.write(pin, gpio.HIGH) 
	> gpio.write(pin, gpio.LOW)

## ampy

[https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy](https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy)

## Resources

### login


    picocom v2.2
    
    port is        : /dev/tty.wchusbserial1460
    flowcontrol    : none
    baudrate is    : 115200
    parity is      : none
    databits are   : 8
    stopbits are   : 1
    escape is      : C-a
    local echo is  : no
    noinit is      : no
    noreset is     : no
    nolock is      : no
    send_cmd is    : sz -vv
    receive_cmd is : rz -vv -E
    imap is        : lfcrlf,
    omap is        : 
    emap is        : crcrlf,delbs,
    
    
### Brew

* http://blog.coldflake.com/posts/Minimal-Development-Setup-for-Mac-OS/

	$ brew install tree
	$ brew install wget
	$ brew install picocom
	$ brew install htop-osx
	$ brew install dos2unix 
	$ brew install jq 
	$ brew install tig  # git ascii browser
	$ brew install sqlite
	$ brew cask install omnigraffle
	$ brew cask install virtualbox
	$ brew tap homebrew/science
	$ brew install opencv
	$ brew link opencv

* [opencv install via homebrew](https://books.google.com/books?id=zOx3CgAAQBAJ&pg=PA20&lpg=PA20&dq=useful+homebrew+packages+arduino&source=bl&ots=LifN_I7SJK&sig=6CW-ph8l05Jf4gqkP6NzK7uV9qc&hl=en&sa=X&ved=0ahUKEwjcifT-tYjUAhVI7YMKHdSKAXoQ6AEITjAH#v=onepage&q=useful%20homebrew%20packages%20arduino&f=false)


### esp8266 versions

* [top-6-esp8266-modules](https://www.losant.com/blog/top-6-esp8266-modules)

#### esp8266 Motorshield

* [micropython gpio](http://micropython.org/resources/docs/en/latest/esp8266/esp8266/tutorial/pins.html?highlight=gpio)
* [motorshield manual](https://cdn.hackaday.io/files/8856378895104/user-mannual-for-esp-12e-motor-shield.pdf)
* [doitcar lua program](https://smartarduino.gitbooks.io/user-manual-for-wifi-car-by-nodemcu-doitcar-/content/31_code_for_ap_case_on_doitcar.html)
* [esp8266-nodemcu-motor-shield-review](https://blog.squix.org/2015/09/esp8266-nodemcu-motor-shield-review.html)

Jumper

The motor shield has some jumpers. We need better information about them. Here some starting points.

*If you use two power sources, remove the jumper which connects VM and VIN.*

* [http://www.instructables.com/id/Motorize-IoT-With-ESP8266/](http://www.instructables.com/id/Motorize-IoT-With-ESP8266/)
* [Node MCU Motorshield](https://blog.the-jedi.co.uk/2015/11/26/nodemcu-motor-shield-review/)

### Projects


* [Google search on esp8266 projects](https://www.google.com/search?q=esp8266+projects&rlz=1C5CHFA_enUS727US727&oq=esp8266+&aqs=chrome.0.69i59l3j69i61j69i60l2.3594j0j4&sourceid=chrome&ie=UTF-8)
* [http://randomnerdtutorials.com/getting-started-with-esp8266-wifi-transceiver-review/](http://randomnerdtutorials.com/getting-started-with-esp8266-wifi-transceiver-review/)

### Grove

GroveKit

* [esp8266-grove-kit](https://cknodemcu.wordpress.com/2016/04/21/esp8266-grove-kit-arrived/)
* [Grovekit manual](http://bbs.smartarduino.com/attachment.php?aid=20)
* Grove kit has different plugs

Grove Base Shield

* [Seeedstudio-Grove-Base-Shield-NodeMCU Amazon](https://www.amazon.com/Seeedstudio-Grove-Base-Shield-NodeMCU/dp/B018FNOWFM/ref=pd_lpo_sbs_504_t_0?_encoding=UTF8&psc=1&refRID=PG5ZRRG08AYRA5XYNF5E)
* [Grove-Base-Shield-for-NodeMCU Seedstudio](https://www.seeedstudio.com/Grove-Base-Shield-for-NodeMCU-p-2513.html)

Wio

* [wio-node-grove-esp8266-wifi-module](https://www.digikey.com/en/maker/blogs/wio-node-grove-esp8266-wifi-module/57ad3656de7a4e8bb1ba5b2c82d4352f) (from digikey)
* [Wio Node](https://solarbotics.com/product/30314/) (from solarrobotics)
* [Wio Link](https://solarbotics.com/product/30316/)


### Power

* [Power](http://henrysbench.capnfatz.com/henrys-bench/arduino-projects-tips-and-more/powering-the-esp-12e-nodemcu-development-board/)
