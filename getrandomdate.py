import random
import time

def getRandomDate(StartDate, endDate):
    print("Printing random date between", StartDate, "and", endDate)
    randomGenerator = random.random()
    dateFormat = "%m/%d/%Y"
    startTime = time.mktime(time.strptime(StartDate, dateFormat"))
    endTime = time.mktime(time.strptime(endDate, dateFormat))
    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

print("Random date = ", getRandomDate("1/1/2016", "12/12/2018"))