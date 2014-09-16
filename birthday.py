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
                print months
                continue
            if dayCounter > 32:
                    break

            guys = ', '.join(row).split(',')
            guys.pop(0)
            #print 'Length:', len(guys)
            for name in guys:
                if (name == ''):
                    name = 'Nobody'
                monthCounter += 1
                if monthCounter > 14:
                    break
                #print 'month:', monthCounter
                if (dayCounter-1 == int(day) and monthCounter-1 == int(month)):
                    name = name.replace(';', ' and') + '\'s birthday!'
                    print dayCounter-1, months[monthCounter-1]
                    print 'Today is' , name
                #else:
                 #   print dayCounter-1, '=/=', day

    return months


def birthday():
    print "Happy Birthday"

    import time
    return day,month

def bivalue():
    return (1,2)

if __name__ == '__main__':
    import time
    day = time.strftime("%d")
    month = time.strftime("%m")
    #months = getBirthdays(day, month)
    months = getBirthdays(26, 05)
