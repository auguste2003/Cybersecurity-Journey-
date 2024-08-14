import datetime # the modul that handle the time

print(datetime.datetime.now())
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.date.today())
print(datetime.datetime.now().time()) # for the time

# format the time
now = datetime.datetime.now()
print(now)
now.strftime("%d %m %y %H:%M:%S")
now.strftime("%d-%b-%y %H:%M:%S")