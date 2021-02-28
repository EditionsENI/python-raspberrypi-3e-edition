#!/usr/bin/env python3
from time import sleep

temperature = 10

while temperature < 15:
    temperature = temperature + 1
    if temperature == 13:
        continue
    if temperature == 14:
        break
    print(f"L'eau est désormais à {temperature} degrés")
    print("L'eau n'est pas assez chaude")
    print("J'augmente la température d'un degré ...")
    sleep(1)

print("C'est prêt !")
