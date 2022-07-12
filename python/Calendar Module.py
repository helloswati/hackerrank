Calendar Module
The calendar module allows you to output calendars and provides additional useful functions for them.
class calendar.TextCalendar([firstweekday])
This class can be used to generate plain text calendars.



import datetime
import calendar

m, d, y = map(int, input().split())
input_date = datetime.date(y, m, d)
print(calendar.day_name[input_date.weekday()].upper())