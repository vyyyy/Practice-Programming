#import modules
from datetime import date, datetime, timedelta

#function generates items with some delta
def perdelta(start, end, delta):
	curr = start
	while curr < end:
		yield curr
		curr += delta

#generate a list with dates
my_list = [x for x in perdelta(date(2016, 2, 27), date(2017, 1, 1), timedelta(days=1))]

#generate a list to wrap around the main list 
strings = ['a', 'b', 'c', 'd', 'e']

#loop through main list to print item and associated string value from strings
for i, date in enumerate(my_list[:10]):
    index = i % len(strings)
    s = strings[index]
    print(i, date, s)
