from datetime import date
from calendar import monthcalendar
from string import letters

MeetupDayException = Exception

def meetup_day(year, month, weekday, which):
    WEEKDAYS = {'Monday': 0,
                'Tuesday': 1,
                'Wednesday': 2,
                'Thursday': 3,
                'Friday': 4,
                'Saturday': 5,
                'Sunday': 6}
    month_weekdays = zip(*monthcalendar(year, month))
    meetings = list(n for n in month_weekdays[WEEKDAYS[weekday]]
                    if n != 0)
    if which == 'teenth':
        find_index = map(lambda x: x in range(13, 20), meetings).index(1)
        return date(year, month, meetings[find_index])
    elif which == 'last':
        return date(year, month, meetings[-1])
    else:
        which = int(which.translate(None, letters))
        if which > len(meetings):
            raise MeetupDayException
        else:
            return date(year, month, meetings[which-1])

