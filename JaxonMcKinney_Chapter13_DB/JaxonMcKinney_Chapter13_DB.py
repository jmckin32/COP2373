import sqlite3 as sql
import math
import matplotlib.pyplot as plt
import numpy as np


def growthCalc(connection):

    cursor = connection.cursor()

    for row in cursor.execute('''SELECT POPULATION FROM population'''):
        ## cleaning up input
        pop = str(row).replace(',', '')
        pop = pop.replace('(', '')
        pop = int(pop.replace(')', ''))

        ## formula and saving result
        p = int(round(pop * (math.e ** (.02 * 20))))
        cursor.execute(f'''UPDATE population
        SET POPULATION={p}''')

    for row in cursor.execute('''SELECT YEAR FROM population'''):
        ## cleaning up
        year = str(row).replace(',', '')
        year = year.replace('(', '')
        year = int(year.replace(')', ''))

        ## add to year
        cursor.execute(f'''UPDATE population
        SET YEAR={year+20}''')


def plotGrowth(connection):

    cursor = connection.cursor()

    ## display cities
    string = 'Cities:'
    for row in cursor.execute('''SELECT CITY FROM population'''):
        ## cleanup and add to display
        name = str(row).replace(',', '')
        name = name.replace('(', '')
        name = name.replace(')', '')
        string += f' {name}'
    print(string)

    ## get inputs
    city = input("Which city do you want to plot the growth of? (Please enter exact): ")
    years = int(input("How many sets of 20 years do you want to replicate the growth of?: ")) + 1

    ## set plot points
    xpoints = []

    for x in range(1, years+1):
        xpoints.append(x-1)

    ## get starting y value
    for y in cursor.execute(f'''SELECT POPULATION from population WHERE CITY='{city}';'''):
        ## cleanup and get value
        pop = str(y).replace(',', '')
        pop = pop.replace('(', '')
        pop = int(pop.replace(')', ''))
    ypoints = [pop]

    ## get rest of y values
    for x in xpoints:
        if x < len(xpoints)-1:
            ypoints.append(int(round(ypoints[x]*1.02)))

    ## plot the graph
    plt.plot(xpoints, ypoints, marker='o')
    plt.title("Population")
    plt.ylabel("Amount of people (hundred thousands)")
    plt.xlabel("Years since current (times 20)")
    plt.show()


def main():

    ## create sql objects
    connection = sql.connect("population_JM.db")
    cursor = connection.cursor()

    ## start creating table
    cursor.execute('''CREATE TABLE IF NOT EXISTS population(
    CITY TEXT,
    YEAR INTEGER,
    POPULATION INTEGER);''')

    ## insert values into table
    cursor.execute('''INSERT INTO population(CITY, YEAR, POPULATION)
    VALUES ('Jacksonville',2023,985843)
    ,('Miami',2023,455924)
    ,('Tampa',2023,403364)
    ,('Orlando',2023,320742)
    ,('St. Petersburg',2023,263553)
    ,('Port St. Lucie',2023,245021)
    ,('Cape Coral',2023,224455)
    ,('Hialeah',2023,221300)
    ,('Tallahassee',2023,202221)
    ,('Fort Lauderdale',2023,184255);''')

    ## display initial values
    for row in cursor.execute('''SELECT * FROM population'''):
        print(row)

    ## do amount of growth calculations
    choich = int(input("How many sets of 20 years do you want to simulate population growth of? (Input 0 to skip): "))
    if choich != 0:
        for i in range(0, choich):
            growthCalc(connection)

        ## display new values
        for row in cursor.execute('''SELECT * FROM population'''):
            print(row)

    ## do plot growth function
    plotGrowth(connection)


if __name__ == "__main__":
    main()
