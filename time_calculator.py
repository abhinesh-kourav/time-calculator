def add_time(start, duration, startDay=None):
    startList = start.split(':')
    startHH = startList[0]
    startMM = startList[1].split(" ")[0]
    am_pm = startList[1].split(" ")[1]
    if am_pm == "PM":
        startHH = int(startHH) + 12
    durationHH = duration.split(':')[0]
    durationMM = duration.split(':')[1]
    resultMM = int(startMM) + int(durationMM)
    resultHH = int(startHH) + int(durationHH)
    if resultMM >= 60:
        resultMM -= 60
        resultHH += 1
    resultMM = str(resultMM)
    if len(resultMM) == 1:
        resultMM = '0'+ resultMM
    dayCount = 0
    while resultHH >= 24:
        dayCount += 1
        resultHH -= 24
    if resultHH < 12:
        resultAMPM = "AM"
    else:
        resultAMPM = "PM"
        resultHH -= 12
    if resultHH == 0:
        resultHH += 12
    if dayCount == 0:
        countText = ""
    elif dayCount == 1:
        countText = " (next day)"
    else:
        countText = " (" + str(dayCount) + " days later)"
    days = ["monday",'tuesday','wednesday','thursday','friday','saturday','sunday']
    dayText = ''
    for day in days:
        if startDay != None:
            if startDay.lower() == day:
                startIndex = days.index(day)
                lastIndex = startIndex + dayCount
                while(lastIndex > 6):
                    lastIndex -= 7
                newDay = days[lastIndex]
                dayText = ', ' + newDay[0].upper() + newDay[1:]
    result = str(resultHH) + ':' + resultMM + " " + resultAMPM + dayText + countText
    return result
