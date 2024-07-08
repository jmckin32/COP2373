## money class that supports add,sub,mult using inheritance, plus test functions
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


def main():

    ## for checking for proper currency input
    pat = re.compile(r'\d\.\d\d')

    loop = 'y'
    val1 = ''
    uni1 = ''
    val2 = ''
    uni2 = ''
    op = ''

    while loop != 'n':

        ## gets the first unit
        while True:
            uni1 = input('What unit is your first value? (USD/CAD/EUR): ')
            uni1.strip()
            if uni1 in ('USD', 'CAD', 'EUR'):
                break
            else:
                print('Incorrect input. Please use USD or CAD or EUR')

        ## gets the first value
        while True:
            val1 = input('What value is your first value? (#.##): ')
            val1.strip()
            if pat.fullmatch(val1):
                break
            else:
                print('Incorrect format. Please use #.##')

        ## creates the first object
        num1 = Money(val1, uni1)

        ## gets the second unit
        while True:
            uni2 = input('What unit is your second value? (USD/CAD/EUR): ')
            uni2.strip()
            if uni2 in ('USD', 'CAD', 'EUR'):
                break
            else:
                print('Incorrect input. Please use USD or CAD or EUR')

        ## gets the second value
        while True:
            val2 = input('What value is your second value? (#.##): ')
            val2.strip()
            if pat.fullmatch(val2):
                break
            else:
                print('Incorrect format. Please use #.##')

        ## creates the second object
        num2 = Money(val2, uni2)

        ## gets the operation to perform
        while True:
            op = input('Which operation would you like to perform? (+/-/*): ')
            op.strip()
            if op in ('+', '-', '*'):
                break
            else:
                print('Incorrect input. Please type + or - or *')

        ## does the operation chosen
        if op == '+':
            print(f'The sum of {str(num1)} and {str(num2)} is {num1 + num2} {num1.units}')
        elif op == '-':
            print(f'The difference of {str(num1)} and {str(num2)} is {num1 - num2} {num1.units}')
        elif op == '*':
            print(f'The product of {str(num1)} and {str(num2)} is {num1 * num2} {num1.units}')

        loop = input('Would you like to try again? (y/n): ')


if __name__ == '__main__':
    main()
