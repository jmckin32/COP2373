import csv


def main():

    ## get the number of students from user
    numStudents = int(input("How many students would you like to input?\n"))

    print("Please input the first name, last name, exam 1 score, exam 2 score, and exam 3 score separated by a comma and space (\", \").\n")

    with open('grades.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        ## write header
        writer.writerow(["FirstName", "LastName", "Exam1", "Exam2", "Exam3"])

        for i in range(numStudents):
            x = input()
            x = x.split(", ")
            x[2] = int(x[2])
            x[3] = int(x[3])
            x[4] = int(x[4])
            writer.writerow(x)


if __name__ == "__main__":
    main()
