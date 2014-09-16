#!/usr/bin/python
#birthday.py
#A script to tell you who's birthday it is
#Author: paul-louis
#TODO: Handle real csv and not csv+comapunkt
#TODO: Get the last data from the internet
#TODO: Wish the lucky guy a wonderful birthday!
#

def getBirthdays(day, month):
    months = []
    dayCounter = 0
    import csv
    with open('Birthdays.csv', 'rb') as csvfile:
        linereader = csv.reader(csvfile, delimiter='\n', quotechar='|')
        for row in linereader:
            monthCounter = 1
            dayCounter +=1
            if dayCounter == 1:
                for name in row[0].split(','):
                    months.append(name)
                continue
            if dayCounter > 32:
                    break

            guys = ', '.join(row).split(',')
            guys.pop(0)
            for name in guys:
                if (name == ''):
                    name = 'Nobody'
                monthCounter += 1
                if monthCounter > 14:
                    break
                if (dayCounter-1 == int(day) and monthCounter-1 == int(month)):
                    name = name.replace(';', ' and') + '\'s birthday!'
                    print 'We are the', dayCounter-1, 'of', months[monthCounter-1]
                    print 'Today is' , name

    return months


def birthday():
    print "Happy Birthday"

if __name__ == '__main__':
    from time import strftime
    day     = strftime("%d")
    month   = strftime("%m")
    months  = getBirthdays(day, month)
    months  = getBirthdays(13, 12)
