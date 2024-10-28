from store_yearName import weekName


def getweekname():
    week_name = int(input("Please Enter Week Name : "))
    if week_name in weekName:
        return weekName[week_name]
    else:
        return 'Unknown'

obj = getweekname()
print(obj)


