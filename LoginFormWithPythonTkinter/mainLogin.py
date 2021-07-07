''' 
This is a basic login form with Python, Tkinter and PIL. I've tried to make it by following Object Oriented Principles. Further Contributions and ammendments are welcomed whole-heartedly. Thanks for giving my mini-project a try!!.. :)   
'''
from tkinter import *
from PIL import Image,ImageTk

# in this program i'll make an object oriented form ui-design with tkinter 
class myFormUI(Tk):
    def __init__(self,parent):
        '''this function initialises the init function of our Tk class and creates a window for us!!so we dont need to write root = Tk()'''
        self.parent = parent
        self.parent.title("Login Form")
        self.parent.configure(bg="#ccffff")
        self.parent.geometry("400x500")
        self.parent.minsize(400,500)
        self.parent.maxsize(400,500)
        self.parent.iconbitmap("Icons8-Windows-8-User-Interface-Login.ico")
        self.createLabel()
        self.createImageLabel()
        self.createNameEntry()
        self.createMailEntry()
        self.createPassEntry()
        self.createLoginButton()
        self.createSubmitButton()
    
    def success(self,n,e):
        ''' A pop-up window for successful login showing users data and a logout button'''
        new_root = Tk()
        new_root.title("Success!!")
        new_root.geometry("500x500")
        new_root.minsize(500,500)
        new_root.maxsize(500,500)
        new_root.config(bg="#ccffff")
        varMsg1 = "Welcome "+str.title(n)+" !!"
        varMsg2 = "Your Email ID is : "+str(e)
        labelMsg1 = Label(new_root,text=varMsg1,font=("Arial",15,"bold"),padx=20,pady=20,foreground="blue",background="pink",borderwidth=2,relief="solid")
        labelMsg1.pack(fill=X,anchor=N)
        labelMsg2 = Label(new_root,text=varMsg2,font=("Arial",15,"bold"),padx=20,pady=20,foreground="blue",background="pink",borderwidth=2,relief="solid")
        labelMsg2.pack(fill=X,anchor=N)
        btnClose = Button(new_root,text="Logout Now",font=("arial",12,"bold"),padx=15,pady=15,background="brown",foreground="yellow",activeforeground="yellow",activebackground="brown",command=new_root.destroy)
        btnClose.pack(anchor=N)
        new_root.mainloop()
    
    def loginMe(self):
        ''' this functions performs the login functionality for the program'''
        def emptyFieldError():
            screen = Tk()
            screen.title("Input Error!")
            screen.geometry("250x200")
            screen.minsize(350,140)
            screen.maxsize(350,140)
            screen.config(bg="#ccffff")
            errMsg = "Entry fields can't be left empty!"
            labelMsg = Label(screen,text=errMsg,font=("Arial",15,"bold"),padx=25,pady=25,foreground="blue",background="pink",borderwidth=2,relief="solid")
            labelMsg.pack(fill=X,anchor=N)

            btnClose = Button(screen,text="Quit!",font=("arial",12,"bold"),padx=15,pady=15,background="brown",foreground="yellow",activeforeground="yellow",activebackground="brown",command=screen.destroy)
            btnClose.pack(anchor=N)
            screen.mainloop()

        def sendInvalidMsg():
            ''' A pop-up window prompting user with invalid credentials message!'''
            new_root = Tk()
            new_root.title("Oops!!")
            new_root.geometry("300x300")
            new_root.minsize(300,300)
            new_root.maxsize(300,300)
            new_root.config(bg="#ccffff")
            varMsg = "Invalid Credentials Pal!!"
            labelMsg = Label(new_root,text=varMsg,font=("Arial",15,"bold"),foreground="blue",background="pink",borderwidth=2,relief="solid")
            labelMsg.pack(expand=YES,fill=BOTH)
            btnClose = Button(new_root,text="Quit!",font=("arial",12,"bold"),padx=10,pady=10,background="brown",foreground="yellow",activeforeground="yellow",activebackground="brown",command=new_root.destroy)
            btnClose.pack(anchor=N)
            new_root.mainloop()

        nameData = self.nameEntry.get()
        emailData = self.mailEntry.get()
        passkData = self.passEntry.get()
        self.nameEntry.delete(0,END)
        self.mailEntry.delete(0,END)
        self.passEntry.delete(0,END)
        if(nameData!='' and emailData!='' and passkData!=''):
            if(nameData=='admin' and emailData=='admin@corp.in' and passkData=='pass123@456#'):
                self.success(nameData,emailData)
            elif(nameData=='user1' and emailData=='user1@corp.in' and passkData=='pass456@789#'):
                self.success(nameData,emailData)
            else:
                sendInvalidMsg()
        else:
            emptyFieldError()

    def submitInfo(self):
        '''this functions submits the info of a new user and greets them with a success message'''
        def emptyFieldError():
            screen = Tk()
            screen.title("Input Error!")
            screen.geometry("250x200")
            screen.minsize(350,140)
            screen.maxsize(350,140)
            screen.config(bg="#ccffff")
            errMsg = "Entry fields can't be left empty!"
            labelMsg = Label(screen,text=errMsg,font=("Arial",15,"bold"),padx=25,pady=25,foreground="blue",background="pink",borderwidth=2,relief="solid")
            labelMsg.pack(fill=X,anchor=N)

            btnClose = Button(screen,text="Quit!",font=("arial",12,"bold"),padx=15,pady=15,background="brown",foreground="yellow",activeforeground="yellow",activebackground="brown",command=screen.destroy)
            btnClose.pack(anchor=N)
            screen.mainloop()

        nameData = self.nameEntry.get()
        emailData = self.mailEntry.get()
        passkData = self.passEntry.get()
        self.nameEntry.delete(0,END)
        self.mailEntry.delete(0,END)
        self.passEntry.delete(0,END)
        if(nameData!='' and emailData!='' and passkData!=''):
            userValues = [{'name':nameData,'email':emailData,'passkey':passkData}]
            fields = ['name','email','passkey']
            try:
                with open('persons.csv','w+') as csvFile:
                    writer = DictWriter(csvFile, fieldnames=fields)
                    writer.writeheader()
                    writer.writerow(userValues)
                    print("Number of Records: ",len(writer.writerow()))
                    new_root = Tk()
                    new_root.title("Welcome")
                    new_root.geometry("250x250")
                    new_root.minsize(250,250)
                    new_root.maxsize(250,250)
                    new_root.config(bg="#ccffff")
                    varMsg = "Successfully Submitted!!"
                    labelMsg = Label(new_root,text=varMsg,font=("Arial",15,"bold"),foreground="blue",background="pink",borderwidth=2,relief="solid")
                    labelMsg.pack(expand=YES,fill=BOTH)
                    btnClose = Button(new_root,text="Done!",font=("arial",12,"bold"),padx=10,pady=10,background="brown",foreground="yellow",activeforeground="yellow",activebackground="brown",command=new_root.destroy)
                    btnClose.pack(anchor=N)
                    new_root.mainloop()
            except FileNotFoundError:
                print("Sorry File Does not exists!")
            except:
                print("Other error")
        else:
            emptyFieldError()
            
    def createLabel(self):
        '''this function creates the welcome label of the main window'''
        labelFont = ("Helvetica",18,"bold")
        label = Label(self.parent,text="Welcome to Login Page",pady=35,font=labelFont,foreground="blue",background="pink",borderwidth=2,relief="solid")
        label.place(relx=0.50,rely=0.02,relwidth=0.8,relheight=0.1,anchor=N)
    
    def createImageLabel(self):
        '''this function creates the label image for the main window'''
        img = Image.open("Age-Child-Female-Light-icon.png")
        render = ImageTk.PhotoImage(img)
        self.label = Label(self.parent,image=render,cursor="heart")
        self.label.image = render
        self.label.place(relx=0.48,rely=0.18,anchor=N)
    
    def createNameEntry(self):
        ''' this function creates labels and entry field for the name '''
        userImg = Image.open("Users-Name-icon.png")
        renderUserImg = ImageTk.PhotoImage(userImg)
        self.userImgLabel = Label(self.parent,image=renderUserImg,bd=0)
        self.userImgLabel.image = renderUserImg
        self.userImgLabel.place(relx=0.1,rely=0.47,anchor=N)

        self.nameLabel = Label(self.parent,text="User Name:",font=("arial",14,"normal"),background="pink")
        self.nameLabel.place(relx=0.3,rely=0.47,anchor=N)
        
        self.nameEntry = Entry(self.parent,bd=1,relief="sunken",foreground="black",background="#ffff33")
        self.nameEntry.place(relx=0.46,rely=0.47,relwidth=0.45,relheight=0.05)
    
    def createMailEntry(self):
        '''this function creates the labels and entry field for the email'''
        emailImg = Image.open("Email-3-icon.png")
        renderEmailImg = ImageTk.PhotoImage(emailImg)
        self.emailImgLabel = Label(self.parent,image=renderEmailImg,bd=0)
        self.emailImgLabel.image = renderEmailImg
        self.emailImgLabel.place(relx=0.1,rely=0.55,anchor=N)

        self.mailLabel = Label(self.parent,text="Enter Email:",font=("arial",14,"normal"),background="pink")
        self.mailLabel.place(relx=0.3,rely=0.55,anchor=N)
        
        self.mailEntry = Entry(self.parent,bd=1,relief="sunken",foreground="black",background="#ffff33")
        self.mailEntry.place(relx=0.46,rely=0.55,relwidth=0.45,relheight=0.05)
    
    def createPassEntry(self):
        '''this function creates the labels and entry for the password'''
        keyImg = Image.open("Key-icon.png")
        renderKeyImg = ImageTk.PhotoImage(keyImg)
        self.keyImgLabel = Label(self.parent,image=renderKeyImg,bd=0)
        self.keyImgLabel.image = renderKeyImg
        self.keyImgLabel.place(relx=0.1,rely=0.63,anchor=N)

        self.passLabel = Label(self.parent,text="Password:",font=("arial",14,"normal"),background="pink")
        self.passLabel.place(relx=0.3,rely=0.63,anchor=N)
        
        self.passEntry = Entry(self.parent,bd=1,relief="sunken",foreground="black",background="#ffff33")
        self.passEntry.place(relx=0.46,rely=0.63,relwidth=0.45,relheight=0.05)
    
    def createLoginButton(self):
        ''' this button creates the login button and login functionality'''
        self.loginButton = Button(self.parent,text="Login",font=("arial",12,"bold"),padx=10,pady=10,background="brown",foreground="yellow",activeforeground="yellow",activebackground="brown",command=self.loginMe)
        self.loginButton.place(relx=0.245,rely=0.755,relwidth=0.2,relheight=0.08,anchor=N)
    
    def createSubmitButton(self):
        ''' this button creates the submit button and submit info functionality'''
        self.submitButton = Button(self.parent,text="Submit",font=("arial",12,"bold"),padx=10,pady=10,background="brown",foreground="yellow",activeforeground="yellow",activebackground="brown",command=self.submitInfo)
        self.submitButton.place(relx=0.645,rely=0.755,relwidth=0.2,relheight=0.08,anchor=N)


if __name__=='__main__':
    ''' create an object of our myFormUI class in order to run the program'''
    root = Tk()
    run = myFormUI(root)
    root.mainloop()
