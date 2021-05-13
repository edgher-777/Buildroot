from gpiozero import Button
import time
import datetime
import logging
import os
import csv

def reed(ReedOutputToMain, ReedControl):
    reed = Button(24, pull_up=True, bounce_time=3)
    reedLamp = LED(23)
    reedErrorCode = "E-47"
    reedError = {}
    reedData = {}
    reedLamp.off()
    
    logger = logging.getLogger("REED")
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    logger.debug("Starting Tray Scanning")

    def present():
      reed.Lamp.off()
      logger.debug("Tray in place!")
      reedData["event"] = "Tray in place!"
      ReedOutputToMain.put(reedData)
      state = "OK"

    def notPresent():
      reed.Lamp.on()
      logger.debug("Tray not in place!")
      reedError["event"] = "error"
      reedError["timestamp"] = int(datetime.datetime.utcnow().timestamp())
      reedError["errorCode"] = reedErrorCode
      reedError["errorDesc"] = "Heat Amps (Current Draw Too Low)"
      reedError["errorValue"] = "TC5 = 250F"
      logger.error(buttonsError["errorDesc"])
      ReedOutputToMain.put(reedError)

    while state != "EXIT":
      reed.when_pressed = present
      reed.when_released = notPresent

    logger.debug("Exiting the Reed Thread")
