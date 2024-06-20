import csv


def main():

    with open('grades.csv', 'r', newline='') as file:
        reader = csv.reader(file, delimiter=',')

        ## the %--s indicates how many characters long each thing takes up for nicer display
        ## row[0] = first name, [1] = last name, [2][3][3] = exam scores 1 2 and 3 respectfully
        for row in reader:
            print("%15s" % row[0], "%20s" % row[1], "%6s" % row[2], "%6s" % row[3], "%6s" % row[4])


if __name__ == "__main__":
    main()
