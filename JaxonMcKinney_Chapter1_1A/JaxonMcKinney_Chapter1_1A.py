# Pre-Selling 20 tickets with a max of 4 per person
MAXORDER = int(4)                        # max amount of tickets one may order at a time
STARTINGTICKETS = int(20)                # amount of tickets at start of program

def main():

    # define variables/constants
    global ticketsRemaining
    ticketsRemaining = int(STARTINGTICKETS)  # amount of tickets left
    ticketOrder = int()                      # amount of tickets ordered at a time
    totalBuyers = int(0)                     # amount of buyers/how many times loop has run


    while ticketsRemaining > 0:

        print(f"There are {ticketsRemaining} tickets remaining.")

        try:
            ticketOrder = int(input(f"How many tickets would you like to order? (Max: 4)\n"))

        # checks for if input is not integer
        except ValueError:
            print("Please input an integer")

        # checks if order is valid
        if checkTicketOrder(ticketOrder) == True:
            print("Invalid order!")

        # removes order from total tickets
        else:
            ticketsRemaining -= ticketOrder
            totalBuyers += 1

    print(f"We are out of tickets! There were {totalBuyers} total buyers!")

def checkTicketOrder(ticketOrder):
    return ticketOrder > MAXORDER or ticketOrder > ticketsRemaining or ticketOrder < 0


if __name__ == "__main__":
    main()