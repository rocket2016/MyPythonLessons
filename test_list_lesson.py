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

# TODO: Попрацювати за допомогою методів списку з створеним списком int
list_of_int = [100, 200, 300, 300, 50, 1]

list_of_int.append(5)
print(list_of_int)

list_of_int.insert(4, 150)
print(list_of_int)

list_of_int.remove(300)
print (list_of_int)

list_of_int[0] = 6
print(list_of_int)