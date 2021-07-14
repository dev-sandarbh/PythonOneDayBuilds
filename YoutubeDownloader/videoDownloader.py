import tkinter, pytube
from tkinter import font
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from pytube import *

def startDownload():
    ''' This function starts the download and save it to a specified path. '''
    try:
        urlVal = urlEntry.get()
        
        # changing state, text and bgcolor of button
        downBtn.config(text="Downloading....")
        downBtn.config(background="#153131")
        downBtn.config(foreground="#ffffff")
        downBtn.config(state=DISABLED)

        path_to_save = askdirectory()
        print("Directory Chosen: ", path_to_save)
        if path_to_save is None:
            return 

        # creating object of YouTube Class
        utubeObj = YouTube(urlVal)
        
        # selecting first stream out of all available streams
        mainStream = utubeObj.streams.first()
        
        # downloading the selected stream
        mainStream.download(path_to_save)
        
        # changing state, text and bgcolor of button again after downloading gets complete
        downBtn.config(text="Start Again..")
        downBtn.config(state=NORMAL)
        downBtn.config(background="#2E933C")
        downBtn.config(foreground="#ffffff")

        urlEntry.delete()

        # showing a info message
        showinfo("Download Status", "Downloaded Successfully")
        print("Successfully Downloaded Video....")



    except Exception as e:
        print(e)
        print("Sorry Video Cannot be downloaded.")

''' Creating GUI '''
root = Tk()
root.title("YouTube Video Downloader")
root.geometry("600x450")
root.iconphoto(False, PhotoImage(file='vid64px.png'))

imgFile = PhotoImage(file='vid256px.png')
introLabel = Label(root, image=imgFile)
introLabel.pack(side='top')

urlEntry = Entry(root, font=('Verdana', 15), justify='center')
urlEntry.pack(side='top', fill='x', padx=75)

downBtn = Button(root, text="Click To Download..", font=('Verdana', 15), foreground='#ffffff', background='#d4483f', relief='ridge', command=startDownload)
downBtn.pack(side='top', pady=25)

if __name__ == "__main__":
    root.mainloop()