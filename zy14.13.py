#James Harris
#2078031

num_calls = 0

def partition(user_ids, i, k):
    index = (i + k) // 2
    value = user_ids[index]

    x = i
    y = k

    while True:
        while user_ids[x] < value:
            x += 1

        while user_ids[y] > value:
            y -= 1

        if x >= y:
            return y

        user_ids[x], user_ids[y] = user_ids[y], user_ids[x]

        x += 1
        y -= 1

# Quicksort algorithm
def quicksort(user_ids, i, k):
    global num_calls
    num_calls += 1

    if i < k:
        part_index = partition(user_ids, i, k)

        quicksort(user_ids, i, part_index)
        quicksort(user_ids, part_index + 1, k)


if __name__ == "__main__":

    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()


    quicksort(user_ids, 0, len(user_ids) - 1)

    print(num_calls)

    for user_id in user_ids:
        print(user_id)