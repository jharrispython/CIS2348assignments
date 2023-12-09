#James Harris
#2078031
num = input()
first = num.split()

list = []

for i in first:
    if int(i) >= 0:
        list.append(int(i))

list.sort()

for x in list:
    print(x, end=' ')