## get the nearest angle and the length of the adjacent side, and determine the hypotenuse of a right triangle
from math import cos, radians


def main():

    ## get angle
    angle = float(input('What is the value of the chosen angle in degrees?: '))
    ## get adjacent side
    side = float(input('What is the value of the adjacent side?: '))

    ## calculate the hypotenuse
    result = round((side / cos(radians(angle)))*100)/100

    ## display the hypotenuse
    print(f"The length of the hypotenuse is {result}")


if __name__ == "__main__":
    main()
