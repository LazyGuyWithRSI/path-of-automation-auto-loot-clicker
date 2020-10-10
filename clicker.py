# written by LazyGuyWithRSI

import pyautogui
import ctypes
import time
from PIL import ImageGrab
import numpy as np
import cv2 as cv
import win32api
import keyboard
from configparser import ConfigParser

# TODO HOTKEY not implemented yet
# change HOTKEY to whatever key you want (ex. 'a', 'f2') even modifiers (ex. 'ctrl+d')
HOTKEY = 'space' #default: 'space'

# change LOOT_COLOR to whatever color the loot you want to pick up is (R, G, B)
LOOT_COLOR = (255, 0, 239) #default: (255, 0, 239)

COLOR_DEVIATION = 10

searchScaleWidth = 0.8
searchScaleHeight = 0.8
searchOffset = 0.02

offsetX = 1050
offsetY = 540

searchWidth = 1000
searchHeight = 850

keyDown = False
keyState = 0

def init(): # global gross, but I am writing this at 11pm so I'll fix it later
   global offsetX, offsetY, searchWidth, searchHeight, searchScaleWidth, searchScaleHeight, HOTKEY, LOOT_COLOR

   res = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
   searchWidth = res[0] * searchScaleWidth
   searchHeight = res[1] * searchScaleHeight
   offsetX = (res[0] / 2) - (searchWidth / 2)
   offsetY = (res[1] / 2) - (searchHeight / 2) - (res[1] * searchOffset)

   # load values from config.ini if there are any
   parser = ConfigParser()
   parser.read("config.ini")
   if (parser.has_option('config', 'hotkey')):
      HOTKEY = parser.get('config', 'hotkey')
      print("loading HOTKEY=" + str(HOTKEY) + " from config.ini")
   if (parser.has_option('config', 'loot_color')):
      LOOT_COLOR = eval(parser.get('config', 'loot_color'))
      print("loading LOOT_COLOR=" + str(LOOT_COLOR)+ " from config.ini")
   print("-- init finished --\n\n")


def leftClick(sleep=0.005):
   ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
   time.sleep(sleep)
   ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up
   time.sleep(sleep)

def extrapolate(xVals, yVals, lagCompensation = 1.0):
   if len(xVals) < 2 or len(yVals) < 2:
      return (0, 0)

   slope = (xVals[1] - xVals[0]) * lagCompensation, (yVals[1] - yVals[0]) * lagCompensation
   return slope

def grabLoot():

   cXList = []
   cYList = []
   for i in range(2):
      ### detect the loot ###
      img = np.array(ImageGrab.grab(bbox=(offsetX, offsetY, offsetX + searchWidth, offsetY + searchHeight)))

      scale_percent = 25 # percent of original size
      width = int(img.shape[1] * scale_percent / 100)
      height = int(img.shape[0] * scale_percent / 100)
      dim = (width, height)
      # resize image
      frame = cv.resize(img, dim, interpolation = cv.INTER_AREA)
      frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
      lowerBound = (
         max(0, min(255,LOOT_COLOR[2] - COLOR_DEVIATION)),
         max(0, min(255,LOOT_COLOR[1] - COLOR_DEVIATION)),
         max(0, min(255,LOOT_COLOR[0] - COLOR_DEVIATION)))
      upperBound = (
         max(0, min(255,LOOT_COLOR[2] + COLOR_DEVIATION)),
         max(0, min(255,LOOT_COLOR[1] + COLOR_DEVIATION)),
         max(0, min(255,LOOT_COLOR[0] + COLOR_DEVIATION)))
      frameGray = cv.inRange(frame, lowerBound, upperBound)
      #cv.imshow("pre thresh", frameGray)
      ret, thresh = cv.threshold(frameGray, 100, 255, 0)
      #thresh = cv.erode(thresh, None, iterations=1)
      thresh = cv.dilate(thresh, None, iterations=1)
      #cv.imshow("test", thresh)

      contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

      #cv.drawContours(frame, contours, -1, (0,255,0), 1)
      foundThingToClick = False
      for contour in contours:
         if cv.contourArea(contour) < 100:
            continue

         approx = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, True), True)
         if len(approx) >= 4 and len(approx) <= 50:
            cv.drawContours(frame, [contour], 0, (0, 50, 200), 2)
            foundThingToClick = True

            # find center of the loot
            M = cv.moments(contour)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            #scale cX and cY by image scale
            cX *= 100/scale_percent
            cY *= 100/scale_percent
            cXList.append(cX)
            cYList.append(cY)
            break

   ### click on the loot! ###
   if foundThingToClick:
      last = pyautogui.position()

      vector = extrapolate(cXList, cYList, 1.1)
      predictedPoint = cXList[len(cXList) - 1] + vector[0], cYList[len(cYList) - 1] + vector[1]
      ctypes.windll.user32.SetCursorPos(int(offsetX + predictedPoint[0]), int(offsetY + predictedPoint[1]))
      time.sleep(0.005)
      leftClick()
      ctypes.windll.user32.SetCursorPos(int(last[0]), int(last[1]))

   print("nabbin' a loot")
   #cv.imshow("frame", frame)
   #cv.waitKey(10)

print(
   "\nPath of Automation:\n" + 
   "     _         _              _                _      ____ _ _      _             \n" +
   "    / \  _   _| |_ ___       | |    ___   ___ | |_   / ___| (_) ___| | _____ _ __ \n" +
   "   / _ \| | | | __/ _ \ _____| |   / _ \ / _ \| __| | |   | | |/ __| |/ / _ \ '__|\n" +
   "  / ___ \ |_| | || (_) |_____| |__| (_) | (_) | |_  | |___| | | (__|   <  __/ |   \n" +
   " /_/   \_\__,_|\__\___/      |_____\___/ \___/ \__|  \____|_|_|\___|_|\_\___|_|   \n\n" +
   "by LazyGuyWithRSI\n\n"
)

init()

print("Ready to grab some loot!\n")

keyboard.add_hotkey(HOTKEY, grabLoot)
while True:
   time.sleep(0.03) #keep it alive