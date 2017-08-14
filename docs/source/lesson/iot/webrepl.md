# Webrepl

	$ cms robot probe
	$ cms robot put boot.py

Reset

	$ cms robot put cloudmesh.py 
	$ cms robot login


>		ERROR: If you do not see a >>> please press the reset button.
>
>		NoneType: None
>
>		picocom v2.2
>
>		port is        : /dev/tty.wchusbserial130
>		flowcontrol    : none
>		baudrate is    : 115200
>		parity is      : none
>		databits are   : 8
>		stopbits are   : 1
>		escape is      : C-a
>		local echo is  : no
>		noinit is      : no
>		noreset is     : no
>		nolock is      : no
>		send_cmd is    : sz -vv
>		receive_cmd is : rz -vv -E
>		imap is        : lfcrlf,
>		omap is        : 
>		emap is        : crcrlf,delbs,
>
>		Type [C-a] [C-h] to see available commands
>
>		Terminal ready

.

	>>> import cm

>		starting network ...
>		connection ok
>		('10.0.1.102', '255.255.255.0', '10.0.1.1', '10.0.1.1')
>		IP:  10.0.1.102

>		WebREPL is not configured, run 'import webrepl_setup'

Login

	>>> import webrepl_setup

>		WebREPL daemon auto-start status: disabled
>
>		Would you like to (E)nable or (D)isable it running on boot?
>		(Empty line to quit)
>		> E
>		To enable WebREPL, you must set password for it
>		New password: BLA
>		Confirm password: BLA
>		Changes will be activated after reboot
>		Would you like to reboot now? (y/n) y

Lots of characters will appear

	could not open file 'main.py' for reading

	MicroPython v1.8.7-7-gb5a1a20a3 on 2017-01-09; ESP module with ESP8266
	Type "help()" for more information.

	>>> 

Next	
	
	>>> import cm

>		starting network ...
>		{'ssid': 'robis', 'password': 'BLA', 'username': 'u'}
>		connection ok
>		('10.0.1.102', '255.255.255.0', '10.0.1.1', '10.0.1.1')
>		IP:  10.0.1.102
	
.

	>>> cm.console()
	
>		WebREPL daemon started on ws://192.168.4.1:8266
>		WebREPL daemon started on ws://10.0.1.102:8266
>		Started webrepl in normal mode
>	
>		WebREPL connection from: ('10.0.1.2', 59432)


	>>> import os
	>>> os.listdir()
	
>		['credentials.txt', 'cloudmesh.py', 'boot.py', 'webrepl_cfg.py']

	>>>
	
In terminal		
	
	$ open webrepl.html

In webrepl connect to ws:/10.0.1.102:8266

Try this in the window and you will see the output

	cm.version
	
		0.1

## References

1. [https://learn.adafruit.com/micropython-basics-esp8266-webrepl/access-webrepl](https://learn.adafruit.com/micropython-basics-esp8266-webrepl/access-webrepl)
