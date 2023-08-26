from playsound import playsound
import pygame

import time

clear = "\033[J"
clear_and_return = "\033[H"

def alarm(seconds):
    timePassed = 0

    print(clear)
    while timePassed < seconds:
        time.sleep(1)
        timePassed = timePassed + 1

        timeLeft = seconds - timePassed

        minutes = timeLeft // 60
        second = timeLeft % 60

        print( f"{clear_and_return}Alarm will sound in : {minutes : 02d} : {second : 02d}")
    playsound("alarm.mp3")
  
min = int(input("Enter minutes : "))
sec = int (input("Enter seconds :"))

total = min * 60 + sec
alarm(total)