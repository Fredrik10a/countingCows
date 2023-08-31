#
# Counting Cows
#


def presentation():
    """
    """
    message = """
Counting Cows: \n
A cow has one calf every year.
A calf becomes a cow in 2 years, starting with one cow, we have to count how many animals there are i N years. Suppose no cow ever dies...
"""
    print(message)

def countCows(maxYear, year, noCows, yearCalves):
    """
    """
    if year == maxYear:
        print("Total no of cows {} after {} years ".format(noCows, year))
    else:
        grownCows = 0
        try:
            if yearCalves[year - 2] > 0:
                grownCows = yearCalves[year - 2]
        except:
            pass
        
        noCows += grownCows
        if year == 0:
            yearCalves[year] = 0
        else:
            yearCalves[year] = noCows

        print("Year: {} Cows: {} Calves: {} - calves grown to cows this year: {}".format(year, noCows, yearCalves[year], grownCows))
        countCows(maxYear, year + 1, noCows, yearCalves)

# Init
presentation()
# Lets Go!
maxYears = int(input("Please define how many years: "))
noCows = 1
yearCalves = {}
countCows(maxYears, 0, noCows, yearCalves)







