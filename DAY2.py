fi = open('DAY2.inp')
reports = fi.readlines()
fi.close()
count = 0
def safeReportFilter(report):
    global errorIndex
    for i in range(1, len(levelReport)):
        if i+1<len(levelReport):
            if (levelReport[i] < levelReport[i-1] and levelReport[i] < levelReport[i+1]):
                print(levelReport[i] < levelReport[i-1] and levelReport[i] < levelReport[i+1])
            if (abs(levelReport[i] - levelReport[i-1]) > 3):
                print(abs(levelReport[i] - levelReport[i-1]) > 3)
            if (abs(levelReport[i] - levelReport[i+1]) > 3):
                print(abs(levelReport[i] - levelReport[i+1]) > 3)
            if (levelReport[i] > levelReport[i-1] and levelReport[i] > levelReport[i+1]):
                print(levelReport[i] > levelReport[i-1] and levelReport[i] > levelReport[i+1])
            if (levelReport[i] == levelReport[i-1] or levelReport[i] == levelReport[i+1]):
                print(levelReport[i] == levelReport[i-1] or levelReport[i] == levelReport[i+1])
            if (levelReport[i] < levelReport[i-1] and levelReport[i] < levelReport[i+1]) or abs(levelReport[i] - levelReport[i-1]) > 3 or abs(levelReport[i] - levelReport[i+1]) > 3:
                errorIndex = i
                return "UNSAFE"
            elif (levelReport[i] > levelReport[i-1] and levelReport[i] > levelReport[i+1]) or abs(levelReport[i] - levelReport[i-1]) > 3 or abs(levelReport[i] - levelReport[i+1]) > 3:
                errorIndex = i
                return "UNSAFE"
            elif (levelReport[i] == levelReport[i-1] or levelReport[i] == levelReport[i+1]):
                errorIndex = i
                return "UNSAFE"
        else:
            if (abs(levelReport[i] - levelReport[i-1]) > 3):
                print(abs(levelReport[i] - levelReport[i-1]) > 3)
            if (levelReport[i] == levelReport[i-1]):
                print(levelReport[i] == levelReport[i-1])
            if abs(levelReport[i] - levelReport[i-1]) > 3:
                errorIndex = i
                return "UNSAFE"
            elif (levelReport[i] == levelReport[i-1]):
                errorIndex = i
                return "UNSAFE"
    return "SAFE"
def getErrorIndex():
    global errorIndex
    return errorIndex
for report in reports:
    levelReport = list(map(int, report.split(" ")))
    tempLevelReport = list(map(int, report.split(" ")))
    print(levelReport)
    print(safeReportFilter(levelReport))
    if (safeReportFilter(levelReport) == "SAFE"):
        count+=1
    elif (safeReportFilter(levelReport) == "UNSAFE"):
        print("ITERATION 2")
        savedErrorIndex = getErrorIndex()
        tempLevelReport.remove(tempLevelReport[savedErrorIndex])
        print(tempLevelReport)
        print(safeReportFilter(tempLevelReport))
        if (safeReportFilter(tempLevelReport) == "SAFE"):
            count+=1
        elif (safeReportFilter(tempLevelReport) == "UNSAFE" and savedErrorIndex+1<len(levelReport)):
            print("ITERATION 3")
            levelReport.remove(levelReport[savedErrorIndex+1])
            print(levelReport)
            print(safeReportFilter(levelReport))
            if (safeReportFilter(levelReport) == "SAFE"):
                count+=1
fo = open('DAY2.out','w')
fo.write(str(count))
fo.close()
