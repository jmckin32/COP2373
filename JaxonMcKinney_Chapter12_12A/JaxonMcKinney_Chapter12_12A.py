## read csv file, print dataset, calculate mean, median, standard dev, min, max,
## print if students passed each exam (>60), calculate pass percentage for each exam
import numpy as np


def main():

    ## turn the csv file into numpy array
    a = np.genfromtxt('grades.csv', delimiter=',', skip_header=True)
    ## cut off the names (turned into nans)
    a = a[:, 2:5]
    ## display the array
    print(a)

    ## mean
    print(f"\nMean Scores || "
          f"Exam 1: {round(np.mean(a[:,0]), 2)}, "
          f"Exam 2: {round(np.mean(a[:,1]), 2)}, "
          f"Exam 3: {round(np.mean(a[:,2]), 2)}, "
          f"Total: {round(np.mean(a), 2)}")

    ## median
    print(f"Median Scores || "
          f"Exam 1: {round(np.median(a[:,0]), 2)}, "
          f"Exam 2: {round(np.median(a[:,1]), 2)}, "
          f"Exam 3: {round(np.median(a[:,2]), 2)}, "
          f"Total: {round(np.median(a), 2)}")

    ## standard deviation
    print(f"Standard Deviation || "
          f"Exam 1: {round(np.std(a[:,0]), 2)}, "
          f"Exam 2: {round(np.std(a[:,1]), 2)}, "
          f"Exam 3: {round(np.std(a[:,2]), 2)}, "
          f"Total: {round(np.std(a), 2)}")

    ## maximum
    print(f"Max Score || "
          f"Exam 1: {round(np.max(a[:,0]), 2)}, "
          f"Exam 2: {round(np.max(a[:,1]), 2)}, "
          f"Exam 3: {round(np.max(a[:,2]), 2)}, "
          f"Total: {round(np.max(a), 2)}")

    ## minimum
    print(f"Min Score || "
          f"Exam 1: {round(np.min(a[:,0]), 2)}, "
          f"Exam 2: {round(np.min(a[:,1]), 2)}, "
          f"Exam 3: {round(np.min(a[:,2]), 2)}, "
          f"Total: {round(np.min(a), 2)}\n")

    ## display true if they got above 60 on an exam
    print("Did they pass?")
    print(np.bool(a > 60))

    ## pass percentage per each exam
    print(f"Pass Percentage || "
          f"Exam 1: {(np.sum(np.bool(a[:,0] > 60))) / np.size(a[:,0]):.0%}, "
          f"Exam 2: {(np.sum(np.bool(a[:,1] > 60))) / np.size(a[:,1]):.0%}, "
          f"Exam 3: {(np.sum(np.bool(a[:,2] > 60))) / np.size(a[:,2]):.0%}, "
          f"Total: {(np.sum(np.bool(a > 60))) / np.size(a):.0%}")


if __name__ == "__main__":
    main()
