import re
month_list ={
    "January": 1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12}
while True:
    try:
        while True:
            input_date = input("Date: ").strip()
            if "/" in input_date:
                m,d,y = re.split(r'/', input_date)
                if y.isdigit() and int(d) <= 31 and int(m) <= 12:
                    print(y,f"{int(m):02}",f"{int(d):02}", sep ="-")
                    break
            if ", " in input_date:
                m,d,y = re.split(r' |, ', input_date)
                if y.isdigit() and int(d) <= 31 and m in month_list:
                    m = month_list.get(m)
                    print(y,f"{int(m):02}",f"{int(d):02}", sep ="-")
                    break
    except ValueError:
        pass
    else:
        break





