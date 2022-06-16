import os
import json
import re
from datetime import date 
import sqlite3

# regex expression to identify a message with crossword times
crosswordRegexp = re.compile(r'[0-9]+:?[0-9]*,?\s?[0-9]*:?[0-9]*')
# regex expression for a single crossword time
timeRegexp = re.compile(r'[0-9]+:?[0-9]*')
# dictionary mapping month numbers to names
dateMonthDict = {1:'Jan', 2:'Feb', 3:'March', 4:'April', 5: 'May',6:'June',7:'July', 8:'Aug', 9:'Sept',10:'Oct', 11:'Nov', 12:'Dec'}

# function that returns whether a message is a crossword message or not
def isCrosswordTime(message):
    return(re.match(crosswordRegexp, message))

# extracting the first and second times from the tuple of times in our messages
def convertToTimes(times):
    pos1 = times.find(", ")
    pos2 = times.find(",")
    pos3 = times.find(" ")
    (firstTime, secondTime) = (None, None)
    if(pos1 > -1):
        firstTime = re.search(timeRegexp, times[:pos1])
        secondTime = re.search(timeRegexp, times[pos1+2:])
    elif(pos2 > -1):
        firstTime = re.search(timeRegexp, times[:pos2])
        secondTime = re.search(timeRegexp, times[pos2+1:])
    elif(pos3 > -1):
        firstTime = re.search(timeRegexp, times[:pos3])
        secondTime = re.search(timeRegexp, times[pos3+1:])
    if(firstTime):
        firstTime = firstTime[0]
    if(secondTime):
        secondTime = secondTime[0]
    return (convertToSeconds(firstTime), convertToSeconds(secondTime))

# converting a string time to seconds
def convertToSeconds(time):
    if(time is None):
        return None
    colonLoc = time.find(":")
    if(colonLoc == -1):
        return time
    minutes = time[:colonLoc]
    seconds = time[colonLoc+1:]
    if(minutes == ""):
        minutes = 0
    if(seconds == ""):
        seconds = 0
    return int(minutes)*60+int(seconds)

# taking date inputs and returning the month name
def convertToMonth(dateParam):
    return dateMonthDict[dateParam.month]

anoushkaDict = {} # to store my times of each day
partnerDict = {} # to store my friend's times of each day
messageFileOpened = open("message_1.json", "r")
messageFile = json.load(messageFileOpened)

# go through each message, adding (date, message content) as a key-value pair into the correct person's dictionary
for message in messageFile["messages"]:
    if(message.get("content", None)):
        if(isCrosswordTime(message["content"])):
            if(message["sender_name"] == "Anoushka Shrivastava"):
                anoushkaDict[date.fromtimestamp(message["timestamp_ms"]/1000)] = message["content"]
            else:
                partnerDict[date.fromtimestamp(message["timestamp_ms"]/1000)] = message["content"]

crosswordConnection = sqlite3.connect('crosswordTimes.db')
crosswordCursor = crosswordConnection.cursor()
crosswordCursor.execute('''CREATE TABLE times(month text, date text, name1Time1 int, name1Time2 int)''')

# when dates exist in both dictionaries, add my times into the database table
counter = 0
for key in anoushkaDict:
    if(partnerDict.get(key, None)):
        name1 =  convertToTimes(anoushkaDict[key])
        name2 = convertToTimes(partnerDict[key])
        if((name1[0] is not None) and (name1[1] is not None) and (name2[0] is not None) and (name2[1] is not None)):
            crosswordCursor.execute("INSERT INTO times(month, date, name1Time1, name1Time2) VALUES (?, ?, ?, ?)", (convertToMonth(key), str(key), str(name1[0]), str(name1[1])))
            crosswordConnection.commit()
            counter += 1

crosswordConnection.close()
messageFileOpened.close()


