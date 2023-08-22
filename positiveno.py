# write a Python program to print all positive numbers in a range. create list
def print_positive_numbers_in_range(lst):
    positive_numbers = [num for num in lst if num > 0]
    for num in positive_numbers:
        print(num)

list1 = [12,-7,5,64,-14]
print("List 1:")
print_positive_numbers_in_range(list1)

list2 = [12,14,-95,3]
print("List 2:")
print_positive_numbers_in_range(list2)

# output : 
# List 1:
# 12
# 5
# 64
# List 2:
# 12
# 14
# 3