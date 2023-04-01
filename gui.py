from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
root = tk.Tk()# Using Tkiner
root.geometry('350x350') # Size of the window
root.title("Password manager")#Name of the program
def frame1():
    def store():# This functions is used to create an account.
        found=False
        with open("username.txt", "r") as file:# Opens the txt file
            if file.read():#Determines if there is informaiton in the code.
                found=True
        if found:#If its found I tell the user there is an exisiting account 
            text.delete(1.0, END) 
            text.insert(END,"You already have an account added.")
        if not found:
            account = entry.get()
            password = entryPass.get()
            with open("username.txt", "a") as file: #Using with statement again
                file.write(f'{account} password is: {password}')# Stores the username and password into the txt file.
                text.delete(1.0, END) 
                text.insert(END,"The username and password has been added") #Lets the user know the password has been stored into the txt.
            return
    def loginnow():#This function logins in/switches to frame2/password maanger
        acc_account = entryPass.get() #The entries for username and password become variables
        password=entry.get()
        found = False
        with open("username.txt", "r") as file:#Open file is read
            for i in file:#Using for loop to verify
                if acc_account in i.split():#Split prevents it from logining in.
                    if password in i.split():#If the username and password is in the txt file.
                        frame2()#Then they are logged in. 
                    found = True    
            if not found:
                text.delete(1.0, END) 
                text.insert(END,"There are no accounts/password for this username") 
    def change_pass():#This function is to change the password
        password = entryPass.get()
        acc_account=entry.get()
        found = False
        with open("username.txt", "r") as file:
            for i in file:
                if acc_account in i.split():
                    if password in i.split(): #Making sure the account name and password are entered before resetting. 
                        with open("username.txt", "w") as file: 
                            file.write("")#Overwrites the txt file/clears it. 
                            text.delete(1.0, END) 
                            text.insert(END,"Your password has been reset")
                        found = True    
            if not found:
                text.delete(1.0, END) 
                text.insert(END,"There are no accounts/password added") 
    
    global frame1
    frame1=Frame(root)
    frame1.grid(row=0,column=0,sticky='nsew')#Noth south east and west(can appear anywhere in window)
    # Placing the object in frame1
    lb1=Label(frame1,text="Username:")
    lb1.grid(row=1,column=0)
    
    entry=Entry(frame1)
    entry.grid(row=1,column=1)
    
    lblPass=Label(frame1,text="Password:")
    lblPass.grid(row=2,column=0)
    
    entryPass=Entry(frame1,show="*")
    entryPass.grid(row=2,column=1)
    
    btnLogin1=Button(frame1,text="Login",command=loginnow,width=8)#Buttons that connect to functions.
    btnLogin1.grid(row=3,column=1,sticky=W)
    
    btnLogin2=Button(frame1,text="Register",command=store)
    btnLogin2.grid(row=3,column=1,sticky=E)
    
    label=Label(frame1,text="Entrys are above")
    label.grid(row=6,column=1)
    btnLogin3=Button(frame1,text="Reset password",command=change_pass)
    btnLogin3.grid(row=5,column=1,columnspan=1)    
    
    text=Text(frame1,height=4,width=27)
    text.grid(row=4,column=1)
    
    image = Image.open("work.png")
    photo = ImageTk.PhotoImage(image)
    la_bel = tk.Label(frame1, image=photo)
    la_bel.image = photo # Store a reference to the image to prevent garbage collection
    la_bel.grid(column=1,row=0)
    
def frame2():
    root.geometry('300x800')
    global frame2
    frame1.grid_remove()#hide frame 1
    def add_account():
        account_name = b1.get()#This makes the entry boxes into variables.
        password = b2.get()
        with open('passwords.txt', 'a') as file:
            file.write(f"Account password for {account_name} is: {password}\n-----------------------------------------\n") #Write in the list
            b3.insert(END,f"Account password for {account_name} has been added") # Print it in the text box
            return
    def view_accounts():
        b4.delete(1.0,END) #Only shows passwrod once. e.g. It does not print out the accounts if you press the button again
        found=False
        with open('passwords.txt', 'r') as file:
            lines = file.readlines()
            for i in lines:
                b4.insert(END, i) #Inserts the print into the entry box. 
                found=True
        if not found:
            b4.insert(END,"There are no passwords added.")
    def delate_account():# Delate account password function. 
        b4.delete(1.0, END) 
        with open("passwords.txt", "w") as file:
            file.write("")
        b4.insert(END,"Your account passwords have been cleared\n")
        
    def delate_account2(): # Clear list functions. 
        b4.delete(1.0, END)    
        b4.insert(END,"Your account passwords have been cleared\n")
        
    def retrieve_account():
        acc_account = b5.get()
        found = False
        with open("passwords.txt", "r") as file:
            for i in file:
                if acc_account in i.split():
                    b6.insert(END,i.split())
                    found = True    
            if not found:
                b6.insert(END,"There are no accounts/password added") 

    label = Label(root, text="Welcome to the password manager")
    label.pack()#Adding the labels

    label2 = Label(root, text="Please enter your account name")
    label2.pack()

    b1 = Entry(root,width=300)
    b1.pack() #Inserting an entry box. 

    label3 = Label(root, text="Please enter your account password:")
    label3.pack()

    b2 = Entry(root, show="*",width=300)
    b2.pack()

    button = Button(root, text="Add account", command=add_account)
    button.pack() #Insert a button
    b3 = Text(root,height=3)
    b3.pack()


    label4=Label(root,text="Enter your account name to retrive password:")
    label4.pack() #Inserting more labels
    b5=Entry(root,width=300)
    b5.pack()
    button3 = Button(root, text="Retrieve password", command=retrieve_account)
    button3.pack()
    b6=Text(root,height=3) #Insert more labels and button. 
    b6.pack()

    button2 = Button(root, text="View all accounts", command=view_accounts)
    button2.pack()
    b4 = Text(root)
    b4.pack()

    button4=Button(root,text="Clear list of password",command=delate_account2)
    button4.pack()
    button3=Button(root,text="Delate all account passoword",command=delate_account)
    button3.pack()
frame1()
root.mainloop()
#Lets the tkiner run. 