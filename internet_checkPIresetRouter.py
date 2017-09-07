#!/usr/bin/python
import socket
import RPi.GPIO as GPIO
import time
import syslog

PIN = 12
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

def ResetRouter():
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(PIN, GPIO.OUT)
  GPIO.output(PIN,1)       # turn on pin
  syslog.syslog('Modem Reset')
  time.sleep( 5 )         # sleep for 5
  GPIO.output(PIN,0)       # turn off pin
  GPIO.cleanup()          # cleanup

def main():
  if not (is_connected("www.google.ca") and is_connected("www.cnn.com")):
    ResetRouter()
  else:
    syslog.syslog('Internet Up')

if __name__ == "__main__":
  main()
