## bank acc class with: name, acc number, balance, interest rate
## functions for __init__, adjust interest rate, withdraw/deposit, give balance, calculate interest based on given days
## __str__ method for displaying balances and interests
## test function to test the different methods
import time

class BankAcc:
    def __init__(self, name, accNum, balance, intRate):
        ## creates the values
        self.name = name
        self.accNum = accNum
        self.balance = balance
        self.intRate = intRate

    def addIntRate(self):
        ## adds to interest rate
        self.intRate += float(input("How much to add to Interest Rate?: "))

    def subIntRate(self):
        ## subtracts from interest rate
        self.intRate -= float(input("How much to subtract from Interest Rate?: "))

    def withdraw(self):
        ## subtracts from balance
        self.balance -= float(input("How much would you like to withdraw from your balance?: "))

    def deposit(self):
        ## adds to balance
        self.balance += float(input("How much would you like to add to the balance?: "))

    def displayBalance(self):
        ## returns the balance
        return self.balance

    def intCalc(self):
        ## get the number of days from user
        days = int(input("How many days do you want to calculate interest for?: "))
        print(f"The interest for {days} day(s) would be "
              ## P*R*T, rounded to 2 decimals
              f"{round((self.balance * self.intRate * days) * 100) / 100}")

    def __str__(self):
        ## returns the name, acc #, balance, and interest rate as a string
        return (f"Name: {self.name} || Acc #: {self.accNum} || Balance: {self.balance} || Interest Rate: {self.intRate}")


def main():

    inp = ()
    obj1 = BankAcc("Laios Touden", 1, 100, .0045)

    ## just so user can see what the values in obj1 are
    print(obj1.__str__())

    while inp != 8:
        print("Welcome to the test function! Select a method you would like to perform by entering a number"
              "\n1: Add Interest Rate"
              "\n2: Subtract Interest Rate"
              "\n3: Withdraw Money"
              "\n4: Deposit Money"
              "\n5: Display Balance"
              "\n6: Calculate Interest"
              "\n7: Display Values (the infamous __str__ method)"
              "\n8: Quit")

        inp = int(input())

        match inp:
            ## options to test each method
            case 1:
                obj1.addIntRate()
            case 2:
                obj1.subIntRate()
            case 3:
                obj1.withdraw()
            case 4:
                obj1.deposit()
            case 5:
                print(obj1.displayBalance())
            case 6:
                obj1.intCalc()
            case 7:
                print(obj1.__str__())
            case 8:
                print("Exiting now!")

        time.sleep(2.5)


if __name__ == "__main__":
    main()