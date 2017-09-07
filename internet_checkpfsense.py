#!/usr/bin/python
#
# Python script to check for live internet based on a cron schedule
# If no connection to both servers, then toggle GPIO pin to power cycle
# both router and modem
#
# GPIO pin is held low for active, HI to toggle power off and on
#  http://www.digital-loggers.com/iot.html for logic switch
#  wired to use the NC contacts
#
# M. Walker va3mw 09/16/2016


import socket 
import time 
import syslog 
import os

def is_connected(REMOTE_SERVER):
	try:
		# see if we can resolve the host name -- tells us if there is a DNS listening
		host = socket.gethostbyname(REMOTE_SERVER)
		# connect to the host -- tells us if the host is actually reachable
		s = socket.create_connection((host, 80), 2)
		# syslog.syslog('Successful Test')
		return True
	except:
		pass
	return False 

def reboot():
	os.system("shutdown /r") 

def main():
	if not (is_connected("www.google.ca") and is_connected("www.cnn.com")):
		reboot()
	else:
		syslog.syslog('Internet Up') 
if __name__ == "__main__":
	main()
