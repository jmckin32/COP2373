## ask user for monthly expenses (type of expense, amount)
## using reduce, display total expenses, highest expense, lowest expense

import functools


def main():
    userInput = ""
    expenses = {}
    key = ""
    value = ()

    while userInput != "n":
        try:
            ## get keys and values from user
            key = input("Enter the expense: ")
            value = float(input("Enter the value of expense: "))

            ## sets the values from above to the dictionary
            expenses[key] = value

            display_values(expenses)

            userInput = input(f"\nWould you like to add another expense? (y/n)\n")
        except TypeError:
            print("ERROR: Please enter a number for the value.")
        except ValueError:
            print("ERROR: Please enter a number for the value.")

    print("You have exited out. Have a nice day!")


## displays the values
def display_values(expenses):
    ## display sum
    print(f"\nThe sum of your expenses are $"
          f"{sum(expenses.values()):,.2f}.")

    ## display the highest expense
    print(f"Your highest expense is "
          f"{functools.reduce(lambda a, b: a if a > b else b, expenses)} for $"
          f"{max(expenses.values()):,.2f}.")

    ## display the lowest expense
    print(f"Your lowest expense is "
          f"{functools.reduce(lambda a, b: a if a < b else b, expenses)} for $"
          f"{min(expenses.values()):,.2f}.")


if __name__ == "__main__":
    main()
