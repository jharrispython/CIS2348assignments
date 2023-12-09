#James Harris
#2078031

def selection_sort_descend_trace(number):
    for i in range(len(number) - 1):
        x = i
        for y in range(i + 1, len(number)):
            if number[x] < number[y]:
                x = y
        number[i], number[x] = number[x], number[i]
        for value in number:
            print(value, end=" ")
        print()
    return number

if __name__ == "__main__":
    number = []
    number = [int(j) for j in input("").split()]
    selection_sort_descend_trace(number)