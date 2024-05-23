# User enters an email, and program gives a score on how likely the email is to be a scam

def main():

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

if __name__ == "__main__":
    main()