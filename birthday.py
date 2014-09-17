#!/usr/bin/python
#birthday.py
#A script to tell you who's birthday it is
#Author: paul-louis
#TODO: Wish the lucky guy a wonderful birthday!
#

from time import strftime
import xlrd, csv
import os, sys
import gspread
import getpass

def init():
    if len(sys.argv) != 2:
        usage()
    username = sys.argv[1]
    print "Hi", username.replace("@swiftkey.com",'') + "!"
    print "Please enter your password to download the latest birthday spreadsheet."
    password = getpass.getpass()
    return (username, password)

def usage():
    sys.exit()
    print "Usage: ./birthday.py username"

def getBirthdays(day, month):
    months = []
    dayCounter = 0
    with open('Birth.csv', 'rb') as csvfile:
        lineReader = csv.reader(csvfile, delimiter='\n', quotechar='|')
        for row in lineReader:
            monthCounter = 1
            dayCounter +=1
            if dayCounter == 1:
                for name in row[0].split(','):
                    months.append(name.strip('"'))
                continue
            if dayCounter > 32:
                break

            friends = ', '.join(row).split(',')
            friends.pop(0)
            for name in friends:
                name = name.strip('"')
                if (name == ''):
                    name = 'nobody'
                monthCounter += 1
                if monthCounter > 14:
                    break
                dayReal = dayCounter-1
                monthReal = monthCounter-1
                if (dayReal == int(day) and monthReal == int(month)):
                    name = name.replace(';', ' and') + '\'s birthday!'
                    print 'We are the', dayReal, 'of', months[monthReal] + '.'
                    print 'Today is' , name
    return months

def fetchSpreadsheet(username, password):
    print "Fetching the Birthday spreadsheet..."
    docid = '0AnDRnFzjhfTAdERvbC1YUnJTWlQtR3MwZzhlRERTRUE'
    gc = gspread.login(username, password);
    wks = gc.open('Team Birthdays').sheet1
    spreadsheet = gc.open_by_key(docid)
    for i, workSheet in enumerate(spreadsheet.worksheets()):
        filename = 'Birth.csv'
        with open(filename, 'wb') as f:
            writer = csv.writer(f)
            newValues = []
            for l in workSheet.get_all_values():
                newSubl = []
                for s in l:
                    s = s.replace(',', ';')
                    newSubl.append(s)
                newValues.append(newSubl);
            writer.writerows(newValues)
    print "Spreadsheet fetching completed."

if __name__ == '__main__':
    domain = "@swiftkey.com"
    username, password = init()
    if domain not in username:
        username = username + domain
    fetchSpreadsheet(username, password)
    getBirthdays(strftime("%d"),strftime("%m"))
    os.remove('Birth.csv');
