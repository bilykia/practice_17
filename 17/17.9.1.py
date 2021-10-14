def serch_value(my_list, value):
    if value < my_list[0] or value > my_list[len(my_list) - 1]:
        print('Value out of range')
    else:
        mid = len(my_list) // 2
        low = 0
        high = len(my_list) - 1

        while my_list[mid] != value and low <= high:
            if value > my_list[mid]:
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) // 2

        print("ID =", mid)


def bubble_sort(my_list):
    for i in range(len(my_list) - 1):
        for j in range(len(my_list) - i - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list


my_string = str(input())
my_list = my_string.split(' ')
my_list = list(map(int, my_list))

bubble_sort(my_list)

value = int(input())

serch_value(my_list, value)
