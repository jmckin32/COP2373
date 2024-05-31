# User enters an email, and program gives a score on how likely the email is to be a scam
# take 2: add the make_timer function
import time

# so i moved all the code into a full function and just made main() call that code through make_timer so thats why theres a restructure
def main():
    make_timer(scam_test())

def scam_test():

    email = str()
    score = int(0)
    chances = float()
    wordsAppeared = []

    # read list of scam words
    f = open("wordlist.txt")
    wordList = f.read().splitlines()
    f.close

    email = input(f"Please enter your written email.\n")
    email = email.lower()

    # check if words in list appear in email
    for x in wordList:
        if x in email:
            score += 1

            # adds every suspicious word/phrase to a list
            wordsAppeared.append(x)

    # finds how likely email is to be a scam
    chances = likelihood(score)

    print(f"Your scam score is {score}\n"
          f"The likelihood of being a scam is estimated to be {chances:.0%}\n"
          f"The phrases that seem suspicious are: {', '.join(wordsAppeared)}")

def likelihood(y):

    # how many scam points you need for 100%
    TOTALODDS = 4

    # calculates percentage on how likely email is to be a scam
    r = y/TOTALODDS
    if r > 1:
        r = 1
    return r

def make_timer(scam_test):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        ret_val = scam_test(*args, **kwargs)
        t2 = time.time()
        print("Time elapsed was ", t2 - t1)
        return ret_val
    return wrapper

# this is like not in a function but something about it being here makes the code actually work idk
scam_test = make_timer(scam_test)

if __name__ == "__main__":
    main()