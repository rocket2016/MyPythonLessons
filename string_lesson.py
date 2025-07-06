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
# 1 and o - indexes

client_group_template = "Client name is {1} and {0}"
client_group_1 = client_group_template.format('Microsoft', 'Samsung')
client_group_2 = client_group_template.format('Veres', 'Roshen')
print(client_group_1 + '\n' + client_group_2)
#\n - move to new row

client_1 = 'Microsoft'
client_2 = 'Samsung'
client_3 = 'Veres'
client_4 = 'Roshen'
client_group_1 = f'Client name is {client_1} and {client_2}'
client_group_2 = f'Client namen is {client_3} and {client_4}'

def create_client_group(client_1, client_2):
    client_group = f'Client name is {client_1} and {client_2}'
    return client_group

client_group_1 = create_client_group(client_1 = client_1, client_2 = client_2)
client_group_2 = create_client_group(client_1 = client_2, client_2 = client_4)
client_group_3 = create_client_group(client_1 ='Coro', client_2 ='Trifary')
print(client_group_1 + '\n' + client_group_2 + '\n' + client_group_3)

# TODO : Indexing and slices
