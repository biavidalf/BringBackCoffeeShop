import calendar

calendario = calendar.Calendar(6)

for x in calendario.itermonthdays(2021, 10):
    print(x)
