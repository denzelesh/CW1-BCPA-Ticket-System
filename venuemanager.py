from show import Show # Imports Shows Class
from datetime import datetime # Imports Python Date & Time Module

class VenueManager():
# This class will encapsulate all the functionality and attributes exclusive to the Venue Manager
    def __init__(self, shows): # Used to intialise Venue Manager objects
        super().__init__()
        self.shows = shows
        self.showEventPromotions = []

#####  Below methods abstract away the actual implementations

    def venueManagerMainMenu(self):
        # This will allow the venue manager  to choose what they would like to do in the system
        while True:
            print("1. View Shows")
            print("2. Create New Shows")
            print("3. Manage Promotions")
            print("4. Exit")

            venueManagerSelection = int(input("Select an option: "))

            if venueManagerSelection == 1:
                self.venueManagerMenuOptions()
            elif venueManagerSelection == 2:
                self.createNewShowEvent()
            elif venueManagerSelection == 3:
                self.manageShowEventPromotions()
            elif venueManagerSelection == 4:
                print("Exiting...")
                break
            else:
                print("Invalid selection. Please try again.")

    def venueManagerMenuOptions(self): # Below lets the venue manager decide how they want to view shows/events
        print("1. View all upcoming shows/events")
        print("2. View shows/events from date range")

        venueManagerSelection = int(input("Select an option: "))

        if venueManagerSelection == 1:
            self.displayShowEventsByList()
        elif venueManagerSelection == 2:
            showEventStartDate = input("Enter show/event start date (DD/MM/YYYY): ")
            showEventEndDate = input("Enter show/event end date (DD/MM/YYYY): ")
            self.displayShowEventsByDateRange(showEventStartDate, showEventEndDate)

    def displayShowEventsByList(self):
        print("All Upcoming Shows")
        for upcomingShow, show in enumerate(self.shows, start=1):
            # also shows tickets sold in list , this is not found in customer class
            print(f"{upcomingShow}. {show.title} {show.date} ({show.numOfSoldTickets} Tickets Sold)")

        venueManagerShowSelection = int(input("Enter the number of the show you want to select: "))
        if 1 <= venueManagerShowSelection <= len(self.shows):
            venueManagerSelectedShow = self.shows[venueManagerShowSelection - 1]
            self.displayShowEventsInformation(venueManagerSelectedShow)

        # Convert the string input into a datatime object
    def displayShowEventsByDateRange(self, showEventStartDateString, showEventEndDateString):
        showEventStartDate = datetime.strptime(showEventStartDateString, "%d/%m/%Y")
        showEventEndDate = datetime.strptime(showEventEndDateString, "%d/%m/%Y")

        print(f"Show/Events from {showEventStartDateString} to {showEventEndDateString}")
        for dateSpecificShow, show in enumerate(self.shows, start=1):
            showEventDate = datetime.strptime(show.date, "%d/%m/%Y")
            if showEventStartDate <= showEventDate <= showEventEndDate:
                print(f"{dateSpecificShow}. {show.title} {show.date} ({show.numOfSoldTickets} Tickets Sold)")

        venueManagerShowSelection = input("Enter the number of the show you want to view, or ‘0’ to go to main menu: ")

        if venueManagerShowSelection == 0:
            self.venueManagerMainMenu()
        elif venueManagerShowSelection.isdigit():
            venueManagerShowSelection = int(venueManagerShowSelection)
            if 1 <= venueManagerShowSelection <= len(self.shows):
                venueManagerSelectedShow = self.shows[venueManagerShowSelection - 1]
                self.displayShowEventsInformation(venueManagerSelectedShow)
            else:
                print("Invalid input. Please try again.")
                self.displayShowEventsByDateRange(showEventStartDateString, showEventEndDateString)
        else:
            print("Invalid input. Please enter a number or 0 to go main menu.")
            self.displayShowEventsByDateRange(showEventStartDateString, showEventEndDateString)

    def displayShowEventsInformation(self, show):
        print("Show Details:")
        show.displayShowEventsInformation()
        editVenueManagerSelection = input("Do you want to edit this show? (Y/N): ")
        if editVenueManagerSelection.upper() == 'Y': # this will prevent code from crashing if the input is lowercase
            self.editShowEventsInformation(show)
        mainMenuPrompt = input("Do you want to go back to main menu? (Y/N): ")
        if mainMenuPrompt.upper() != 'Y':
            self.venueManagerMainMenu()


    def createNewShowEvent(self):
        # Below will allow the venue manager to provide the required information to create a new show/event
        title = input("Enter show title: ")
        date = input("Enter show date (DD/MM/YYYY): ")
        time = input("Enter show time (HH:MM): ")
        adultTicketPrice = float(input("Enter adult ticket price: "))
        childTicketPrice = float(input("Enter child ticket price: "))
        studentTicketPrice = float(input("Enter student ticket price: "))
        seniorTicketPrice = float(input("Enter senior citizen ticket price: "))
        numOfSoldTickets = int(input("Enter number of tickets sold: "))
        maxSeatsAllowedPerCustomer = int(input("Enter maximum seats per customer: "))
        promotionalShowEventStatus = False # By defaut all shows will have to have promotions applied to them seperatley after creation
        showEventStatus = input("Enter show status (Scheduled/Cancelled): ")

        newShowEvent = Show(title, date, time, adultTicketPrice, childTicketPrice, studentTicketPrice, seniorTicketPrice,
                        numOfSoldTickets, maxSeatsAllowedPerCustomer, promotionalShowEventStatus, showEventStatus)
        self.shows.append(newShowEvent)

        print("New show/event created successfully.")
        self.venueManagerMainMenu()


    def editShowEventsInformation(self, show):
        # Below will allow venue manager to make changes to  a selected show by overwriting the values
        print("Editing Show Details:")
        show.title = input(f"Enter new title (current: {show.title}): ")
        show.date = input(f"Enter new date (current: {show.date}): ")
        show.time = input(f"Enter new time (current: {show.time}): ")
        show.adultTicketPrice = float(input(f"Enter new adult ticket price (current: {show.adultTicketPrice}): "))
        show.childTicketPrice = float(input(f"Enter new child ticket price (current: {show.childTicketPrice}): "))
        show.studentTicketPrice = float(input(f"Enter new student ticket price (current: {show.studentTicketPrice}): "))
        show.seniorTicketPrice = float(input(f"Enter new senior citizen ticket price (current: {show.seniorTicketPrice}): "))
        show.numOfSoldTickets = int(input(f"Enter new number of tickets sold (current: {show.numOfSoldTickets}): "))
        show.maxSeatsAllowedPerCustomer = int(
            input(f"Enter new maximum amount of seats per customer (current: {show.maxSeatsAllowedPerCustomer}): "))
        show.showEventStatus = input(f"Enter new show status (Scheduled/Cancelled) (current: {show.showEventStatus}): ")

        print("Show details updated successfully.")

    def manageShowEventPromotions(self):
        print("1. Create a new promotion")
        print("2. Apply existing promotion to shows")

        venueManagerSelection = int(input("Enter your Selection: "))

        if venueManagerSelection == 1:
            self.createNewShowEventPromotions()
        elif venueManagerSelection == 2:
            self.applyShowEventPromotion()

    def createNewShowEventPromotions(self):
        showEventPromotionName = input("Enter promotion name: ")
        showEventPromotionPercent = float(input("Enter promotion percentage (e.g., 25 for 25%): "))
        venueManagerConfirm = input(f"Create a new promotion '{showEventPromotionName}' with {showEventPromotionPercent}%? (Y/N): ")

        if venueManagerConfirm.upper() == 'Y':
            self.showEventPromotions.append({"name": showEventPromotionName, "percent": showEventPromotionPercent})
            print("Promotion created successfully.")
        else:
            print("Promotion creation canceled.")

        mainMenuPrompt = input("Do you want to go back to the main menu? (Y/N): ")
        if mainMenuPrompt.upper() != 'Y':
            self.manageShowEventPromotions()

    def applyShowEventPromotion(self):
        if not self.showEventPromotions:
            print("No promotions available.")
            return

        print(" ") #spaces for readability
        print("All Upcoming Shows")
        for upcomingShow, show in enumerate(self.shows, start=1):
            print(f"{upcomingShow}. {show.title} {show.date} ({show.numOfSoldTickets} Tickets Sold)")

        print(" ") #spaces for readability
        print("Available Promotions:")
        for availablePromos, promotion in enumerate(self.showEventPromotions, start=1):
            print(f"{availablePromos}. {promotion['name']} - {promotion['percent']}%")

        venueManagerShowSelection = int(input("Select a show to apply promotion to (enter show number): "))
        showEventPromotionvenueManagerSelection = int(input("Select a promotion to apply (enter promotion number): "))

        # Below ensures valid selections have been made before proceeding to make changes
        if 1 <= venueManagerShowSelection <= len(self.shows) and 1 <= showEventPromotionvenueManagerSelection <= len(self.showEventPromotions):
            venueManagerSelectedShow = self.shows[venueManagerShowSelection - 1]
            venueManagerSelectedPromotion = self.showEventPromotions[showEventPromotionvenueManagerSelection - 1]

            venueManagerSelectedShow.applyShowEventPromotion(venueManagerSelectedPromotion['percent'])

            print(f"Promotion '{venueManagerSelectedPromotion['name']}' ({venueManagerSelectedPromotion['percent']}%) applied to show/event '{venueManagerSelectedShow.title}'.")
            self.displayShowEventsInformation(venueManagerSelectedShow)
        else:
            print("Invalid show or promotion selection. Please try again.")

