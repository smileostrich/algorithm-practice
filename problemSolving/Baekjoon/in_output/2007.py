import datetime
m, d = map(int, input().split())
y = 2007
week = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
print(week[datetime.date(y,m,d).weekday()])
