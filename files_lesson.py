file = open("Kipling.txt", mode = "r", encoding = "utf-8")
content = file.read()
print(content)

#file = open("Kipling_ukr.txt", mode = "r", encoding = "cp1251")
#content = file.read()
#print(content)

file.close()

file = open("Kipling.txt", mode = "r", encoding = "utf-8")
list_content = file.readlines()
print(list_content)
file.close()

file = open("Kipling.txt", mode = "r", encoding = "utf-8")
first_row = file.readline()
second_row = file.readline()
print(first_row)
print(second_row)
file.close()

with open("Kipling.txt", mode = "r", encoding = "utf-8") as file:
    content_1 = file.read()
print(content_1)

try:
    with open("Kipling.txt", mode="r", encoding="utf-8") as file:
        content_2 = file.read()
except FileNotFoundError:
    content_2 = "File not found"
finally:
    print("Error handling added")
print(content_2)


