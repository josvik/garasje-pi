#!/usr/bin/python

# Get state of garage-door from sensors. For example two magnetic switches, one at top position and one at bottom position.
# Displays the state through led indicators connected to gpio for red, yellow and green.
# Red: the garage-door is open.
# Yellow: the door is opening or closing.
# Green: Closed.

import RPi.GPIO as GPIO
import time
import logging

logging.basicConfig(filename='/var/log/garagedoorstate.log', format='%(asctime)s %(message)s', level=logging.INFO)

pin_top=15
pin_bottom=14
pin_red = 2
pin_yellow = 3
pin_green = 4

def door_top(channel):
  if GPIO.input(pin_top):
    logging.info('Garagedoor[top] closing...')
    yellow_light()
  else:
    logging.info('Garagedoor[top] opened!')
    red_light()

def door_bottom(channel):
  if GPIO.input(pin_bottom):
    logging.info('Garagedoor[bottom] opening...')
    yellow_light()
  else:
    logging.info('Garagedoor[bottom] closed!')
    green_light()

def all_lights_off():
  GPIO.output(pin_red, GPIO.LOW)
  GPIO.output(pin_yellow, GPIO.LOW)
  GPIO.output(pin_green, GPIO.LOW)

def red_light():
  all_lights_off()
  GPIO.output(pin_red, GPIO.HIGH)

def yellow_light():
  all_lights_off()
  GPIO.output(pin_yellow, GPIO.HIGH)

def green_light():
  all_lights_off()
  GPIO.output(pin_green, GPIO.HIGH)

try:
  logging.info('Configuring GPIO ports...')
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(pin_top, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(pin_bottom, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(pin_red, GPIO.OUT)
  GPIO.setup(pin_yellow, GPIO.OUT)
  GPIO.setup(pin_green, GPIO.OUT)
  all_lights_off()
  logging.info('GPIO ports configured.')
  logging.info('GPIO %i - sensor garageport top.', pin_top)
  logging.info('GPIO %i - sensor garageport bottom.', pin_bottom)
  logging.info('GPIO %i - red led ground.', pin_red)
  logging.info('GPIO %i - yellow led ground.', pin_yellow)
  logging.info('GPIO %i - green led ground.', pin_green)

  if not GPIO.input(pin_top):
    red_light()
  elif not GPIO.input(pin_bottom):
    green_light()

  while True:
    if not 'event1' in locals():
      event1 = GPIO.add_event_detect(pin_top, GPIO.BOTH, callback=door_top, bouncetime=300)
    elif not 'event2' in locals():
      event2 = GPIO.add_event_detect(pin_bottom, GPIO.BOTH, callback=door_bottom, bouncetime=300)
    else:
      time.sleep(1)

except KeyboardInterrupt:
  logging.info('KeyboardInterrupt. Exiting...')
  raise
except:
  logging.error('Unexpected error: &s', sys.exc_info()[0])
  raise
finally:
  logging.info('Exiting. GPIO cleanup')
  GPIO.cleanup() 
