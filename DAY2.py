fi = open('DAY2.inp')
reports = fi.readlines()
fi.close()
count = 0
def safeReportFilter(report):
    state = ""
    levelReport = list(map(int, report.split(" ")))
    for i in range(1, len(levelReport)):
        if levelReport[i] < levelReport[i-1]:
            if state == "INCREASE" or abs(levelReport[i] - levelReport[i-1])>3:
                return "UNSAFE"
            elif state == "":
                if abs(levelReport[i] - levelReport[i-1]) > 3:
                    return "UNSAFE"
                else:
                    state = "DECREASE"
        elif levelReport[i] > levelReport[i-1]:
            if state == "DECREASE" or abs(levelReport[i] - levelReport[i-1])>3:
                return "UNSAFE"
            elif state == "":
                if abs(levelReport[i] - levelReport[i-1]) > 3:
                    return "UNSAFE"
                else:
                    state = "INCREASE"
        elif levelReport[i] == levelReport[i-1]:
            return "UNSAFE"
    return "SAFE"
for report in reports:
    if (safeReportFilter(report) == "SAFE"):
        count+=1
fo = open('DAY2.out','w')
fo.write(str(count))
fo.close()
