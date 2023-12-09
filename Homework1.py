# James Harris
# 2078031
print('Birthday Calculator\nCurrent day')

month1 = int(input('Month: '))
day1 = int(input('Day: '))
year1 = int(input('Year: '))

print('Birthday')

month2 = int(input('Month: '))
day2 = int(input('Day: '))
year2 = int(input('Year: '))

age = year1 - year2
if month2 < month1:
    age += 1
elif month1 == month2:
    if day2 < day1:
        age += 1
if month1 == month2 and day2 == day2:
    print('Happy Birthday')

print('You are '+str(age)+" years old.")