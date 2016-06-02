# import list, a lot of things are required to be imported for this code
from PIL import Image, ImageTk
from Tkinter import Tk, NORMAL, Label, BOTH, W, N, E, S, Entry, Text, INSERT, Toplevel, END, DISABLED, StringVar
from ttk import Frame, Style, Button, Label
import Tkinter
from profanity import profanity

from itertools import count
from datetime import datetime, time
import time
import random
from functools import partial

import Callingwordlist
import SQLStatements

# Login Screen UI

class LoginScreen(Frame):

    def __init__(self, parent):
        #__init__ is called when the function is called
        Frame.__init__(self, parent)
        #The interface inside the window is initiated
         
        self.parent = parent
        
        self.initUI()
        #self is passed through the function initUI
        
    def initUI(self):
      
        self.parent.title("Type!")
        self.pack(fill=BOTH, expand=1)
        
        style = Style()
        style.configure("TFrame", background="black")
        
        Logo = Image.open("Type!.png")
        #This block of text opens an image and creates a frame
        TypeLogo = ImageTk.PhotoImage(Logo)
        #That is the size of the image and places the image inside it
        label1 = Label(self, image=TypeLogo)
        label1.image = TypeLogo
        label1.place(x=342,y=80)
        label1.pack()

        Usertext = Text(self,width=23,height=1,font=("Courier",28))
        #This block of text creates a text widget called usertext that is inserted into the frame 'self'
        Usertext.pack()
        Usertext.config(bg="black",fg="white",bd=0)
        #It is given a black baground and white text                    
        Usertext.place(x=90,y=140)
        #The INSERT statement inserts text into the widget
        Usertext.insert(INSERT,"Username:")
        #The widget is placed at point x = 90, y = 140
        Usertext["state"] = DISABLED
        #"State" determines if the user can edit the string
    
        Passtext = Text(self,width=9,height=1,font=("Courier",28))
        #A text widget named passtext is created
        Passtext.pack()
        #Pack allows me to place the widget by exact coordinate
        Passtext.config(bg="black",fg="white",bd=0)
        #Length of the text widget must be stated or it continues forever
        Passtext.place(x=90,y=240)
        #Bg determines the colour of the background of the widget   
        Passtext.insert(INSERT,"Password:")
        #Fg determines the colour of the text of the widget
        Passtext["state"] = DISABLED #The user is not allowed to edit it

        global UsernameEntry
        UsernameEntry = Entry(self,font =("Courier",28), width = 20)
        #An entry widget named UsernameEntry is created
        UsernameEntry.pack(ipady=10)
        #ipady creates a slightly larger border around the widget on the y axis
        UsernameEntry.config(bg="#CEF6F5")
        #The background of the widget is set to a very light blue colour
        UsernameEntry.place(x=90,y=180)
        #.focus allows us to make the program focus on the
        UsernameEntry.focus()
        # entry widget when the game is started

        global PasswordEntry
        PasswordEntry = Entry(self,font =("Courier",28), width = 20, show = "*")
        # An entry widget name PasswordEntry is created
        PasswordEntry.pack(ipady=10)
        # show="*" makes all entered text appear as a *
        PasswordEntry.config(bg="#CEF6F5")
        # Width determines the width of the widget in number of characters
        PasswordEntry.place(x=90,y=280)

        global Errortext
        Errortext = Text(self, height = 1,font=("Courier",18))
        # A text widget named Errortext is created
        Errortext.pack()
        Errortext.config(bg="black",fg="white",bd=0)
        Errortext.place(x=90,y=350)
        Errortext["state"] = DISABLED
        # The user is not allowed to edit it
        
        SubmitButton = Button(self,text="Continue", command=lambda: submituser(self))
        #A button named SubmitButton is created and will execute the function submituser when being pressed
        SubmitButton.pack()
        SubmitButton.place(x=630,y=180, height = 43, width = 140)
        # The text on the button is "Continue"
        
        RegButton = Button(self,text="Create new account", command=lambda:createuser(self))
        # A button named RegButton is created and will execute the function createuser when being pressed
        RegButton.pack()
        RegButton.place(x=630,y=230, height = 43, width = 140)
        # The button is placed at x = 630, y = 230

        GuestButton = Button(self, text="Play as a guest", command=lambda:guest(self))
        # A button named GuestButton is created and will execute the function guest when being pressed
        GuestButton.pack()
        GuestButton.place(x=630,y=280, height = 43, width = 140)
        # The button is 43 pixels high and 140 pixels wide

# Declares that the user is logged on as a guest
def guest(self):
    global guestuser
    guestuser = 1
    # guestuser Tells the program that the user is logged on as a guest
    global CUser
    CUser = 0
    # CUser Tells the program that the user has created a new account
    global LUser
    LUser = 0
    # LUser Tells the program that the user has logged on
    donecreating(self)
    # Calls the function donecreating

# UI for creating a new user

class CreateUserUI(Frame):

    def __init__(self, parent):
        # __init__ is called when the function is called
        Frame.__init__(self, parent)
        # The interface inside the window is initiated   
         
        self.parent = parent
        
        self.initUI()
        # self is passed through the function initUI
        
    def initUI(self):
      
        self.parent.title("Type!")
        # The window name is set to "Type!"
        self.pack(fill=BOTH, expand=1)
        
        style = Style()
        # Style inside the window is created
        style.configure("TFrame", background="black")
        # Style is configured so that the background is black        
        
        Logo = Image.open("Type!.png")
        # This block of text opens an image and creates a frame
        TypeLogo = ImageTk.PhotoImage(Logo)
        # That is the size of the image and places the image inside it
        label1 = Label(self, image=TypeLogo)
        label1.image = TypeLogo
        label1.place(x=342,y=80)
        label1.pack()

        Usertext = Text(self,width=23,height=1,font=("Courier",28))
        # A text widget named Usertext is created
        Usertext.pack()
        Usertext.config(bg="black",fg="white",bd=0)
        Usertext.place(x=90,y=100)
        Usertext.insert(INSERT,"Username:") 
        Usertext["state"] = DISABLED
        # The user is not allowed to edit it

        Passtext = Text(self,width=9,height=1,font=("Courier",28))
        #A text widget named Passtext is created
        Passtext.pack()
        Passtext.config(bg="black",fg="white",bd=0)
        Passtext.place(x=90,y=200)
        Passtext.insert(INSERT,"Password:")
        Passtext["state"] = DISABLED
        # The user is not allowed to edit it

        Passtext2 = Text(self, width= 20, height = 1, font =("Courier",28))
        # A text widget named Passtext2 is created
        Passtext2.pack()
        Passtext2.config(bg="black",fg="white",bd=0)
        Passtext2.place(x=90,y=290)
        Passtext2.insert(INSERT,"Re-enter Password:")
        Passtext2["state"] = DISABLED
        # The user is not allowed to edit it

        global UsernameEntry
        UsernameEntry = Entry(self,font =("Courier",28), width = 20)
        # An entry widget named UsernameEntry is created   
        UsernameEntry.pack(ipady=10)
        UsernameEntry.config(bg="#CEF6F5")
        # The background colour of the widget is set to a very light blue
        UsernameEntry.place(x=90,y=140)
        UsernameEntry.focus()
        # The widget is focused on meaning it is automatically selected

        global PasswordEntry
        PasswordEntry = Entry(self,font =("Courier",28), width = 20, show = "*")
        # An entry widget named Passwordentry is created
        PasswordEntry.pack(ipady=10)
        PasswordEntry.config(bg="#CEF6F5")
        # The background colour of the widget is set to a very light blue
        PasswordEntry.place(x=90,y=240)

        global PasswordEntry2
        PasswordEntry2 = Entry(self,font =("Courier",28), width = 20, show = "*")
        # An entry widget named PasswordEntry is created
        PasswordEntry2.pack(ipady=10)
        PasswordEntry2.config(bg="#CEF6F5")
        # The background colout of the widget is set to a very light blue
        PasswordEntry2.place(x=90,y=340)

        global Errortext
        Errortext = Text(self, height = 1,font=("Courier",18))
        # A text widget named Errortext is created
        Errortext.pack()
        Errortext.config(bg="black",fg="white",bd=0)
        # The background is set to black and the text colour is set to white
        Errortext.place(x=90,y=400)
        Errortext["state"] = DISABLED
        # The text cannot be edited by the user
        
        RegButton = Button(self,text="Create new account", command=lambda:createuser1(self))
        # A button called RegButton is created and calls the function createuser1 when clicked
        RegButton.pack()
        RegButton.place(x=630,y=230, height = 43, width = 140)
        # The button is set to have a height of 43 pixels and a width of 140 pixels

# Checks all errors when creating an account and creates an account
def createuser1(self):
    global UserName
    UserName = UsernameEntry.get()
    # Username takes what the user entered into the UsernameEntry widget
    global Password
    Password = PasswordEntry.get()
    # Password takes what the user entered into the PasswordEntry widget
    global Password2
    Password2 = PasswordEntry2.get()
    # Password2 takes what the user entered into the PasswordEntry2 widget
    checkprofanity = profanity.contains_profanity(UserName)
    # The username string is checked for profanities
    if checkprofanity == True:
        # Checks for a profanity in the username
        Errortext["state"] = NORMAL
        # The Errortext widget state is changed so we can edit it
        Errortext.delete("1.0",END)
        # Everything inside the widget is deleted
        Errortext.insert(INSERT,"No profanities in the username please!")
        #The error message is inserted
        Errortext["state"] = DISABLED
        # The state is set back to disabled so the user cannot edit the widget
    elif UserName == "" or len(UserName) > 20:
        # Checks that the username is between 1 and 20 characters
        Errortext["state"] = NORMAL
        # The Errortext widget is edited, the relevant error message is inserted
        Errortext.delete("1.0",END)
        # And the state is set back to disabled
        Errortext.insert(INSERT,"Username must be between 1 and 20 characters")
        Errortext["state"] = DISABLED
    elif len(Password)<8:
        # Checks that the password is greater than eight characters
        Errortext["state"] = NORMAL
        # The Errortext widget is edited, the relevant error message is inserted
        Errortext.delete("1.0",END)
        # And the state is set back to disabled
        Errortext.insert(INSERT,"Password must be at least 8 characters")
        Errortext["state"] = DISABLED
    elif Password == Password2:
        # Makes sure that both entered passwords are the same
        SQLStatements.createnewuser(UserName,Password,self)
        if SQLStatements.online == 1:
            # Checks that the program is connected to the database
            Errortext["state"] = NORMAL
            # The Errortext widget state is changed so we can edit it
            Errortext.delete("1.0",END)
            # Everything inside the widget is deleted
            Errortext.insert(INSERT,"Cannot connect to database")
            #The error message is inserted
            Errortext["state"] = DISABLED
        else:
            if SQLStatements.errorcheck == 1:
                # Checks if the user wanted to be created already exists
                Errortext["state"] = NORMAL
                # The Errortext widget is edited, the relevant error message is inserted
                Errortext.delete("1.0",END)
                # And the state is set back to disabled
                Errortext.insert(INSERT,"User already exists")
                Errortext["state"] = DISABLED
            else:
                global guestuser             
                guestuser = 0
                # guestuser Tells the program that the user is logged on as a guest
                global CUser
                CUser = 1
                # CUser Tells the program that the user has created a new account
                global LUser 
                LUser = 0
                #LUser Tells the program that the user has logged on
                Errortext["state"] = NORMAL
                # The Errortext widget is edited, the relevant error message is inserted
                Errortext.delete("1.0",END)
                Errortext.insert(INSERT,"User has been created")
                Errortext["state"] = DISABLED
                # And the state is set back to disabled
                donecreating(self)
                # Calls the function donecreating
    else:
        Errortext["state"] = NORMAL
        # The Errortext widget is edited, the relevant error message is inserted
        Errortext.delete("1.0",END)
        # And the state is set back to disabled
        Errortext.insert(INSERT,"Passwords do not match")
        Errortext["state"] = DISABLED
            
    
# Destroys the self frame and sends the user to the create user UI screen
def createuser(self):
    self.destroy()  
    app = CreateUserUI(root)

# Resizes the window and takes the user to the main menu
def donecreating(self):
    self.destroy()
    # Destroys the self feame
    global truevalue
    truevalue = 1
    # Tells the program to display a log on message
    root.geometry("860x640+200+50") # Resizes the window to 860x640
    root.minsize(width = 860, height = 640)
    root.maxsize(width = 860, height = 640)
    app = MainMenuUI(root)
    # Creates the main menu UI

# Checks that the user has logged on with valid data
def submituser(self):
    global UserName
    UserName = UsernameEntry.get()
    # Username takes what the user entered into the UsernameEntry widget
    global Password
    Password = PasswordEntry.get()
    # Password takes what the user entered into the PasswordEntry widget
    SQLStatements.searchforuser(UserName,Password,self)
    # Runs the function searchforuser in the file SQLStatements
    if SQLStatements.online == 1:
        # Checks that the program is connected to the database
        Errortext["state"] = NORMAL
        # The Errortext widget state is changed so we can edit it
        Errortext.delete("1.0",END)
        # Everything inside the widget is deleted
        Errortext.insert(INSERT,"Cannot connect to database")
        #The error message is inserted
        Errortext["state"] = DISABLED
    else:
        if SQLStatements.account == 0:
        # Checks the variable account from the file SQLStatements
            Errortext["state"] = NORMAL
            # The Errortext widget is edited,the relevant error message is inserted.
            Errortext.delete("1.0",END)
            Errortext.insert(INSERT,"Username/Password entered incorrectly")
            Errortext["state"] = DISABLED # The state is set back to disabled
        if SQLStatements.account == 1:
        # Checks the variable account from the file SQLStatements
            global guestuser
            guestuser = 0
            # guestuser tells the program if the user is logged on as a guest
            global CUser
            CUser = 0
            # Cuser tells the program that the user has created a new acount
            global LUser
            LUser = 1
            # LUser tells the program if the user has logged on using a valid account
            donecreating(self)

# Initial Menu UI

class MainMenuUI(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Type!")
        self.pack(fill=BOTH, expand=1)
        
        style = Style()
        style.configure("TFrame", background="black")        
        
        Logo = Image.open("Type!.png")
        #This block of text opens an image and creates a frame
        TypeLogo = ImageTk.PhotoImage(Logo)
        #That is the size of the image and places the image inside it
        label1 = Label(self, image=TypeLogo)
        label1.image = TypeLogo
        label1.place(x=342,y=80)
        label1.pack()
        
        GameButton = Button(self, text="Main Game", command=lambda: main2(self.parent,self))
        # A button called GameButton is created and calls the function main2 when pressed 
        GameButton.pack()
        GameButton.place(x=344,y=200,height = 80,width = 176)

        TutorialButton = Button(self,text="Tutorial Level",command=lambda:tutorial(self))
        # A button called TutorialButton is created and calls the function tutorial when pressed
        TutorialButton.pack()
        TutorialButton.place(x=344, y=300 ,height = 80,width = 176)

        quitbutton = Button(self, text= "Quit",command=self.parent.destroy)
        # A button called quibutton is created and quits the window when pressed
        quitbutton.pack()
        quitbutton.place(x = 344,y = 400,height = 80,width = 176)

        helpbutton = Button(self, text = "Help",command=lambda:GameHelp(self))
        # A button called helpbutton is created calls the function GameHelp when pressed
        helpbutton.pack()
        helpbutton.place(x = 800, y = 590, height = 30, width = 40)

        if truevalue == 1:
        # Checks whether the log on message should be displayed or not
            logontext = Text(self,font=("Courier",18),height=1)
            # A text widget named logontext is created
            logontext.pack()
            logontext.config(bg="black",fg="white",bd=0)
            logontext.place(x=240,y=500)
            if guestuser == 1:
            # Checks if the user is logged on as a guest
                logontext.insert(INSERT,"logged in as guest user!")
                # The relevant logon message is inserted into logontext
                logontext["state"] = DISABLED
                # The user cannot edit this text
            elif CUser == 1:
            # Checks if the user has created a new account
                logontext.insert(INSERT,"New account created!")
                # The relevant logon message is inserted into logontext
                logontext["state"] = DISABLED
                # The user cannot edit this text
            elif LUser == 1:
            # Checks if the user has logged on with a vaid account 
                logontext.insert(INSERT,"Successfully logged on!")
                # The relevant logon message is inserted into logontext
                logontext["state"] = DISABLED
                # The user cannot edit this text

# This function destroys the self frame and calls the help game UI
def GameHelp(self):
    global truevalue
    truevalue = 0
    # Tells the program not to display the log on message again
    app = HelpGameUI(root)
    # Calls the class HelpGameUI
    self.destroy()
    # Destroys the frame called self

#UI for help images

class HelpGameUI(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Type!")
        self.pack(fill=BOTH, expand=1)
        
        style = Style()
        style.configure("TFrame", background="black")

        hp = Image.open("helpimages/help1.png")
        #This block of text opens an image and creates a frame
        help1 = ImageTk.PhotoImage(hp)
        #That is the size of the image and places the image inside it
        helplable = Label(self, image=help1)
        helplable.image = help1
        helplable.place(x=0,y=0)
        helplable.pack()
        
        imagecount = 1
        # The variable imagecount is set to 1
        
        nextbutton = Button(self, text = "Next", command = lambda:nextimage(self,nextbutton,helplable,imagecount))
        nextbutton.pack() # A button called nextbutton is created and calls the function nextimage when pressed
        nextbutton.place(x=760,y=560, height = 50, width = 70)

# Destroys the self frame and sends the user back to the main menu
def gobacktomain(self): 
    self.destroy()
    app = MainMenuUI(root)

# Used for the help screen, advances the user through the help images
def nextimage(self,nextbutton,helplable,imagecount): 

    nextbutton.destroy()
    # Destroys the nexbutton button
    helplable.destroy()
    # Destroys the helplable lable
    
    imagecount += 1
    # Adds one to the variable imagecount
    simage = str(imagecount)
    # Turns imagecount to a string and assigns it to the variable simage
    wpicture = "helpimages/help"+simage+".png"
    # creates a string for the directory and name of the relevant help image
    
    hp = Image.open(wpicture)
    # Opens the help image where the directory is the string assigned to the variable wpicture
    help1 = ImageTk.PhotoImage(hp)
    # Materialises the image into python and assigns it to the lable named helplable
    helplable = Label(self, image= help1)
    helplable.image = help1
    helplable.place(x=0, y=0)
    helplable.pack()

    if imagecount > 14:
        # Stops the user advancing through the images when the final image is reached
        returnmain = Button(self, text = "Finish", command = lambda: gobacktomain(self))
        # A button named returnmain is created and calls the function called gobacktomain when pressed
        returnmain.pack()
        returnmain.place(x=760,y=560,height=50,width=70)

    else:
        nextbutton = Button(self, text = "Next", command= lambda: nextimage(self,nextbutton,helplable,imagecount))
        # A button named nextbutton is created and calls the functio nextimage when pressed
        nextbutton.pack()
        nextbutton.place(x=760,y=560,height=50,width=70)    

# This function takes the program to the main game
def main2(root,self):
    global truevalue
    truevalue = 0
    # Tells the program not to display the logon message again
    app = MainGameUI(root)
    # The class MainGameUI is called
    self.destroy()
    # The frame self is destroyed
    start(self)
    # The function start is called

# This function takes the program to the tutorial level
def tutorial(self):
    global truevalue
    truevalue = 0
    # Tells the program not to display the logon message again
    app = TutorialUI(root)
    # The class TutorialUI is called
    self.destroy()
    # The frame self is destroyed

# This function sends the user back to the main menu
def returntutmain(self):
    global truevalue
    truevalue = 0
    # Tells the program not to display the logon message again
    self.destroy()
    # Destroys the self frame
    root.unbind("<Key>")
    # Unbinds key from the window so that no function is called when any key is pressed
    app = MainMenuUI(root)
    # The class MainMenuUI is called

# Creates the tutorial screen

class TutorialUI(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Type!")
        self.pack(fill=BOTH, expand=1)
        
        style = Style()
        style.configure("TFrame", background="black")

        Type = Image.open("Type!.png")
        # This block of text opens an image and creates a frame
        Typet = ImageTk.PhotoImage(Type)
        # That is the size of the image and places the image inside it
        label3 = Label(self, image=Typet)
        label3.image = Typet
        label3.place(x=0, y=0)

        # A button called MenuButton is created and calls the function returntutmain when pressed 
        MenuButton = Button(self, text="Main Menu",command = lambda: returntutmain(self)) 
        MenuButton.pack()
        MenuButton.place(x=560,y=20,height = 80,width = 100)

        # A button called QuitButton is created and destroys the root window when pressed
        QuitButton = Button(self,text="Quit",command=self.parent.destroy)
        QuitButton.pack()
        QuitButton.place(x=680,y=20,height = 80,width = 100)

        # A button called StartButton is created and calls the function InitTutorial when pressed
        StartButton = Button(self, text="Start",command = lambda: InitTutorial(self,StartButton))
        StartButton.pack()
        StartButton.place(x=440,y=20,height=80,width=100)

# The function updates the UI when a key is pressed in the tutorial
def recall(key,self,letter,Nletter,total,score,accuracy,KeyLabel):
    initiated = 1
    # initiated tells the program that the UI has already been initiated once
    total += 1
    # Total counts the total number of letters entered
    if key.char == letter:
        # key.char takes what the user has entered, this if statement compares this to the letter on screen
        score += 1
        # Score represents the number of letters entered correctly
    accuracy = ((score*100)/(total))
    # Accuracy is calculated by diving the number of correct letters by the total number of letters
    letter = Nletter
    # Assigns the letter to enter next to the letter to enter

    KeyLabel.destroy()
    # Destroys the label containing the on screen keyboard
    
    directory = "keys/key"+letter+".png"
    # Directory is a string with the correct directory for the required keyboard image
    OSKeyboard = Image.open(directory)
    # Inputs the relevant keyboard image into a label
    OSK = ImageTk.PhotoImage(OSKeyboard)
    # The label is then placed onto the screen
    KeyLabel = Label(self, image = OSK)
    KeyLabel.image = OSK
    KeyLabel.place(x=80,y=360)
   
    elapsed_time = time.time() - start_time
    # Elapsed_time counts the time since the tutorial was initiated
    
    if elapsed_time >= 60:
    # The user is taken to the end screen when the elapsed time is greater than 60 seconds
        root.unbind("<Key>")
        # Unbinds key from the window so that no function is called when any key is pressed 
        global acc
        acc = str(accuracy)
        # Accuracy is turned into a string and assigned to the variable acc
        global kdpm
        # Total is equivalent to key depressions per minute so total is turned
        kdpm = str(total)
        # into a string and assigned to the variable kdpm  
        EndTutorial(self)
        # The function EndTutorial is called
    else:
        NASCIILetter = random.randint(97,122)
        # NASCIILetter is assigned to a random variable between 97 and 122 inclusive
        Nletter = chr(NASCIILetter)
        # This letter is turned into its ASCII value and assigned to the variable Nletter
        while Nletter == letter:
        # Checks that the next letter to enter is not the same as the letter to enter
            NASCIILetter = random.randint(97,122)
            # If so then Nletter is chosen at random again
            Nletter = chr(NASCIILetter)
            
        StartTutorial(self,initiated,letter,Nletter,total,score,accuracy,KeyLabel)
        # Function StartTutorial is called
    
# Initiates the non visual side of the tutorial
def InitTutorial(self,StartButton):  

    StartButton.destroy()
    # The StartButton button is destroyed
     
    initiated = 0
    # The program is told that the Tutorial has not yet been initiated
    
    ASCIILetter = random.randint(97,122)
    # ASCIILetter is assigned to a random variable between 97 and 122 inclusive
    letter = chr(ASCIILetter)
    # This letter is turned into its ASCII value and assigned to the variable Letter
    NASCIILetter = random.randint(97,122)
    # NASCIILetter is assigned to a random variable between 97 and 122 inclusive
    Nletter = chr(NASCIILetter)
    # This letter is turned into its ASCII value and assigned to the variable Nletter
    
    # The three variables, total, score and accuracy are created
    total = 0 
    score = 0
    accuracy = 0

    # AccLabel is the label used to hold the counter
    AccLabel = Label(self, font = ("Courier",18)) 
    AccLabel.pack()
    AccLabel.place(x=300,y=40)

    start_counter(AccLabel)
    # The counter is assigned to the AccLabel Label
    
    directory = "keys/key"+letter+".png"
    # Directory is a string with the correct directory for the required keyboard image
    OSKeyboard = Image.open(directory)
    # Inputs the relevant keyboard image into a label
    OSK = ImageTk.PhotoImage(OSKeyboard)
    # The label is then placed onto the screen
    KeyLabel = Label(self, image = OSK)
    KeyLabel.image = OSK
    KeyLabel.place(x=80,y=360)

    global start_time
    start_time=time.time()
    # The time when the tutorial is initiated is assigned to the variable start_time
        
    StartTutorial(self,initiated,letter,Nletter,total,score,accuracy,KeyLabel)
    #The Function StartTutorial is called

# Starts/edits the tutorial interface    
def StartTutorial(self,initiated,letter,Nletter,total,score,accuracy,KeyLabel):

    # Key is bound to the root window meaning that the even recall will be called when any key is pressed
    root.bind("<Key>",lambda event: recall(event,self,letter,Nletter,total,score,accuracy,KeyLabel))

    if initiated == 0:
    # The initial UI is initiated if it hasnt already been initiated

        timetext = Text(self,font=("Courier",18),width=14,height=1)
        # A text widget named timetext is created
        timetext.pack()
        timetext.config(bg="black",fg="white",bd=0)
        timetext.insert(INSERT,"Time elapsed")
        timetext.place(x=230,y=10)
        timetext["state"] = DISABLED
        # The user cannot edit this widget
        
        Wtext1 = Text(self,width=23,height=1,font=("Courier",25))
        # A text widget named Wtext1 is created
        Wtext1.pack()
        Wtext1.config(bg="black",fg="white",bd=0)
        Wtext1.place(x=250,y=150)
        Wtext1.insert(INSERT,"Letter to enter:")
        Wtext1["state"] = DISABLED
        # The user cannot edit this widget
        
        global Wentry
        # The Wentry text widget is globalised
        Wentry = Text(self,font =("Courier",38), width = 1, height = 1)
        # A text widget named Wentry is created
        Wentry.pack()
        Wentry.config(bg="white",fg="black",bd=0)
        Wentry.place(x=380,y=190)
        Wentry.insert(INSERT,letter)
        Wentry["state"] = DISABLED

        global Wentry2
        Wentry2 = Text(self,font =("Courier",38), width = 1, height = 1)
        # A text widget named Wentry2 is created
        Wentry2.pack()
        Wentry2.config(bg="white",fg="black",bd=0)
        Wentry2.place(x=690,y=190)
        Wentry2.insert(INSERT,Nletter)
        Wentry2["state"] = DISABLED
        # The user cannot edit this widget

        Wtext2 = Text(self,width=23,height=1,font=("Courier",25))
        # A text widget named Wtext2 is created
        Wtext2.pack()
        Wtext2.config(bg="black",fg="white",bd=0)
        Wtext2.place(x=600,y=150)
        Wtext2.insert(INSERT,"Next letter:")
        Wtext2["state"] = DISABLED
        # The user cannot edit this widget

        Acctext = Text(self,width=8,height=1,font=("Courier",28))
        # A text widget named Acctext2 is created
        Acctext.pack()
        Acctext.config(bg="black",fg="white",bd=0)
        Acctext.place(x=20,y=190)
        Acctext.insert(INSERT,"Accuracy")
        Acctext["state"]=DISABLED
        # The user cannot edit this widget
        
        global Accentry
        Accentry = Text(self,width=3,height=1,font=("Courier",28))
        # A text widget named Accentry2 is created
        Accentry.pack()
        Accentry.config(bg="white",fg="black",bd=0)
        Accentry.place(x=70,y=240)
        Accentry.insert(INSERT,accuracy)
        Accentry["state"]=DISABLED
        # The user cannot edit this widget
    
    elif initiated == 1:

        # This block of code allows us to edit the following text widgets
        Wentry["state"] = NORMAL
        Wentry2["state"] = NORMAL
        Accentry["state"] = NORMAL

        # Said text widgets are cleared
        Accentry.delete("1.0",END) 
        Wentry.delete("1.0",END)
        Wentry2.delete("1.0",END)

        # The relevant data is inserted into the following text widgets
        Accentry.insert(INSERT,accuracy) 
        Wentry.insert(INSERT,letter)
        Wentry2.insert(INSERT,Nletter)

        # The widgets are then re-disabled to stop the user from editing them
        Accentry["state"] = DISABLED 
        Wentry["state"] = DISABLED
        Wentry2["state"] = DISABLED

# The function destroys the self frame and initiates the End Tutorial UI
def EndTutorial(self):
    self.destroy()
    app = EndTutorialUI(root)

# Results screen for the tutorial

class EndTutorialUI(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
        
        style = Style()
        style.configure("TFrame", background="black")
        
        Type = Image.open("Type!.png")
        # This block of text opens an image and creates a frame
        Typet = ImageTk.PhotoImage(Type)
        # The size of the image that the image is then placed into
        label3 = Label(self, image=Typet)
        label3.image = Typet
        label3.place(x=0, y=0)

        self.pack(fill=BOTH, expand=1)

        Ktext = Text(self,font=("Courier",28),width = 26, height=1)
        # A text widget named Ktext is created
        Ktext.pack()
        Ktext.config(bg="black",fg="white",bd=0)
        Ktext.insert(INSERT,"Key depressions per minute")
        Ktext.place(x=150,y=130)
        Ktext["state"] = DISABLED
        # The user cannot edit this widget
        
        KDPMtext = Text(self,font=("Courier",28), width = len(kdpm),height=1)
        # A text widget named KDPMtext is created
        KDPMtext.pack()
        KDPMtext.config(bg="white",fg="black",bd=0)
        KDPMtext.insert(INSERT,kdpm)
        KDPMtext.place(x=390,y=180)
        KDPMtext["state"] = DISABLED
        # The user cannot edit this widget
        
        Atext = Text(self,font=("Courier",28),width=15, height=1)
        # A text widget named Atext is created
        Atext.pack()
        Atext.config(bg="black",fg="white",bd = 0)
        Atext.insert(INSERT,"Total accuracy:")
        Atext.place(x=260,y=300)
        Atext["state"] = DISABLED
        # The user cannot edit this widget

        Acctext = Text(self,font=("Courier",28),width = len(acc), height=1)
        # A text widget named Acctext is created
        Acctext.pack()
        Acctext.config(bg="white",fg="black",bd=0)
        Acctext.insert(INSERT,acc)
        Acctext.place(x=390,y=350)
        Acctext["state"] = DISABLED
        # The user cannot edit this widget

        # A button named MainButton is created and calls the function returnmain when pressed
        MainButton = Button(self, text="Main Menu",command = lambda: returnmain(self))
        MainButton.pack()
        MainButton.place(x=660,y=500,height = 80,width = 100)
    
# This function destroys the self frame and sends the user to the main menu
def returnmain(self): 
    self.destroy()
    app = MainMenuUI(root)

# The following three functions are called when selecting difficulty
def easy(self,ButtonWindow):
    global difficulty
    difficulty = 1
    # The difficulty is set to 1
    Callingwordlist.CallWordlist(difficulty)
    # The function CallWordlist from the file Callingwordlist is executed
    ModifyUI(self,ButtonWindow)
    # The function ModifyUI is called

def medium(self,ButtonWindow):
    global difficulty
    difficulty = 2
    # The difficulty is set to 2
    Callingwordlist.CallWordlist(difficulty)
    # The function CallWordlist from the file Callingwordlist is executed
    ModifyUI(self,ButtonWindow)
    # The function ModifyUI is called

def hard(self,ButtonWindow):
    global difficulty
    difficulty = 3
    # The difficulty is set to 3
    Callingwordlist.CallWordlist(difficulty)
    # The function CallWordlist from the file Callingwordlist is executed
    ModifyUI(self,ButtonWindow)
    # The function ModifyUI is called

# The start button is placed and the buttonwindow window destroyed
def ModifyUI(self,ButtonWindow):
    StartButton.pack()
    # The start button is placed into the window and positioned
    StartButton.place(x=440,y=20,height=80,width=100)
    ButtonWindow.destroy()
    # The ButtonWindow Window is destroyed
    
# The select difficulty window is created    
def start(self): 
    
    ButtonWindow = Toplevel()
    # A sub window named button window is created
    ButtonWindow.title("Select Difficulty")
    # The window is named "Select Difficulty"
    ButtonWindow.geometry("320x160+300+300")
    # The window size is determined
    ButtonWindow.configure(background="black")
    # The background is set to black

    difftext = Text(ButtonWindow,height=1,font=("Calibri",20))
    # A text widget named Difftext is created
    difftext.pack()
    difftext.config(bg="black",fg="white",bd=0)
    difftext.place(x=40,y=10)
    difftext.insert(INSERT,"Select Your Difficulty:")
    difftext["state"] = DISABLED
    # The widget cannot be edited

    # A button named D1Button is created and the function easy is called when pressed
    D1Button = Button(ButtonWindow, text="1:Easy",command=lambda:easy(self,ButtonWindow))
    D1Button.pack()
    D1Button.place(x=20,y=50,height = 80,width = 80)

    # A button named D2Button is created and the function medium is called when pressed
    D2Button = Button(ButtonWindow,text="2:Medium",command=lambda:medium(self,ButtonWindow))
    D2Button.pack()
    D2Button.place(x=120,y=50,height = 80,width = 80)

    # A button named D3Button is created and the function hard is called when pressed
    D3Button = Button(ButtonWindow, text="3:Hard",command=lambda:hard(self,ButtonWindow))
    D3Button.pack()
    D3Button.place(x=220,y=50,height = 80,width = 80)


# UI For the main game

class MainGameUI(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
        
        style = Style()
        style.configure("TFrame", background="black")
        
        Type = Image.open("Type!.png")
        # This block of text opens an image and creates a frame 
        Typet = ImageTk.PhotoImage(Type)
        # The size of the image that the image is then placed into
        label3 = Label(self, image=Typet)
        label3.image = Typet
        label3.place(x=0, y=0)

        
        self.pack(fill=BOTH, expand=1)

        # A button named MenuButton is created and calls the function returnmain when pressed
        MenuButton = Button(self, text="Main Menu",command = lambda: returnmain(self))
        MenuButton.pack()
        MenuButton.place(x=560,y=20,height = 80,width = 100)

        # A button named QuitButton is created and destroys the window when pressed
        QuitButton = Button(self,text="Quit",command=self.parent.destroy)
        QuitButton.pack()
        QuitButton.place(x=680,y=20,height = 80,width = 100)

        # A button named StartButton is created and calls the function mains when pressed
        global StartButton
        StartButton = Button(root, text="Start",command = lambda: mains(self))
        StartButton.pack_forget() # pack_forgot means that the button is created but not on screen

# Initiates the main UI for the main game
def mains(self): 

    StartButton.destroy()
    # The start button is destroyed

    AccLabel = Label(self, font = ("Courier",18))
    # A label named AccLabel is created
    AccLabel.pack()
    AccLabel.place(x=290,y=40)
    
    start_counter(AccLabel)
    # The counter is placed inside the label called acclabel
    
    global start_time
    start_time=time.time()
    # Start_time is assigned to the time which the main game was initiated
    
    returncount = 0
    # Returncount determins if the UI has been initiated already and if the timer is greate than 60 seconds

    total = 0
    # The three variables, total, score and accuracy are created
    score = 0
    accuracy = 0
        
    maininit(returncount,self,total,score,accuracy)
    # the function maininit is called
   
    
def maininit(returncount,self,total,score,accuracy):

    # Enter is bound to the root window so that the function callback is called whenever enter is pressed
    root.bind("<Return>",lambda event: callback(self,event,total,score,accuracy))

    if returncount == 2:
        # this statement is true when the counter has reached 60 seconds
        global words_per_minute
        if difficulty > 1:
        # There are two words per phrase in difficulty 2 and 3, so WPM is doubled
            words_per_minute = score * 2
        else:
        # When the difficulty is 1, the score is the same as WPM
            words_per_minute = score
        global acc
        acc = accuracy
        # Acc is assigned to accuracy so that the value can be globalised correctly
        self.destroy()
        # The self frame is destroyed
        app = EndGameUI(root)
        # The class EndGameUI is called

    elif returncount == 0:
    # This statement is true when the game is called for the first time

        global entry1
        entry1 = Entry(self,font =("Courier",38), width = 22)
        # An entry widget named entry1 is created
        entry1.pack(ipady=10)
        entry1.config(bg="#CEF6F5")
        entry1.place(x=90,y=200)
        entry1.focus()
        # The widget is focused on when the game is started

        global entry2
        entry2 = Entry(self,font =("Courier",38), width = 22)
        # An entry widget named entry2 is created
        entry2.pack(ipady=10)
        entry2.config(bg="#CEF6F5")
        entry2.place(x=90,y=350)

        global text1
        text1 = Text(self,width=23,height=1,font=("Courier",38))
        # A text widget named text1 is created 
        text1.pack()
        text1.config(bg="black",fg="white",bd=0)
        text1.place(x=90,y=150)
        text1.insert(INSERT,Callingwordlist.word)
        text1["state"] = DISABLED
        # The user cannot edit this text widget
        # The DISABLED state stops the user from editing certain text boxes

        global text2
        text2 = Text(self,width=23,height=1,font=("Courier",38))
        # A text widget named text2 is created
        text2.pack()
        text2.config(bg="black",fg="white",bd=0)
        text2.place(x=90,y=300)
        text2.insert(INSERT,Callingwordlist.word2)
        # The variable word2 from the file Callingwordlist is inserted
        text2["state"] = DISABLED
        # The user cannot edit this text widget

        dtext = Text(self,font=("Courier",28),width=10,height=1)
        # A text widget named dtext is created
        dtext.pack()
        dtext.config(bg="black",fg="white",bd=0)
        dtext.insert(INSERT,"Difficulty")
        dtext.place(x=50,y=500)
        dtext["state"] = DISABLED
        # The user cannot edit this text widget

        atext = Text(self,font=("Courier",28),width=8,height=1)
        # A text widget named atext is created
        atext.pack()
        atext.config(bg="black",fg="white",bd=0)
        atext.insert(INSERT,"Accuracy")
        atext.place(x=595,y=500)
        atext["state"] = DISABLED
        # The user cannot edit this text widget

        global aentry
        aentry = Text(self,font=("Courier",28),width=3,height=1)
        # A text widget named aentry is created
        aentry.pack()
        aentry.config(bg="white",bd=0)
        aentry.insert(INSERT,accuracy)
        # The variable accuracy is inserted into this widget
        aentry.place(x=620,y=550)
        aentry["state"] = DISABLED
        # The user cannot edit this text widget

        timetext = Text(self,font=("Courier",18),width=14,height=1)
        # A text widget named timetext is created
        timetext.pack()
        timetext.config(bg="black",fg="white",bd=0)
        timetext.insert(INSERT,"Time elapsed")
        timetext.place(x=210,y=10)
        timetext["state"] = DISABLED
        # The user cannot edit this text widget

        dentry = Text(self,font=("Courier",28),width=1,height=1)
        # A text widget named dentry is created
        dentry.pack()
        dentry.config(bg="white",bd=0)
        dentry.place(x=140,y=550)
        dentry.insert(INSERT,difficulty)
        # The variable difficulty is inserted into this widget
        dentry["state"] = DISABLED
        # The user cannot edit this text widget

    elif returncount == 1:
    # This statement is true when the main game is running

        text1["state"] = NORMAL
        text2["state"] = NORMAL
        aentry["state"] = NORMAL
        # The NORMAL state allows the program to enter strings into the text boxes
        
        text1.delete("1.0",END)
        text2.delete("1.0",END)
        # Delete everything inside the text widgets
        
        text1.insert(INSERT,Callingwordlist.word) 
        text2.insert(INSERT,Callingwordlist.word2)
        # Insert relevant variables into the text widgets

        aentry.delete("1.0",END)
        aentry.insert(INSERT,accuracy)
        
        entry1.delete(0,END) 
        entry2.delete(0,END)
        # Delete everything inside the entry widgets

        # re-disable the text boxes to stop the user editing them
        text1["state"] = DISABLED
        text2["state"] = DISABLED
        aentry["state"] = DISABLED

        entry1.focus()
        # The first entry widget is focused on

# Results for the main game
       
class EndGameUI(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Type!")
        self.pack(fill=BOTH, expand=1)
        
        root.unbind("<Return>")
        
        style = Style()
        style.configure("TFrame", background="black")

        # The total score is calculated
        tscore = acc * words_per_minute
        # tscore multiplies the end accuracy by the number of words per minute
        global totalscore
        totalscore = tscore * difficulty
        # totalscore multiplies tscore by the difficulty

        Logo = Image.open("Type!.png")
        # This block of text opens an image and creates a frame 
        TypeLogo = ImageTk.PhotoImage(Logo)
        # The size of the image that the image is then placed into
        label1 = Label(self, image=TypeLogo)
        label1.image = TypeLogo
        label1.place(x=0,y=0)
        label1.pack()

        Ttext = Text(self,font=("Courier",28),width=29,height=1)
        # A text widget named Ttext is created
        Ttext.pack()
        Ttext.config(bg="black",fg="white",bd=0)
        Ttext.insert(INSERT,"Times up!")
        Ttext.place(x=540,y=50)
        Ttext["state"] = DISABLED # The user cannot edit this text widget

        Wtext = Text(self,font=("Courier",28),width=35,height=1)
        # A text widget named Wtext is created
        Wtext.pack()
        Wtext.config(bg="black",fg="white",bd=0)
        Wtext.insert(INSERT,"Number of correct words per minute:")
        Wtext.place(x=50,y=100)
        Wtext["state"] = DISABLED
        # The user cannot edit this text widget
        
        WPMtext = Text(self,font=("Courier",28),width=3,height=1)
        # A text widget named WPMtext is created
        WPMtext.pack()
        WPMtext.config(bg = "white", fg = "black" ,bd=0)
        WPMtext.insert(INSERT,words_per_minute)
        # The variable words_per_minute is inserted
        WPMtext.place(x=390,y=150)
        WPMtext["state"] = DISABLED
        # The user cannot edit this text widget

        TotText = Text(self,font=("Courier",28),height=1)
        # A text widget named TotText is created
        TotText.pack()
        TotText.config(bg="black",fg="white",bd=0)
        TotText.insert(INSERT,"Total score:")
        TotText.place(x=280, y=300)
        TotText["state"] = DISABLED
        # The user cannot edit this text widget

        TotalText = Text(self,font=("Courier",28),width = 5, height = 1)
        # A text widget named TotalText is created
        TotalText.pack()
        TotalText.config(bg="white",fg="black",bd=0)
        TotalText.insert(INSERT,totalscore)
        # The variable totalscore is inserted
        TotalText.place(x=380,y=350)
        TotalText["state"] = DISABLED
        # The user cannot edit this text widget

        Atext = Text(self,font=("Courier",28),height=1)
        # A text widget named Atext is created
        Atext.pack()
        Atext.config(bg="black",fg="white",bd = 0)
        Atext.insert(INSERT,"Total accuracy:")
        Atext.place(x=260,y=200)
        Atext["state"] = DISABLED
        # The user cannot edit this text widget

        Acctext = Text(self,font=("Courier",28),width = 3, height=1)
        # A text widget named Acctext is created
        Acctext.pack()
        Acctext.config(bg="white",fg="black",bd=0)
        Acctext.insert(INSERT,acc)
        # The variable acc is inserted
        Acctext.place(x=390,y=250)
        Acctext["state"] = DISABLED
        # The user cannot edit this text widget

        # A button called MainButton is created and calls the function returnmain when called
        MainButton = Button(self, text="Main Menu",command = lambda: returnmain(self))
        MainButton.pack()
        MainButton.place(x=660,y=500,height = 80,width = 100)
        
        # Surecount forces the user to press the submit button twice to confirm their choice
        global surecount
        surecount = 1

        global Ftext
        Ftext = Text(self,font =("Courier",18), height=1)
        # A text widget named Ftext is created
        Ftext.pack()
        Ftext.config(bg="black",fg="white",bd=0)
        Ftext.place(x=50,y=450)
        
        if guestuser == 0:
        # Stops the user submitting their score when logged in as a guest
            # A button named SubmitButton is created and calls the function submits when pressed
            SubmitButton = Button(self, text="Submit Score", command = lambda: submits(self,acc,words_per_minute,totalscore))
            SubmitButton.pack()
            SubmitButton.place(x=530,y=500,height=80,width=110)

# Submits the users score and shows error messages for erroneous data
def submits(self,acc,words_per_minute,totalscore): 
    global surecount
    # Checks for the global variable surecount instead of the local variable
    if surecount == 1:
    # This is true the first time the user presses the SubmitButton button
        surecount += 1
        Ftext.insert(INSERT,"Are you sure?(click again to continue)")
        Ftext["state"] = DISABLED
    elif surecount == 2:
    # This is true the second time the user presses the SubmitButton button
        SQLStatements.submitscore(UserName,acc,words_per_minute,totalscore,difficulty)
        if SQLStatements.online == 1:
            # Checks that the program is connected to the database
            Ftext["state"] = NORMAL
            # The Ftext widget state is changed so we can edit it
            Ftext.delete("1.0",END)
            # Everything inside the widget is deleted
            Ftext.insert(INSERT,"Cannot connect to database")
            #The error message is inserted
            Ftext["state"] = DISABLED
        else:
            if SQLStatements.scoreresults == 1:
            # Checks the variable scoreresults from the file SQLStatements
                Ftext["state"] = NORMAL
                # Allows us to enter a phrase 
                Ftext.delete("1.0",END)
                # Deletes everything inside the text widget
                Ftext.insert(INSERT,"Score lower than current highest score ("+SQLStatements.Enteredscore+")")
                # We enter a string including the variable Enteredscore from the file SQLStatements into the text widget
                Ftext["state"] = DISABLED
                # We re-disable the widget to stop the user from editing it
            else:
                self.destroy()
                app = ScoreGameUI(root)

# Results screen after score has been submitted

class ScoreGameUI(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Type!")
        self.pack(fill=BOTH, expand=1)
        
        root.unbind("<Return>")
        
        style = Style()
        style.configure("TFrame", background="black")

        Logo = Image.open("Type!.png")
        # This block of text opens an image and creates a frame 
        TypeLogo = ImageTk.PhotoImage(Logo)
        # The size of the image that the image is then placed into
        label1 = Label(self, image=TypeLogo)
        label1.image = TypeLogo
        label1.place(x=0,y=0)
        label1.pack()

        Sctext = Text(self,font=("Courier",18),width=35,height=1)
        # A text widget named Sctext is created
        Sctext.pack()
        Sctext.config(bg="black",fg="white",bd=0)
        Sctext.insert(INSERT,"Score submitted successfully!")
        Sctext.place(x=50,y=550)
        Sctext["state"] = DISABLED
        # The user cannot edit this text widget

        Ranktext = Text(self,font=("Courier",28),height=1)
        # A text widget named Ranktext is created
        Ranktext.pack()
        Ranktext.config(bg="black",fg="white",bd = 0)
        Ranktext.insert(INSERT,"Rank:")
        Ranktext.place(x=160,y=150)
        Ranktext["state"] = DISABLED
        # The user cannot edit this text widget

        RText = Text(self,font=("Courier",28),width = 3, height=1)
        # A text widget named Rtext is created
        RText.pack()
        RText.config(bg="white",fg="black",bd=0)
        RText.insert(INSERT,SQLStatements.results)
        # The variable results from the file SQLStatements is inserted
        RText.place(x=180,y=200)
        RText["state"] = DISABLED
        # The user cannot edit this text widget

        Scoretext = Text(self,font=("Courier",28),height = 1)
        # A text widget named Scoretext is created
        Scoretext.pack()
        Scoretext.config(bg="black",fg="white",bd=0)
        Scoretext.insert(INSERT,"Total score:")
        Scoretext.place(x=460,y=150)
        Scoretext["state"] = DISABLED
        # The user cannot edit this text widget

        Stext = Text(self,font=("Courier",28), width = 5, height=1)
        # A text widget named Stext is created
        Stext.pack()
        Stext.config(bg="white",bd=0)
        Stext.insert(INSERT,totalscore)
        # The variable totalscore is inserted
        Stext.place(x=530,y=200)
        Stext["state"] = DISABLED
        # The user cannot edit this text widget

        MainButton = Button(self, text="Main Menu",command = lambda: returnmain(self))
        # A button called MainButton is created and calls the function returnmain when pressed
        MainButton.pack()
        MainButton.place(x=660,y=500,height = 80,width = 100)

        Hightext = Text(self,font=("Courier",28),height=1)
        # A text widget named Hightext is created
        Hightext.pack()
        Hightext.config(bg="black",fg="white",bd = 0)
        Hightext.insert(INSERT,"Current user with highest score:")
        Hightext.place(x=60,y=300)
        Hightext["state"] = DISABLED
        # The user cannot edit this text widget

        # A text widget named Usertext is created
        Usertext = Text(self,font=("Courier",28),height=1,width = len(SQLStatements.highestuser))
        Usertext.pack()
        Usertext.config(bg="white",fg="black",bd = 0)
        Usertext.insert(INSERT,SQLStatements.highestuser)
        # The variable highestuser from the file SQLStatements is inserted
        Usertext.place(x=165,y=350)
        Usertext["state"] = DISABLED
        # The user cannot edit this text widget

        # A text widget named HStext is created
        HStext = Text(self,font=("Courier",28),height=1)
        HStext.pack()
        HStext.config(bg="black",fg="white",bd = 0)
        HStext.insert(INSERT,"With a score of:")
        HStext.place(x=60,y=400)
        HStext["state"] = DISABLED
        # The user cannot edit this text widget

        # A text widget named HScoretext is created
        HScoretext = Text(self,font=("Courier",28),height=1,width = len(SQLStatements.highestscore))
        HScoretext.pack()
        HScoretext.config(bg="white",fg="black",bd = 0)
        HScoretext.insert(INSERT,SQLStatements.highestscore)
        # The variable highestscore from the file SQLStatements is inserted
        HScoretext.place(x=165,y=450)
        HScoretext["state"] = DISABLED
        # The user cannot edit this text widget
    
# This function initiates the visual timer
def start_counter(label):
    counter = count(0)
    # Variable "counter" is created and set to 0
    def update_func():
        label.config(text=str(counter.next()))
        #Adds one to the counter and updates the label
        label.after(1000, update_func)
        # calls itself every second (1000 milliseconds)
    update_func()
    # Calls the function update_func

# Calculates the accuracy
def createscore(returncount,self,tempword,tempword2,eword,eword2,total,score,accuracy):
    if difficulty == 1:
    #If the difficulty is one, only one word is needed to be checked
        total += 1
        # The total is added even if the word is entered incorrectly
        if eword == tempword:
        # If the word entered is the same as the word on screen
            score = score + 1
            # We add one to the score
    else:
    # The algorithm for difficulty 2 and 3 are the same, so we only need an else statement
        if tempword2 == "":
        # Checks how many phrases need to be entered
            total += 1
            # If only one is needed to be entered, we only add one to the score
            if eword == tempword:
            # If the word entered is the same as the word on screen
                score += 1
                # We add one to the score
        else:
            total += 2
            # If two phrases are needed to be entered, we add two to the total
            if eword == tempword:
            # If the first word entered is the same as the first word on screen
                score += 1
                # We add one to the score
            if eword2 == tempword2:
            # If the second word entered is the same as the second word on screen
                score += 1
                # We add one to the score
    accuracy = (score*100/total*100)/100
    maininit(returncount,self,total,score,accuracy)

# Is called whenever the enter key is pressed on the main game            
def callback(self,event,total,score,accuracy): 
    tempword = Callingwordlist.word
    # Takes the first word to enter
    tempword2 = Callingwordlist.word2
    # Takes the second word to enter
    eword = entry1.get()
    # Takes the first word entered
    eword2 = entry2.get()
    # Takes the second word entered
    Callingwordlist.CallWordlist(difficulty)
    # Gets two new words to enter
    elapsed_time = time.time()-start_time
    # Updates the time elapsed
    returncount = 1
    # Tells the program that the game is running
    if elapsed_time < 60:
    # If the time is under 60 seconds we continue with the game
        createscore(returncount,self,tempword,tempword2,eword,eword2,total,score,accuracy)
        # Calls the funcion createscore
    elif elapsed_time >= 60:
    # If the time is over 60 seconds we end the game
        returncount = 2
        # tells the program that the time is up
        createscore(returncount,self,tempword,tempword2,eword,eword2,total,score,accuracy)
        # Calls the funcion createscore

if __name__ == '__main__':
    root = Tk()
    # Assigns variable 'root' to create a window
    root.geometry("860x440+200+50")
    # Sets the size and position of the window when created
    root.minsize(width = 860, height = 440)
    root.maxsize(width = 860, height = 440)
    # Stops the window from being resized
    app = LoginScreen(root)
    root.mainloop()
    #Creates a loop for the window 'root'
