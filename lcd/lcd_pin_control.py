#!usr/bin/python

#    Utilitaire de gestion d'alimentation des ports GPIO sur Raspberry Pi
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

a = raw_input("Quel pin GPIO voulez vous controler ? (Entrer le numero du pin)")
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
