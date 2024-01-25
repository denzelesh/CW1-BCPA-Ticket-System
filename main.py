from ticketagent import TicketAgent # Imports Ticket Agent Class
from customer import Customer # Imports Customer Class
from venuemanager import VenueManager  # Imports Venue Manager Class
from show import Show  # Imports the Show Class
from login import login # Imports login method

def main():
    shows = [ #Name  #Date   #Time   #Adult  #Child  #Student  #Senior #MaxSeatsPerCustomer, #Promotion Status #Show Status
        Show("Toy Adventure", "25/07/2023", "14:15", 26, 14, 17, 8, 34, 5, False, "Scheduled"),
        Show("Melted 2", "12/03/2023", "17:00", 21, 12, 14, 9, 24, 6, False, "Scheduled"),
        Show("The Unbalancer", "11/01/2023", "12:30", 26, 14, 17, 5, 22, 5, False, "Scheduled")
    ]

    user = login()

    if user:
        if user.role == "VenueManager":
            loggedInVenueManager = VenueManager(shows)  # Provides the list of shows to the Venue Manager
                                                    # Passed to class so promotions can be applied to shows
            loggedInVenueManager.venueManagerMainMenu()
        elif user.role == "Customer":
            loggedInCustomer = Customer(user.username, user.password)
            loggedInCustomer.customerMainMenu(shows) # Provides the list of shows to the Customer
        elif user.role == "TicketAgent":
            loggedInTicketAgent = TicketAgent(user.username, user.password, "Linked Customer Name")  # Update with the actual customer name
            loggedInTicketAgent.ticketAgentMainMenu(shows)  # Provides the list of shows to the Ticket Agent


main() # This will start the program