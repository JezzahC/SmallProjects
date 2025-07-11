from datetime import datetime
import time, pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[14].id)

monthDict = {
    "january": "1",
    "february": "2",
    "march": "3",
    "april": "4",
    "may": "5",
    "june": "6",
    "july": "7",
    "august": "8",
    "september": "9",
    "october": "10",
    "november": "11",
    "december": "12"
}

def speak(text, rate=120):
    engine.setProperty("rate", rate)
    engine.say(text)
    engine.runAndWait()

def checkPastDates(year, month, day):
    if year < int(datetime.now().strftime("%Y")):
        return False
    elif year >= int(datetime.now().strftime("%Y")) and month < int(datetime.now().strftime("%m")):
        return False
    elif year <= int(datetime.now().strftime("%Y")) and month < int(datetime.now().strftime("%m")):
        return False
    elif year <= int(datetime.now().strftime("%Y")) and month <= int(datetime.now().strftime("%m")) and day < int(datetime.now().strftime("%d")):
        return False
    
    return True

def checkTimes(year, month, day, hour, minute, currentTime):
    if year < int(datetime.now().strftime("%Y")):
        return True
    elif year >= int(datetime.now().strftime("%Y")) and month < int(datetime.now().strftime("%m")):
        return True
    elif year <= int(datetime.now().strftime("%Y")) and month < int(datetime.now().strftime("%m")):
        return True
    elif year <= int(datetime.now().strftime("%Y")) and month <= int(datetime.now().strftime("%m")) and day < int(datetime.now().strftime("%d")):
        return True
    elif year <= int(datetime.now().strftime("%Y")) and month <= int(datetime.now().strftime("%m")) and day <= int(datetime.now().strftime("%d")) and hour < int(datetime.now().strftime("%H")):
        return True
    elif year <= int(datetime.now().strftime("%Y")) and month <= int(datetime.now().strftime("%m")) and day <= int(datetime.now().strftime("%d")) and hour <= int(datetime.now().strftime("%H")) and minute < int(datetime.now().strftime("%M")):
        return True
    elif currentTime == datetime.now().strftime("%d %m %Y %H %M"):
        return True
    
    return False

def makeReminder(name: str, notificationTime: list):
    timeDict = {
        0: "%d",
        1: "%m",
        2: "%Y",
        3: "%H",
        4: "%M",
        5: "%s"
    }

    for i in range(len(notificationTime)):
        nums = notificationTime[i]
        if nums in monthDict:
            numIndex = notificationTime.index(nums)
            notificationTime.pop(numIndex)
            notificationTime.insert(numIndex, monthDict[nums])
        elif nums == '':
            notificationTime.pop(0)
    

    while len(notificationTime) < 5:
        index = len(notificationTime)
        if index == 4:
            notificationTime.append(str(int(datetime.now().strftime(timeDict[index])) + 1))
        else: 
            notificationTime.append(datetime.now().strftime(timeDict[index]))

    if not checkPastDates(int(notificationTime[2]), int(notificationTime[1]), int(notificationTime[0])):
        return "You can't set reminders into the past silly."

    with open("reminder.txt", "a+") as f:
        f.write(f"{name} - {' : '.join(notificationTime[:3])} - {' '.join(notificationTime[3:])}\n")
    
    return "Reminder set"

def notifyReminders():
    with open("/Users/jeremie/Desktop/Coding/Python/computer/reminder.txt", "r") as reminder:
        reminderList = reminder.readlines()

    times = []
    for reminders in reminderList:
        remind = reminders.split(" - ")[1:].split(" ")
        day, month, year, hour, minute = remind[0], remind[1], remind[2], remind[3], remind[4]
        times.append((reminderList.index(reminders), day, month, year, hour, minute))

    for noteTime in times:
        if checkTimes(noteTime[0], noteTime[1], noteTime[2], noteTime[3], noteTime[4], " ".join(noteTime[1:])):
            notification(reminderList[noteTime[0]].split(" - ")[0])
            reminderList.pop(noteTime[0])
            with open("reminder.txt", "w") as f:
                f.writelines(reminderList)

def notification(reminder):
    speak(f"It's time for {reminder}! Go go go!")