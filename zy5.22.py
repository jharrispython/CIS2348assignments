# James Harris
# 2078031
print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12\n")

first_service = input("Select first service:\n")
second_service = input("Select second service:\n")

print("\nDavy's auto shop invoice\n")
Total_sum = 0
if first_service == "Oil change":
    print("Service 1: Oil change, $35")
    Total_sum += 35
elif first_service == "Tire rotation":
    print("Service 1: Tire rotation, $19")
    Total_sum += 19
elif first_service == "Car wash":
    print("Service 1: Car wash, $7")
    Total_sum += 7
elif first_service == "Car wax":
    print("Service 1: Car wax, $12")
    Total_sum += 12
elif first_service == "-":
    print("Service 1: No service")
else:
    print("Service 1: Wrong service entered. Please refer menu")

if second_service == "Oil change":
    print("Service 2: Oil change, $35")
    Total_sum+= 35
elif second_service == "Tire rotation":
    print("Service 2: Tire rotation, $19")
    Total_sum += 19
elif second_service == "Car wash":
    print("Service 2: Car wash, $7")
    Total_sum += 7
elif second_service == "Car wax":
    print("Service 2: Car wax, $12")
    Total_sum += 12

elif second_service == "-":
    print("Service 2: No service")
else:
    print("Service 1: Wrong service entered. Please refer menu")

print("\nTotal: $", Total_sum, sep="")
