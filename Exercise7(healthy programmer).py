# #healthy programmer
# 9am to 5pm
# water - water.mp3 - 3.6 liters - Drank every 40 mint
# Eyes - eyes.mp3 - every 30  minute - Eydone
# Physical Exercise - exercise.mp3 - every 45 minute - Exdone
# rule
# Pygame module to play audio
#-----------------------------------------------------------------------------------
from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    # musiconloop("meri zindagi.mp3","stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersec = 5
    eyesec = 20
    exsec =  10

    while True:
        if time()-init_water > watersec:
            print("Time to drink Water. Enter 'Drank' to stop the alarm. ")
            musiconloop("meri zindagi.mp3","Drank")
            init_water = time()
            log_now("Drank water at")
        if time()-init_eyes > eyesec:
            print("Time to do Eye Exercise. Enter 'Eydone' to stop the alarm. ")
            musiconloop("Barish Ban Jana.mp3","Eydone")
            init_eyes = time()
            log_now("Eye Ex. done at")
        if time()-init_exercise > exsec:
            print("Time to do Exercise. Enter 'Exdone' to stop the alarm. ")
            musiconloop("khushi jab bhi.mp3","Exdone")
            init_exercise = time()
            log_now("Exercise done at")