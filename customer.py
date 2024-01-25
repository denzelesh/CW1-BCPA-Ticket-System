from show import Show #Imports Show Class
from users import User # Imports User Class
from datetime import datetime # Imports Python Date & Time Module


class Customer(User): # Customer inherits the all the attributes from User class
 # This class will encapsulate all the functionality and attributes exclusive to the customer

    def __init__(self, username, password): # Used to intialize customer objects
        super().__init__(username, password, "Customer")

###  Below methods abstract away the actual implementations

    def customerMainMenu(self, shows):
        # This will allow the customer to choose what they would like to do in the ticketing system
        while True:
            print("1. View Shows")
            print("2. Exit")

            CustomerSelection = int(input("Select an option: "))

            if CustomerSelection == 1:
                self.customerMenuOptions(shows)
            elif CustomerSelection == 2:
                print("Exiting...")
                break
            else:
                print("Invalid selection. Please try again.")

    def customerMenuOptions(self, shows):
        # This will allow the customer to choose how they would like to view shows
        print("1. View all upcoming shows/events")
        print("2. View shows/events from date range")

        CustomerSelection = int(input("Select an option: "))

        if CustomerSelection == 1:
            self.displayShowEventsByList(shows)
        elif CustomerSelection == 2:
            self.displayShowEventsByDateRange(shows)

    def displayShowEventsByList(self, shows):
        print("All Upcoming Shows/Events")
        for upcomingShow, show in enumerate(shows, start=1):
            print(f"{upcomingShow}. {show.title} {show.date}")

        displayCustomerSelection = int(input("Enter the number of the show you want to view, or Press '0' to go to main menu: "))
        if 1 <= displayCustomerSelection <= len(shows):
            selectedEventShow = shows[displayCustomerSelection - 1]
            self.displayShowEventsInformation(selectedEventShow)
        elif displayCustomerSelection == 0:
            return
        else:
            print("Invalid show number. Please try again.")
            self.displayShowEventsByList(shows)

    def displayShowEventsByDateRange(self, shows):
        showEventStartDateString = input("Enter show/event start date (DD/MM/YYYY): ")
        showEventEndDateString = input("Enter show/event end date (DD/MM/YYYY): ")

        showEventStartDate = datetime.strptime(showEventStartDateString, "%d/%m/%Y")
        showEventEndDate = datetime.strptime(showEventEndDateString, "%d/%m/%Y")

        print(f"Show/Events from {showEventStartDateString} to {showEventEndDateString}")
        for dateSpecifcShow, show in enumerate(shows, start=1):
            showEventDate = datetime.strptime(show.date, "%d/%m/%Y")
            if showEventStartDate <= showEventDate <= showEventEndDate:
                print(f"{dateSpecifcShow}. {show.title} {show.date}")

        displayCustomerSelection = int(input("Enter the number of the show you want to view, or Press '0' to go to main menu: "))

        if 1 <= displayCustomerSelection <= len(shows):
            selectedEventShow = shows[displayCustomerSelection - 1]
            self.displayShowEventsInformation(selectedEventShow)
        elif displayCustomerSelection == 0:
            return
        else:
            print("Invali input. Please try again.")
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
        self.CustomerSubMenu(show)

    def CustomerSubMenu(self, show):
        print("1. Go back to main menu")
        print("2. Book a ticket")

        CustomerSelection = int(input("Enter your Selection: "))

        if CustomerSelection == 1:
            return
        elif CustomerSelection == 2:
            self.ticketSelectionProcess(show)
        else:
            print("Invalid Selection. Please try again.")
            self.CustomerSubMenu(show)

    def ticketSelectionProcess(self, show):
        print(f"Selected Show: {show.title} - {show.date}")
        print("Enter the number of tickets for each ticket type:")
        amountAdultShowEventTickets = int(input("Number of Adult tickets: "))
        amountChildrenShowEventTickets = int(input("Number of Child tickets: "))
        amountStudentsShowEventTickets = int(input("Number of Student tickets: "))
        amountSeniorsShowEventTickets = int(input("Number of Senior Citizen tickets: "))

        print("How would you like to choose your seats?")
        print("1. Interactive Selection")
        print("2. Automatic Selection")

        showEventSeatSelectionType = int(input("Enter your Selection: "))

        if showEventSeatSelectionType == 1:
            self.manualInteractiveSeatSelection(show, amountAdultShowEventTickets, amountChildrenShowEventTickets, amountStudentsShowEventTickets, amountSeniorsShowEventTickets)
        elif showEventSeatSelectionType == 2:
            self.otsAutomaticSeatSelection(show, amountAdultShowEventTickets + amountChildrenShowEventTickets + amountStudentsShowEventTickets + amountSeniorsShowEventTickets)
        else:
            print("Invalid Selection. Please try again.")
            self.ticketSelectionProcess(show)

    def manualInteractiveSeatSelection(self, show, amountAdultShowEventTickets, amountChildrenShowEventTickets, amountStudentsShowEventTickets, amountSeniorsShowEventTickets):
        print("Interactive Seat Selection")

        # This will create a 5x5 seating chart of repeating 'A's to indicate available seats
        showEventSeatingChart = [['A' for i in range(5)] for i in range(5)]

        print("Available Seats:")
        self.displayManualInteractiveSeatingChart(showEventSeatingChart)

        # Below will hold the selected seats in a list to ensure customer
        # cannot select the same seat twice
        CustomerSeatSelection = []

        # Below will add the number of selected seats per type to the list
        for i in range(amountAdultShowEventTickets):
            seat = self.specificInteractiveSeatSelection(showEventSeatingChart)
            CustomerSeatSelection.append((seat, 'Adult'))

        for i in range(amountChildrenShowEventTickets):
            seat = self.specificInteractiveSeatSelection(showEventSeatingChart)
            CustomerSeatSelection.append((seat, 'Child'))

        for i in range(amountStudentsShowEventTickets):
            seat = self.specificInteractiveSeatSelection(showEventSeatingChart)
            CustomerSeatSelection.append((seat, 'Student'))

        for i in range(amountSeniorsShowEventTickets):
            seat = self.specificInteractiveSeatSelection(showEventSeatingChart)
            CustomerSeatSelection.append((seat, 'Senior'))

        print("Your Selected Seats:")
        for seat, showEventTicketType in CustomerSeatSelection:
            print(f"Seat {seat} - {showEventTicketType} ticket")

        CustomerConfirm = input("Confirm your seat selection? (Y/N): ")

        if CustomerConfirm.upper() == 'Y':
            self.otsPaymentProcess(show, CustomerSeatSelection)
        else:
            self.manualInteractiveSeatSelection(show, amountAdultShowEventTickets, amountChildrenShowEventTickets, amountStudentsShowEventTickets, amountSeniorsShowEventTickets)

    def specificInteractiveSeatSelection(self, showEventSeatingChart):
        # This will allow the customer to select the desired seats
        seatingChartRow = int(input("Enter seat row number: ")) - 1
        seatingChartColumn = int(input("Enter seat column number: ")) - 1

        # Checks to ensure seats selected exist and are available
        if 0 <= seatingChartRow < len(showEventSeatingChart) and 0 <= seatingChartColumn < len(showEventSeatingChart[0]) and showEventSeatingChart[seatingChartRow][seatingChartColumn] == 'A':
            showEventSeatingChart[seatingChartRow][seatingChartColumn] = 'H'   # Marks the seat as held, so it cannot be selected again
            print("Seat successfully selected.")
            self.displayManualInteractiveSeatingChart(showEventSeatingChart) # Displays the updated seating chart
            return f"{chr(seatingChartRow + 65)}{seatingChartColumn + 1}"  # Returns the selected seats for customer to confirm
        else:
            print("Invalid seat selection. Please try again.")
            return self.specificInteractiveSeatSelection(showEventSeatingChart)

    def displayManualInteractiveSeatingChart(self, showEventSeatingChart):
        print("Seating Chart:")
        for seatingChartRow in showEventSeatingChart:
            print(' '.join(seatingChartRow)) # Will display the current seat status with  by a space to make it easier to read.

    def otsAutomaticSeatSelection(self, show, numberOfSeats):
        print("Automatic Seat Selection")

        # Uses the same values as above to ensure it does not provide seats outside the range of the seat chart
        showEventSeatingChart = [['A' for i in range(5)] for i in range(5)]

        CustomerSeatSelection = self.specificInteractiveSeatSelectionsMatchingCriteria(showEventSeatingChart, numberOfSeats)

        # Returns the selected seats so customer can confirm selection
        print("Selected Seats:")
        for seat, showEventTicketType in CustomerSeatSelection:
            print(f"Seat {seat} - {showEventTicketType} ticket")

        CustomerConfirm = input("Confirm your seat selection? (Y/N): ")

        if CustomerConfirm.upper() == 'Y':
            self.otsPaymentProcess(show, CustomerSeatSelection)
        else:
            mainMenuPrompt = input("Do you want to go back to the main menu? (Y/N): ")
            if mainMenuPrompt.upper() == 'Y':
                return
            else:
                self.otsAutomaticSeatSelection(show, numberOfSeats)


    def specificInteractiveSeatSelectionsMatchingCriteria(self, showEventSeatingChart, numberOfSeats):
        CustomerSeatSelection = []

        for i in range(numberOfSeats):
            seatingChartRow, seatingChartColumn = self.manualInteractiveSeatsAllocation(showEventSeatingChart)
            CustomerSeatSelection.append((f"{chr(seatingChartRow + 65)}{seatingChartColumn + 1}", 'Adult')) #sets default seat type to Adult
        return CustomerSeatSelection

    def manualInteractiveSeatsAllocation(self, showEventSeatingChart):
        for seatingChartRow in range(len(showEventSeatingChart)):
            for seatingChartColumn in range(len(showEventSeatingChart[0])):
                if showEventSeatingChart[seatingChartRow][seatingChartColumn] == 'A': # Marks the seat as available, so it can be selected
                    showEventSeatingChart[seatingChartRow][seatingChartColumn] = 'H'  # Marks the seat as held, so it cannot be selected again
                    return seatingChartRow, seatingChartColumn

    def displayManualInteractiveSeatingChart(self, showEventSeatingChart):
        # Below will loop through each row in the seating chart
        for seatingChartRow in showEventSeatingChart:
            print(' '.join(seatingChartRow)) # Will display the current seat status with  by a space to make it easier to read.

    def otsPaymentProcess(self, show, CustomerSeatSelection):
        # This will ask customer for details required to purchase ticket
        # Below uses casting to verify strings and ints are entered to 'validate' payment
        totalTicketCost = self.otsSelectedTicketPrices(show, CustomerSeatSelection)
        print(f"Total Cost: £{totalTicketCost}")
        name = str(input("Enter your name: "))
        customerPaymentEmail = str(input("Enter your email: "))
        paymentCardLongNumber = int(input("Enter your credit card number: "))
        cvv = int(input("Enter your CVV: "))

        print(" ") #Space for better readability
		# This will output customer ticket information
        print("Payment Detials:")
        print(f"Name: {name}")
        print(f"Email: {customerPaymentEmail}")
        print(f"Show: {show.title} - {show.date} {show.time}")
        print(f"Total Cost: £{totalTicketCost}")
        print("Selected Seats:")
        for seat, showEventTicketType in CustomerSeatSelection:
            print(f"Seat {seat} - {showEventTicketType} ticket")

        CustomerConfirm = input("Confirm ticket purchase? (Y/N): ")

        if CustomerConfirm.upper() == 'Y':
            print("Payment successful. Tickets Booked!")
        else:
            print("Booking canceled.")

    def otsSelectedTicketPrices(self, show, CustomerSeatSelection):
        otsShowEventTicketPrices = {
            'Adult': show.adultTicketPrice,
            'Child': show.childTicketPrice,
            'Student': show.studentTicketPrice,
            'Senior': show.seniorTicketPrice
        }

        totalTicketCost = sum(otsShowEventTicketPrices[showEventTicketType] for i, showEventTicketType in CustomerSeatSelection)
        return totalTicketCost

