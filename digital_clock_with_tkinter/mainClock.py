from tkinter import *
import sys
import time

def getTime():
    currentTime = time.strftime("%H:%M:%S")
    getTimeLabel.config(text=currentTime)
    getTimeLabel.after(200, getTime)

root = Tk()
root.geometry("500x250")
root.title("Welcome to Digital Clock")
root.wm_iconbitmap("clk.ico")

##making the different labels for our program
welcomeLabel = Label(root, text="Digital Clock", font=("Arial", 30, "bold"), padx=25, pady=15)
getTimeLabel = Label(root, font=("Arial", 30, "bold"), bg="white", foreground="green", pady=25, padx=100)
## we need to call our function now which will give us the time 
getTime() 
hmsLabel = Label(root, text="hrs  min  sec", font=("Arial", 15, "bold"))

##placing order of different labels using Pack Manager
welcomeLabel.pack()
getTimeLabel.pack()
hmsLabel.pack()

root.mainloop()
