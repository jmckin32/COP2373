import random

def main():

    # initialize variable
    question = str()

    # read file to list object
    f = open("8ball_responses.txt")
    list = f.read().splitlines()

    # loop code until user enters quit
    while question != "quit":
        question = input(f"What is thy question for the Magic 8 Ball? (Type \"quit\" to quit)\n")

        if question != "quit":
            print(random.choice(list))

    print("The 8 ball beckons thee to come again.")

    #make sure to close that file
    f.close

if __name__ == "__main__":
    main()