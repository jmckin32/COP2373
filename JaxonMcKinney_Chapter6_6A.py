## validate phone number, social security number, and zip code
import re

def main():

    ## patterns
    phoneNumberPat = re.compile(r"((\(\d{3}\)|\d{3}[-\s]??)\d{3}[-\s]??\d{4})")
    ssnPat = re.compile(r"(\d{3}[-\s]??\d{2}[-\s]??\d{4})")
    zipPat = re.compile(r"(\d{5})")

    ## other variables
    phoneNumber = ""
    ssn = ""
    zip = ""
    inp = ""

    ## this one's for loop stuff
    flag = 0

    ## get the user's phone number then checks formatting
    while (flag == 0):
        inp = input(f"Please enter your phone number\n")
        if phone_number_search(phoneNumberPat, inp) == True:
            phoneNumber = inp
            flag = 1

    ## reset loop
    flag = 0

    ## get the user's SSN then checks formatting
    while (flag == 0):
        inp = input(f"Please enter your SSN\n")
        if ssn_search(ssnPat, inp) == True:
            ssn = inp
            flag = 1

    ##
    flag = 0

    ## get the user's zip code then checks formatting
    while (flag == 0):
        inp = input(f"Please enter your zip code\n")
        if zip_search(zipPat, inp) == True:
            zip = inp
            flag = 1

    ## prints the previous answers (for user clarity)
    print(f"Your phone number is {phoneNumber}.\n"
          f"Your SSN is {ssn}.\n"
          f"Your zip code is {zip}.")


def phone_number_search(phoneNumberPat, inp):
    ## checks to see if input fits the phone number format
    if re.match(phoneNumberPat, inp):
        print("Phone number accepted!")
        return True
    else:
        print("Incorrect format..")
        return False


def ssn_search(ssnPat, inp):
    ## checks to see if input fits SSN format
    if re.match(ssnPat, inp):
        print("SSN accepted!")
        return True
    else:
        print("Incorrect format..")
        return False


def zip_search(zipPat, inp):
    ## checks to see if input sits ZIP format
    if re.match(zipPat, inp):
        print("Zip code accepted!")
        return True
    else:
        print("Incorrect format..")
        return False


if __name__ == "__main__":
    main()