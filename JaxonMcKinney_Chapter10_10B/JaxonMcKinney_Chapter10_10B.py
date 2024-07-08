## apply Money class to the BankAcc class from previous week assignment
from decimal import Decimal
import re


class Money(Decimal):

    default_curr = 'USD'

    ## exchange rates pulled from the book
    exch_dict = {
        'USDCAD': Decimal('0.75'), 'CADUSD': Decimal('1.33'),
        'USDEUR': Decimal('1.16'), 'EURUSD': Decimal('0.86'),
        'EURCAD': Decimal('0.65'), 'CADEUR': Decimal('1.54')
    }

    def __new__(cls, v, units=''):
        return super(Money, cls).__new__(cls, v)

    def __init__(self, v, units=''):
        if not units:
            self.units = Money.default_curr
        else:
            self.units = units
        self.v = Decimal(v)

    def __str__(self):
        s = str(self.v) + ' ' + self.units
        return s

    def __repr__(self):
        s = 'Money(' + str(self.v) + ', ' + self.units + ')'
        return s

    def __add__(self, other):
        if self.units != other.units:
            r = Money.exch_dict[self.units + other.units]
            m = str(round(self.v + (other.v * r), 2))
        else:
            m = str(round(self.v + other.v, 2))
        return m

    def __sub__(self, other):
        if self.units != other.units:
            r = Money.exch_dict[self.units + other.units]
            m = str(round(self.v - (other.v * r), 2))
        else:
            m = str(round(self.v - other.v, 2))
        return m

    def __mul__(self, other):
        if self.units != other.units:
            r = Money.exch_dict[self.units + other.units]
            m = str(round(self.v * (other.v * r), 2))
        else:
            m = str(round(self.v * other.v, 2))
        return m


class BankAcc(Money):

    def __new__(cls, v, units='', name='', accNum=(), intRate=()):
        return super(BankAcc, cls).__new__(cls, v)

    def __init__(self, v, units='', name='', accNum=int(), intRate=float()):
        super().__init__(v, units)
        self.name = name
        self.accNum = accNum
        self.intRate = intRate

    def __str__(self):
        return (f'Name: {self.name} || Acc #: {self.accNum} || '
                f'Balance: {self.v} {self.units} || Interest Rate: {self.intRate}')

    def addIntRate(self, num):
        """Adding interest rates."""

        self.intRate += num

    def subIntRate(self, num):
        """Subtracting interest rates."""

        self.intRate -= num

    def displayBalance(self):
        """Displaying the balance (v) variable."""

        return f'Balance: {self.v} {self.units}'

    def intCalc(self, days):
        """Calculating the interest of (days) days."""

        return (f'The interest for {days} days would be: '
                f'{round((self.v * Decimal(self.intRate) * days) * 100) / 100}')


def main():
    pat = re.compile(r'\d\.\d\d')
    inp = ()
    obj1 = BankAcc('100', 'USD', 'Laios Touden', 1, .0045)
    val = ''
    unit = ''
    days = ''

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
                ## add interest rate
                obj1.addIntRate(float(input('How much would you like to add to the interest rate?: ')))
            case 2:
                ## subtract interest rate
                obj1.subIntRate(float(input('How much would you like to subtract from the interest rate?: ')))
            case 3:
                ## withdraw
                while True:
                    ## get the value correctly formatted
                    val = input('What value would you like to withdraw? (#.##): ')
                    val.strip()
                    if pat.fullmatch(val):
                        break
                    else:
                        print('Incorrect format. Please use #.##')

                while True:
                    ## get a valid unit
                    unit = input('What unit is that in? (USD/CAD/EUR): ')
                    unit.strip()
                    if unit in ('USD', 'CAD', 'EUR'):
                        break
                    else:
                        print('Incorrect input. Please use USD or CAD or EUR')

                obj1.v = obj1 - Money(val, unit)

            case 4:
                ## deposit
                while True:
                    ## get the value correctly formatted
                    val = input('What value would you like to deposit? (#.##): ')
                    val.strip()
                    if pat.fullmatch(val):
                        break
                    else:
                        print('Incorrect format. Please use #.##')

                while True:
                    ## get a valid unit
                    unit = input('What unit is that in? (USD/CAD/EUR): ')
                    unit.strip()
                    if unit in ('USD', 'CAD', 'EUR'):
                        break
                    else:
                        print('Incorrect input. Please use USD or CAD or EUR')

                obj1.v = obj1 + Money(val, unit)

            case 5:
                ## display balance
                print(obj1.displayBalance())
            case 6:
                ## calculate interest
                days = int(input('How many days do you want to calc for?: '))
                print(obj1.intCalc(days))
            case 7:
                ## display string
                print(obj1.__str__())
            case 8:
                ## exit message
                print("Exiting now!")


if __name__ == "__main__":
    main()
