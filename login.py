from ticketagent import TicketAgent # Imports Ticket Agent Class
from users import User # Imports User Class



def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Checks to ensure account exists and assigns a role
    if username == "vmanager" and password == "password":
        print("Logged In, Hello Venue Manager!")
        return User(username, password, "VenueManager")
    elif username == "customer" and password == "password":
        print("Logged In, Hello Customer!")
        return User(username, password, "Customer")
    elif username == "tagent" and password == "password":
        linkedCustomerName = input("Customer Account Name: ")  #Used to 'Link' Ticket Agent Account to Customer
        print(f"Logged In, Hello Ticket Agent! ( Linked Customer -  {linkedCustomerName})")
        return TicketAgent(username, password, linkedCustomerName)
    else:
        print("Account Does Not Exist With Provided Credentials")
        print("Try Again")
        print("")
        login() #this will keep program running until valid login is provided



