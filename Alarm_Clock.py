from tkinter import *
from datetime import datetime
import time
import playsound



def check_alarm(setTime):
    while True:
        currenttime=datetime.now().strftime('%H:%M:%S')
        if currenttime==setTime:
            print('alaaarrmmmm')
            playsound.playsound("/home/tor/Downloads/Koi_Mil_Gaya_-_Koi_Mil_Gaya____4k_Video____Hrithik_Roshan%2C_Priti_Zinta___Koi_Mil_Gaya___90_s_Song_s(256k).mp3")
            break
           

def set_alarm():
    alarmtime=f'{hour.get()}:{min.get()}:{sec.get()}'
    check_alarm(alarmtime)

clock = Tk()
clock.title("Alarm Clock")
clock.geometry("400x200")
Time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=60,y=120)
AddTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 120)
SetYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
HourTime= Entry(clock,textvariable = hour,bg = "black",width = 15).place(x=110,y=30)
MinTime= Entry(clock,textvariable = min,bg = "black",width = 15).place(x=160,y=30)
SecTime = Entry(clock,textvariable = sec,bg = "black",width = 15).place(x=210,y=30)

#To take the time input by user:
Submit = Button(clock,text = "Set Alarm",fg="white",width = 10,command = set_alarm).place(x =110,y=70)

clock.mainloop()
#Execution of the window.

win.mainloop()