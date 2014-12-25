#!usr/bin/python
# Auteur : knonn
# Utilitaire pour allumage ou extinction des ports GPIO
import RPi.GPIO as GPIO
import subprocess

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

a = raw_input("Quel port voulez vous controler ?")
a = int(a)

GPIO.setup(a, GPIO.OUT)

while 1:
    b = raw_input("Voulez vous allumer ou eteindre le port ?\n \t1. Allumer\n \t2.Eteindre\nChoice number : ")
    b = int(b)

    if b == 1:
        GPIO.output(a, True)
        print("Port %s allume" % a)
        break
    elif b == 2:
        GPIO.output(a, False)
        print("Port %s eteint" % a)
        break
    else:
        print("Entree incorrecte, recommencez")
