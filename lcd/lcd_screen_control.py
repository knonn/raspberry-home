#!/usr/bin/python

#    Utilitaire pour l'allumage ou l'extinction d'un LCD 16x2 branche au Raspberry Pi via un module relai
#    Copyright (C) 2015  <romain.besland@cryptolab.net>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import RPi.GPIO as GPIO
import subprocess

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)


while 1:
	a = raw_input("What do you want to do ?\n \t1. Switch ON the LCD\n \t2. Switch OFF the LCD\n\nChoice number : ")
	a = int(a)

	if a == 1:
		GPIO.output(12, True)
		GPIO.output(16, True)
		GPIO.output(18, True)
		GPIO.output(22, True)
		GPIO.output(24, True)
		GPIO.output(26, True)
		GPIO.output(7, False)
		subprocess.Popen(["sudo", "/etc/init.d/lcd"])
		print("Setting LCD ON : \033[92mDone.")
		break
	elif a == 2:
		GPIO.output(12, False)
                GPIO.output(16, False)
                GPIO.output(18, False)
                GPIO.output(22, False)
                GPIO.output(24, False)
                GPIO.output(26, False)		
		GPIO.output(7, True)
		subprocess.call(["sudo", "killall", "lcd"])
		print("Setting LCD OFF : \033[92mDone.")
		break
	else:
		print("\033[91mWrong input, try again\033[0m\n")
