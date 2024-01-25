
# This class will encapsulate the attributes & methods required to view and complete actions on a show/event
class Show:
    def __init__(self, title, date, time, adultTicketPrice, childTicketPrice, studentTicketPrice, seniorTicketPrice, numOfSoldTickets,
                 maxSeatsAllowedPerCustomer, promotionalShowEventStatus, showEventStatus):
        # Sets the attributes of the Show class
        self.title = title
        self.date = date
        self.time = time
        self.adultTicketPrice = adultTicketPrice
        self.childTicketPrice = childTicketPrice
        self.studentTicketPrice = studentTicketPrice
        self.seniorTicketPrice = seniorTicketPrice
        self.numOfSoldTickets = numOfSoldTickets
        self.maxSeatsAllowedPerCustomer = maxSeatsAllowedPerCustomer
        self.promotionalShowEventStatus = promotionalShowEventStatus
        self.showEventStatus = showEventStatus
        self.showEventSeatingChart = [['A' for i in range(5)] for i in range(5)]  # Provides the default value for seating chart

    def displayShowEventsInformation(self):
        # Output the information about the shows
        # Some information will be hidden depending on logged-in user's role
        print(f"Title: {self.title}")
        print(f"Date: {self.date}")
        print(f"Time: {self.time}")
        print(f"Adult Price: £{self.adultTicketPrice}")
        print(f"Child Price: £{self.childTicketPrice}")
        print(f"Student Price: £{self.studentTicketPrice}")
        print(f"Senior Citizen Price: £{self.seniorTicketPrice}")
        print(f"Tickets Sold: {self.numOfSoldTickets}")
        print(f"Max Seats Per Customer: {self.maxSeatsAllowedPerCustomer}")
        print(f"Promotion Status: {self.promotionalShowEventStatus}")
        print(f"Show Status: {self.showEventStatus}")

    def applyShowEventPromotion(self, showEventPromotionPercent):
        if not self.promotionalShowEventStatus: # Ensures it does not apply promotion twice if one already exisits.
            showEventPromotionAmount = showEventPromotionPercent / 100 # Calculates amount needed to be applied to the show/event
            #  Below applies the amount to the show/event by subtracting from old
            self.adultTicketPrice = self.adultTicketPrice - (self.adultTicketPrice * showEventPromotionAmount)
            self.childTicketPrice = self.childTicketPrice - (self.childTicketPrice * showEventPromotionAmount)
            self.studentTicketPrice = self.studentTicketPrice - (self.studentTicketPrice * showEventPromotionAmount)
            self.seniorTicketPrice = self.seniorTicketPrice - (self.seniorTicketPrice * showEventPromotionAmount)
            self.promotionalShowEventStatus = True # Updates promotion status
