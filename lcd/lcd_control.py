#!/usr/bin/python
# Auteur : knonn
# Utilitaire pour l'allumage ou l'extinction d'un LCD 16x2 branché au Raspberry Pi B+ via un module relai
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

while 1:
	a = raw_input("What do you want to do ?\n \t1. Switch ON the LCD\n \t2. Switch OFF the LCD\n\nChoice number : ")
	a = int(a)

	if a == 1:
		GPIO.output(7, False)
		print("Setting LCD ON : \033[92mDone.")
		break
	elif a == 2:
		GPIO.output(7, True)
		print("Setting LCD OFF : \033[92mDone.")
		break
	else:
		print("\033[91mWrong input, try again\033[0m\n")
