## get sentences from user, then check for amount of sentences and display each sentence individually
import re


def main():
    sentences = ""

    ## get the sentences from user to then put through the function
    sentences = input("Please enter your sentences\n")

    sentence_find(sentences)


def sentence_find(s):
    """Finds the sentences in the string and displays results"""

    ## define the pattern for a "full sentence" and then finds all instances of a full sentence
    pat = re.compile("[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)", flags=re.DOTALL)
    m = re.findall(pat, s)

    ## displays the number of sentences found and each individual found sentence
    print(f"There were {len(m)} sentence(s).")
    for i in m:
        print(f"-> {i}")


if __name__ == "__main__":
    main()
