from users import User # Imports User Class
from customer import Customer # Imports Customer Class
from venuemanager import VenueManager #Imports Venue Manager Class
from datetime import datetime # Imports Python Date & Time Module


class TicketAgent(User): # TicketAgent inherits the all the attributes  from User class
# This class will encapsulate all the functionality and attributes exclusive to the ticket agent
    def __init__(self, username, password, linkedCustomerName): #Used to intialize Ticket Agent objects
        super().__init__(username, password, "TicketAgent")
        # The name below will be used to 'link' ticket agent account to customer account
        self.linkedCustomerName = linkedCustomerName
        # The values here differ from customer, the ticket agent has a smaller set of rows
        # as it assumed these sets of seats are the ones assigned to the agent
        self.showEventSeatingChartRows = 3
        self.showEventSeatingChartColumns = 4


###  Below methods abstracts away the actual implementations
    def ticketAgentMainMenu(self, shows):
        # This will allow the ticket agent to choose what they would like to do in the ots (BCPA's Online Ticekting System)
        while True:
            print("1. View Shows")
            print("2. Exit")

            ticketAgentSelection = int(input("Select an option: "))

            if ticketAgentSelection == 1:
                self.ticketAgentMenuOptions(shows)
            elif ticketAgentSelection == 2:
                print("Exiting...")
                break
            else:
                print("Invalid selection. Please try again.")

    def ticketAgentMenuOptions(self, shows):
        print("1. View all upcoming shows/events")
        print("2. View shows from date range")

        ticketAgentSelection = int(input("Select an option: "))

        if ticketAgentSelection == 1:
            self.displayShowEventsByList(shows)
        elif ticketAgentSelection == 2:
            self.displayShowEventsByDateRange(shows)


    ### The below methods also use polymorphism as the method names are shared and exist in both the Ticket Agent class
    ### and the Customer class, but methods have slightly different funtionality methods unique to the class they are in.

    def displayShowEventsByList(self, shows):
        print("All Upcoming Shows/Events")
        for upcomingShow, show in enumerate(shows, start=1):
            # Differs to customer functionality by showing number of tickets sold
            print(f"{upcomingShow}. {show.title} {show.date} ({show.numOfSoldTickets} Tickets Sold)")

        displayTicketAgentSelection = int(input("Enter the number of the show you want to view, or Press '0' to go to main menu: "))
        if 1 <= displayTicketAgentSelection <= len(shows):
            selectedEventShow = shows[displayTicketAgentSelection - 1]
            self.displayShowEventsInformation(selectedEventShow)
        elif displayTicketAgentSelection == 0:
            return
        else:
            print("Invalid show number. Please try again.")
            self.displayShowEventsByList(shows)

    def displayShowEventsByDateRange(self, shows):
        showEventStartDateString = input("Enter show/event start date (DD/MM/YYYY): ")
        showEventEndDateString = input("Enter show/event end date (DD/MM/YYYY): ")

        # Convert the string input into a datatime object
        showEventStartDate = datetime.strptime(showEventStartDateString, "%d/%m/%Y")
        showEventEndDate = datetime.strptime(showEventEndDateString, "%d/%m/%Y")

        print(f"Show/Events from {showEventStartDateString} to {showEventEndDateString}")
        for dateSpecificShow, show in enumerate(shows, start=1):
            showEventStartDate = datetime.strptime(show.date, "%d/%m/%Y")
            if showEventStartDate <= showEventStartDate <= showEventEndDate:
                # This is an extension to the customer functionality
                # as this includes tickets sold in view
                print(f"{dateSpecificShow}. {show.title} {show.date} ({show.numOfSoldTickets} Tickets Sold)")

        displayTicketAgentSelection = int(input("Enter the number of the show you want to view, or Press '0' to go to main menu: "))

        if 1 <= displayTicketAgentSelection <= len(shows):
            selectedEventShow = shows[displayTicketAgentSelection - 1]
            self.displayShowEventsInformation(selectedEventShow)
        elif displayTicketAgentSelection == 0:
            return
        else:
            print("Invalid input. Please try again.")
            self.displayShowEventsByDateRange(shows)


    def displayShowEventsInformation(self, show):
        print("Show Details:")
        print(f"Title: {show.title}")
        print(f"Date: {show.date}")
        print(f"Time: {show.time}")
        print(f"Adult Price: £{show.adultTicketPrice}")
        print(f"Child Price: £{show.childTicketPrice}")
        print(f"Student Price: £{show.studentTicketPrice}")
        print(f"Senior Citizen Price: £{show.seniorTicketPrice}")
        print(f"Tickets Sold: {show.numOfSoldTickets}")
        self.ticketAgentSubMenu(show)

    def ticketAgentSubMenu(self, show):
        print("1. Go back to main menu")
        print("2. Book a ticket")

        ticketAgentSelection = int(input("Enter your Selection: "))

        if ticketAgentSelection == 1:
            return
        elif ticketAgentSelection == 2:
            self.ticketSelectionProcess(show)
        else:
            print("Invalid Selection. Please try again.")
            self.ticketAgentSubMenu(show)

    def ticketSelectionProcess(self, show):
        print(f"Selected Show: {show.title} - {show.date}")
        print("Select the number of tickets for each ticket type:")
        amountAdultShowEventTickets = int(input("Number of Adult tickets: "))
        amountChildrenShowEventTickets = int(input("Number of Child tickets: "))
        amountStudentsShowEventTickets = int(input("Number of Student tickets: "))
        amountSeniorsShowEventTickets = int(input("Number of Senior Citizen tickets: "))

        print("How would you like to choose your seats?")
        print("1. Interactive Selection")
        print("2. Automatic Selection")

        showEventSeatSelectionType = int(input("Enter your Selection: "))

        if showEventSeatSelectionType == 1:
            self. manualInteractiveSeatSelection(show, amountAdultShowEventTickets, amountChildrenShowEventTickets, amountStudentsShowEventTickets, amountSeniorsShowEventTickets)
        elif showEventSeatSelectionType == 2:
            self.otsAutomaticSeatSelection(show, amountAdultShowEventTickets + amountChildrenShowEventTickets + amountStudentsShowEventTickets + amountSeniorsShowEventTickets)
        else:
            print("Invalid Selection. Please try again.")
            self.ticketSelectionProcess(show)

    def  manualInteractiveSeatSelection(self, show, amountAdultShowEventTickets, amountChildrenShowEventTickets, amountStudentsShowEventTickets, amountSeniorsShowEventTickets):
        print("Interactive Seat Selection")

        # Using the smaller values given above, will create a chart of repeating 'A's
        # to indicate availiable seats
        showEventSeatingChart = [['A' for i in range(self.showEventSeatingChartColumns)] for i in range(self.showEventSeatingChartRows)]

        print("Available Seats:")
        self.displayManualInteractiveSeatingChart(showEventSeatingChart)

        # Below will hold the selected seats in a list to ensure ticket agent
        # cannot select the same seat twice
        ticketAgentSeatSelection = []

        # Below will add the number of selected seats per type to the list
        for i in range(amountAdultShowEventTickets):
            seat = self.specificInteractiveSeatSelection(showEventSeatingChart)
            ticketAgentSeatSelection.append((seat, 'Adult'))

        for i in range(amountChildrenShowEventTickets):
            seat = self.specificInteractiveSeatSelection(showEventSeatingChart)
            ticketAgentSeatSelection.append((seat, 'Child'))

        for i in range(amountStudentsShowEventTickets):
            seat = self.specificInteractiveSeatSelection(showEventSeatingChart)
            ticketAgentSeatSelection.append((seat, 'Student'))

        for i in range(amountSeniorsShowEventTickets):
            seat = self.specificInteractiveSeatSelection(showEventSeatingChart)
            ticketAgentSeatSelection.append((seat, 'Senior'))

        print("Your Selected Seats:")
        for seat, showEventTicketType in ticketAgentSeatSelection:
            print(f"Seat {seat} - {showEventTicketType} ticket")

        TicketAgentConfirm = input("Confirm your selection? (Y/N): ")
        ## The use off upper ensures the code does not crash if the input is in lowercase
        if TicketAgentConfirm.upper() == 'Y':
            self.otsPaymentProcess(show, ticketAgentSeatSelection)
        else:
            self. manualInteractiveSeatSelection(show, amountAdultShowEventTickets, amountChildrenShowEventTickets, amountStudentsShowEventTickets, amountSeniorsShowEventTickets)

    def specificInteractiveSeatSelection(self, showEventSeatingChart):
        # This will allow the ticket agent to select the desired seats
        seatingChartRow = int(input("Enter seat row number: ")) - 1
        seatingChartColumn = int(input("Enter seat column number: ")) - 1

        # Checks to ensure seats selected exist and are available
        if 0 <= seatingChartRow < len(showEventSeatingChart) and 0 <= seatingChartColumn < len(showEventSeatingChart[0]) and showEventSeatingChart[seatingChartRow][seatingChartColumn] == 'A':
            showEventSeatingChart[seatingChartRow][seatingChartColumn] = 'H'  # Marks the seat as held, so it cannot be selected again
            print("Seat selected successfully.")
            self.displayManualInteractiveSeatingChart(showEventSeatingChart)  # Displays the updated seating chart
            return f"{chr(seatingChartRow + 65)}{seatingChartColumn + 1}" # Returns the selected seats for Ticket Agent to confirm
        else:
            print("Invalid seat selection. Please try again.")
            return self.specificInteractiveSeatSelection(showEventSeatingChart)

    def displayManualInteractiveSeatingChart(self, showEventSeatingChart):
        # Below will loop through 3x rows and 4x columns to create the seating chart
        print("Seating Chart:")
        for seatingChartRow in showEventSeatingChart:
            print(' '.join(seatingChartRow))  # Will display the current seat status with  by a space to make it easier to read.

    def otsAutomaticSeatSelection(self, show, noSeatsRequired):
        print("Automatic Seat Selection")
        # This will use the same values as above for the seating chart (the smaller grid compared to customer)
        # To ensure that the automatic selection does not provide seats to the ticket agent that
        # are not assigned to them (outside the chart)
        showEventSeatingChart = [['A' for i in range(self.showEventSeatingChartColumns)] for i in range(self.showEventSeatingChartRows)]

        ticketAgentSeatSelection = self.specificInteractiveSeatSelectionsMatchingCriteria(showEventSeatingChart, noSeatsRequired)

        # Returns the selected seats so ticket agent can confirm selection
        print("Automatically Selected Seats:")
        for seat, showEventTicketType in ticketAgentSeatSelection:
            print(f"Seat {seat} ")

        TicketAgentConfirm = input("Confirm your seat selection? (Y/N): ")

        if TicketAgentConfirm.upper() == 'Y':
            self.otsPaymentProcess(show, ticketAgentSeatSelection)
        else:
            mainMenuPrompt = input("Do you want to go back to the previous screen? (Y/N): ")
            if mainMenuPrompt.upper() == 'Y':
                return
            else:
                self.otsAutomaticSeatSelection(show, noSeatsRequired)

    def specificInteractiveSeatSelectionsMatchingCriteria(self, showEventSeatingChart, noSeatsRequired):
        ticketAgentSeatSelection = []

        for i in range(noSeatsRequired):
            seatingChartRow, seatingChartColumn = self.manualInteractiveSeatsAllocation(showEventSeatingChart)
            ticketAgentSeatSelection.append((f"{chr(seatingChartRow + 65)}{seatingChartColumn + 1}", 'Adult')) #seats default seat type to Adult

        return ticketAgentSeatSelection

    def manualInteractiveSeatsAllocation(self, showEventSeatingChart):
        for seatingChartRow in range(len(showEventSeatingChart)):
            for seatingChartColumn in range(len(showEventSeatingChart[0])):
                if showEventSeatingChart[seatingChartRow][seatingChartColumn] == 'A': # Marks the seat as available, so it can be selected
                    showEventSeatingChart[seatingChartRow][seatingChartColumn] = 'H'  # Marks the seat as held, so it cannot be selected again
                    return seatingChartRow, seatingChartColumn

    def displayManualInteractiveSeatingChart(self, showEventSeatingChart):
        for seatingChartRow in showEventSeatingChart:
            print(' '.join(seatingChartRow)) # Will display the current seat status with  by a space to make it easier to read.

    def otsPaymentProcess(self, show, ticketAgentSeatSelection):
        totalTicketCost = self.otsSelectedTicketPrices(show, ticketAgentSeatSelection)
        print(f"Total Cost: £{totalTicketCost}")

        #This will ask specifically for customer details as the agent is buying on behalf of customer
        # Below uses casting to verify strings and ints are entered to 'validate' payment
        name = str(input("Enter your customer name: "))
        customerPaymentEmail = str(input("Enter your customer email: "))
        paymentCardLongNumber = int(input("Enter your credit card number: "))
        cvv = int(input("Enter your CVV: "))

        print(" ")  # Space for better readability
        # This will output ticket information with customer detials
        print("Payment Detials:")
        print(f"Name: {name}")
        print(f"Email: {customerPaymentEmail}")
        print(f"Show: {show.title} - {show.date} {show.time}")
        print(f"Total Cost: £{totalTicketCost}")
        print("Selected Seats:")
        for seat, showEventTicketType in ticketAgentSeatSelection:
            print(f"Seat {seat} - {showEventTicketType} ticket")

        TicketAgentConfirm = input("Confirm ticekt purchase? (Y/N): ")

        if TicketAgentConfirm.upper() == 'Y':
            print("Payment successful. Tickets Booked!")
        else:
            print("Booking canceled.")

    def otsSelectedTicketPrices(self, show, ticketAgentSeatSelection):
        otsShowEventTicketPrices = {
            'Adult': show.adultTicketPrice,
            'Child': show.childTicketPrice,
            'Student': show.studentTicketPrice,
            'Senior': show.seniorTicketPrice
        }

        totalTicketCost = sum(otsShowEventTicketPrices[showEventTicketType] for i, showEventTicketType in ticketAgentSeatSelection)
        return totalTicketCost

