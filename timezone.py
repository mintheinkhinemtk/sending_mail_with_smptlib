import datetime as dt
now = dt.datetime.now()
print(now)
year = now.year
month = now.month
my_birthday = dt.datetime(year=1997,month=6,day=1,hour=10,minute=10)
print("My birthday is ",my_birthday)
