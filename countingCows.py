# Counting Cows game, where you define N years and then each year Calves increases
#
# A cow has a calf every year. A calf becomes a cow in 2 years, starting with one cow we have to count how many animals are there in N years. Suppose no cow ever dies...
# eg at N=5:
# 1st cow gave 2 calves(1 at the age of 2 another at the age of 3, next at 4, next at 5) total= 4 calves now the first cow is also already 3 year old so (she gave birth to 1 calf at the age of 2 another at the age of 3) total = 2 calves. the second cow must also be 2 year old so she just gave birth to another calf total = 1 calf.
# sum = 1+4+2+1
# The reccursion goes on as the year increases

def countCows(maxYear, year, noCows, yearCalves):
    """
    """
    if year == maxYear:
        print("Total no of cows {} after {} years ".format(noCows, year))
    else:
        grownCows = 0
        if year % 2 == 1:
            try:
                grownCows = yearCalves[year - 2]
            except:
                pass
        
        noCows += grownCows
        if year == 0:
            yearCalves[year] = 0
        else:
            yearCalves[year] = noCows

        print("Year: {} Cows: {} Calves: {} Grown Calves this year: {}".format(year, noCows, yearCalves[year], grownCows))
        countCows(maxYear, year + 1, noCows, yearCalves)


maxYears = 10 #int(input("Please define how many years: "))
noCows = 1
yearCalves = {}
countCows(maxYears, 0, noCows, yearCalves)







