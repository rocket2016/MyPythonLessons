mama = 'her name is Sveta'
print(mama.encode())

mama = 'her name is Sveta'
len(mama)
print(len(mama))

string_list_1 = ['her', 'name', 'is', 'Sveta']
string_1 =  ','.join(string_list_1)
print(string_1)

print(type(str(60)))

name = 'Kava'
fstring_exampl = f'Client name is {name}'
print(fstring_exampl)

age = 55
fstring_age = f'Client age is {age}'
print(fstring_age)

# TODO : Types of strings
test_string_one_quate = 'The book name is \'Bla bla bla\''
print(test_string_one_quate)

test_string_double_quote = "The book name is 'Bla bla bla'"
print(test_string_double_quote)

test_string2_double_quote = "The book name is \n'Bla bla bla'"
print(test_string2_double_quote)

test_string_triple_quote = """The book name is
'Bla bla bla'"""
print(test_string_triple_quote)

# TODO : String comparison

# TODO : Concatenation
string_list_1 = ['her', 'name', 'is', 'Sveta']
result_string = ''
for element in string_list_1:
    result_string = result_string + element + ' '
print(result_string)

# TODO : str methods
help(str) #open documentation for string class

# Case Manipulation

# Searching and Replacing

# Splitting and Joining
test_string_symbols = "What, is your name? My? Name - is Sveta!"
symbols_list = test_string_symbols.split(',')
print(symbols_list)

# Content Checking

# String Cleaning

# Formatting
name_1 = 'Kava'
name_2 = 'Tea'
fstring_exampl = f'Client name is {name_1} and {name_2}'
print(fstring_exampl)

row_string = r"C:\Users\vasilsve\OneDrive - Tietoevry\Infopulse_ODB_Export\Homefolder\Python Projects\MyPythonLessons\string_lesson.py"

name_1 = 'Semen'
name_2 = 'George'
format_string_example = "Client name is {1} and {0}".format(name_1, name_2)
print(format_string_example)

# TODO : Indexing and slices