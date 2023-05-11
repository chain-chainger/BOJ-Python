import datetime

current_time = datetime.datetime.now() + datetime.timedelta(hours = 9)
print(current_time.year)
print("%02d" % current_time.month)
print("%02d" % current_time.day)