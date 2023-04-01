#Creates a dictionery
passwords = {}

# This function stores the account passowrd into the dictionery. 
def add_password(account, password):
    passwords[account] = password

# This function retrieves the password for a given account from the passwords dictionary
def get_password(account):
    return passwords.get(account, None)

# Function that runs the program. 
def main():
    name=input("Please state your name:")
    #Gives the uesr to select 3 choices
    while name !="0":#Using a while loop to input the choices. 
        print("1. Add password")
        print("2. Get password")
        print("3. Exit")
        # Get the user's choice
        choice = input(": ")
        if choice == "1": 
            account = input("Enter account name: ")# ask user for account name/passoword
            password = input("Enter your password: ")
            add_password(account, password)  # Stores the password into the dictionery
        elif choice == "2":
            account = input("Enter your account name: ")
            password = get_password(account) 
            if password:
                print(f"Password for {account}: {password}")
            else:
                print(f"No password found for {account}.")
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
        #if user enters anything other then 1,2,3 they have to enter again. 
main()
