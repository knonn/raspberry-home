#!usr/bin/python
# Auteur : knonn
# Utilitaire pour allumage ou extinction des ports GPIO
import RPi.GPIO as GPIO
import subprocess

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

a = raw_input("Quel pin GPIO voulez vous controler ? (Entrer le numéro du pin)")
a = int(a)

c = raw_input("Choisissez le mode\n \t1. IN\n \t2. OUT\nChoice number : ")
c = int(c)

while 1 :
    if c == 1:
        GPIO.setup(a, GPIO.IN)
        print("Port %s mode IN activated." % a)
        break
    elif c == 2:
        GPIO.setup(a, GPIO.OUT)
        print("Port %s mode OUT activated" % a)
        break
    else:
        print("Entree incorrecte, recommencez")

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
