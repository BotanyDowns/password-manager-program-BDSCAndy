def retrieve_account(): # Retrieve password function
    acc_account = input("Enter the account: ") #Ask for user input
    found = False #Found passowrd=false
    with open("passwords.txt", "r") as file: # This makes the password txt file if it does not exisist.
        work=open("passwords.txt", "r") # Opens the password txt file. 
        for i in work: #Using for loop to print the password for the account
            i2=i.split()
            if acc_account in i2:
                print(i)
                found = True                 
        if not found:#If there are not passwords for account name that message is print. 
            print("There are no passwords added for this account")
def add_account():# Adds account function
    ac_account = input("Add your account name: ") # Ask for account name and password
    password = input("Enter your password: ")
    with open('passwords.txt', 'a') as file:# Makes the txt file if it does not exisit.
        file.write(f'Account password for {ac_account} is: {password}\n') # Write in the txt file.
        file.write("------------------------------------------------------------------------\n")
    return
def view_accounts(): 
    found=False
    with open('passwords.txt','r') as file: # Using forloop to print everything in txt.
        for i in file:
            print(i)
            found=True
    if not found:
        print("There are no passwords added")
def delate_account(): # This  function clears everything on the list
    r=input("Are you sure you want to clear all data? y/n: ")
    if r=="y":
        with open("passwords.txt", "w") as file:
            file.write("") #Using file.write
        print("all your accounts & passwords have been cleared")
    elif r=="n":
        print("")
    else:
        print("Please enter y/n")
def main():# Using a while loop to make user enter the choices given and adding the functons under each if statement.
    name=input("Welcome to the password manager. Before you can access your account/passwords please state your full name: ")
    while name !="0":
        question = input(f"Welcome {name} to your password manager. Please enter a choice from the options below:\n1. Add account/password\n2. View all passwords\n3. Retrieve password\n4. Clear all data\n5. logout\n:")
        if question=="1":
            add_account()
            print("adding password.....\npassword has been added!")
        elif question=="2":
                view_accounts()
        elif question=="3":
                retrieve_account()
        elif question=="4":
            delate_account()
        elif question=="5":
            break
        else:
            print("Please enter the number/choices given to you:")
main()
   
