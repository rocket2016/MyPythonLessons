int_list = [1, 2, 3]
#print(int_list[0])

for i in range(len(int_list)):
    print('index = ' + str(i), int_list[i])

# TODO: Проітерувати за допомогою циклу for список int
list_of_int = [100, 200, 300, 300, 50, 1]

for number in list_of_int:
    print('number = ', number)

# TODO: Проітерувати за допомогою циклу for список floats
list_of_floats = [2.5, 5.5, 11.2, 20.2, 100.1, 100.44]

for number in list_of_floats:
    print('number = ', number)

# TODO: Проітерувати за допомогою циклу for список str
list_of_strings = ['Semen', 'Mariia', 'George', 'Sveta', 'Liyba']

for name in list_of_strings:
    print('name = ', name)

# TODO: Проітерувати за допомогою циклу for змінну str
test_string = 'xyz 123 kyiv'
#print(test_string[0])

for char in test_string:
    print('char = ', char)

# TODO: Попрацювати за допомогою методів списку з створеним списком int (HomeTask)
list_of_int = [100, 200, 300, 300, 50, 1]

list_of_int.append(5)
print(list_of_int)

list_of_int.insert(4, 150)
print(list_of_int)

list_of_int.remove(300)
print (list_of_int)

list_of_int[0] = 6
print(list_of_int)

# TODO: Попрацювати з створеним списком int за допомогою операторів if|else
list_of_int = [100, 200, 300, 300, 50, 1]
#print(max(list_of_int))

min_element = list_of_int[0]
for element in list_of_int:
    if element < min_element:
        min_element = element
print(min_element)

new_list_of_int = [-1, -5, 0, 12, 0, -4, 100, 50]
positive_sublist = []
negative_sublist = []
zero_sublist = []
for element in new_list_of_int:
    if element > 0:
        positive_sublist.append(element)
    elif element < 0:
        negative_sublist.append(element)
    else:
        zero_sublist.append(element)
print(positive_sublist)
print(negative_sublist)
print(zero_sublist)


# TODO: Find max of list of int (HomeTask)

# TODO: Create list of int with even, odd and zero numbers. Find count for each category (even, odd, zero)
# TODO (Hometask)
# TODO hint: if num % 2 == 0 then num is even, else num is odd

# TODO: List slicing
# list[start:stop:step]

list_to_slice = [-1, -5, 0, 12, 0, -4, 100, 50]
sliced_list = list_to_slice[:4]
print(sliced_list)

list_to_slice = [-1, -5, 0, 12, 0, -4, 100, 50]
sliced_list = list_to_slice[:6:2]
print(sliced_list)

list_to_slice = [-1, -5, 0, 12, 0, -4, 100, 50]
sliced_list = list_to_slice[1:6:3]
print(sliced_list)

list_to_slice = [-1, -5, 0, 12, 0, -4, 100, 50]
sliced_list = list_to_slice[::2]
print(sliced_list)

list_to_slice = [-1, -5, 0, 12, 0, -4, 100, 50]
sliced_list = list_to_slice[1::2]
print(sliced_list)

list_to_slice = [-1, -5, 0, 12, 0, -4, 100, 50]
#list_to_slice.reverse()
#print(list_to_slice)
sliced_list = list_to_slice[::-1]
print(sliced_list)

list_to_slice = [-1, -5, 0, 12, 0, -4, 100, 50]
sliced_list = list_to_slice[::len(list_to_slice)-1]
print(sliced_list)

list_to_slice = [-1, -5, 0, 12, 0, -4, 100, 50]
print(type(list_to_slice))