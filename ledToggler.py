#Resouces
from Tkinter import *
import tkFont as TheFont
from gpiozero import LED
import RPi.GPIO as GPIO
#Setup the system
GPIO.setmode(GPIO.BCM)
led1 = LED(20)
led2 = LED(16)
led3 = LED(12)
#Declaire the window
win = Tk()
var= IntVar()
win.title("LED Toggler")
win.geometry('800x480')
#The font
myFont = TheFont.Font(family = 'Helvetica', size = 14, weight = "bold")
#The function to toggle the light
def ledToggle():
	if var.get()==1:
		led1.on()
		led2.off()
		led3.off()
	if var.get()==2:
		led2.on()
		led1.off()
		led3.off()	
	if var.get()==3:
		led3.on()
		led1.off()
		led2.off()
#Function to exit the program
def exitProgram():
	GPIO.cleanup()
	win.quit()
#Create the exit button
exitButton = Button (win, text = "Exit", font = myFont, command = exitProgram, height = 2, width = 6)
exitButton.pack(side = BOTTOM)
#Create the radio button for 3 light options
L1 = Radiobutton(win, text = "LED1", font = myFont, variable=var, value=1, command = ledToggle)
L1.pack(anchor=W)

L2 = Radiobutton(win, text = "LED2", font = myFont, variable=var, value=2, command = ledToggle)
L2.pack(anchor=W)

L3 = Radiobutton(win, text = "LED3", font = myFont, variable=var, value=3, command = ledToggle)
L3.pack(anchor=W)
#Run the program
mainloop()


