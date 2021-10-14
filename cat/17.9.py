a = str(input("Введите числа через запятую:"))
my_list = a.strip().split(' ')
print(my_list)
my_list = list(map(int, my_list))
print(my_list)
my_list.sort()
print(my_list)

# искомое число
value = int(input("Ввести искомое число:"))

mid = len(my_list) // 2
low = 0
high = len(my_list) - 1

while my_list[mid] != value and low <= high:
    if value > my_list[mid]:
        low = mid + 1

    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print("No value")
else:
    print("ID =", mid)

