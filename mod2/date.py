import datetime

print(datetime.datetime.now())
d=datetime.date.today()
print(d.strftime("%d/%m/%y %A"))

#d2=datetime.date(2024,9,8)
dstr="2024/09/08"
d2=datetime.datetime.strptime(dstr,"%Y/%m/%d")
print(d2)
d3=d2+datetime.timedelta(days=40)
print(f"date1: {d2}\ndate2: {d3}")
print(f"diff={(d3-d2).days}")
print()