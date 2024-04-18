# Write a Python Program to find area of a Triangle

base = float(input("Enter Base :"))
height = float(input("Enter Height :"))

area = 0.5 * base * height

print("The area of  Triangle is :", area, "\n")



# Write a Python Program to find area of a Square

side = float(input("Enter Side :"))

area = side ** 2

print("The area of Square is ::", area, "\n")



# Write a Python Program to Convert Celsius to Fahrenheit

celsius = float(input("Enter Celsius :"))

fahrenheit = (1.8 * celsius) + 32

print("Celsius to Fahrenheit is :", fahrenheit, "\n")



# Write a Python Program to Convert US Dollar to Indian Rupees

usd = float(input("Enter USD :"))
inr = usd * 80

print("The currency in INR is :", inr, "\n")



# Write a Python Program to Convert Liter to Mililiters

ltr = float(input("Enter Liter :"))

mltr = ltr * 1000

print("Liter to Mililiter is :", mltr, "\n")



# Enter binary, octal and hexadecimal values and convert it into decimal.

binary_value = "101010"
decimal_value_binary = int(binary_value, 2)
print("Binary Value ", binary_value ,"is equivalent to Decimal value ", decimal_value_binary)

octal_value = "55"
octal_value_binary = int(octal_value, 8)
print("Octal Value ", octal_value ,"is equivalent to Decimal value ", octal_value_binary)

hex_value = "1A"
hex_value_binary = int(hex_value, 16)
print("Hexadecimal Value ", hex_value ,"is equivalent to Decimal value ", hex_value_binary,"\n")



# Accept one integer value from the user; convert it to binary, octal and hexadecimal.

decimal_value = int(input("Enter an integer: "))

binary_value = bin(decimal_value)
octal_value = oct(decimal_value)
hexadecimal_value = hex(decimal_value)

print("Decimal :", decimal_value)
print("Binary :", binary_value)
print("Octal :", octal_value)
print("Hexadecimal :", hexadecimal_value,"\n")



# Accept string from the user (‘The Rajkot is a good city to leave’), and do the following
# operations: i). Display the first character of the string, ii). Display the first character of the string
# using negative index, iii). Display ‘Rajkot is a good city’. iv). Display the last character.

input_string = input("Enter a string: ")

first_character = input_string[0]
print("i). First character :", first_character)

first_character_negative_index = input_string[-len(input_string)]
print("ii). First character using negative index :", first_character_negative_index)

substring = input_string[4:24]
print("iii). Substring :", substring)

last_character = input_string[-1]
print("iv). Last character :", last_character,"\n")



#Create bytes, enter some values and display all elements.

my_bytes = bytes()

my_bytes += b'\x41'  
my_bytes += b'\x42'  
my_bytes += b'\x43'  

print("All elements in the bytes object:")
for element in my_bytes:
    print(element,"\n")



# Create bytearray, enter some values and perform the following: i). Replace the 3rd element with 7, 
# ii). Display the 5th element.

array = [2,7,8,11,75]
my_bytearray = bytearray(array)

my_bytearray[2] = 7

print("Updated bytearray:", my_bytearray)
print("5th element:", my_bytearray[4],"\n")



# Create list and insert values. i).Display all the elements. ii). Display the 3rd element,
# iii). Replace the 4th element with ‘Atmiya’, iv). Display elements from 3rd to 7th element.

list = [1,2,3,4,5,6,7,8,9,10]

print("(i). All Elements :", list)

print("(ii). 3rd Element :", list[2])

list[3]='Atmiya'
print("(iii). Replace 4 th Element with 'Atmiya' :", list)

print("(iv). Element from 3rd to 7th :", list[2:7],"\n")



# Create tuple and insert values. i). Try to replace the 3rd element with 9, ii). Display the 5th element.

t = (1,2,3,4,5)
lst = list(t)
lst[2] = 9
t = tuple(lst)
print("(i). Try to replace the 3rd Element with 9 :", t)

print("(ii). Display the 5th Element", t[4],"\n")



# Create a set insert some values. i). Add elements to it and display, ii). Remove elements from it and display.

set = {1,2,3,4,5}

set.add(6)
set.update({7})
print("(i). Set After adding Elements :", set)

set.remove(2)
set.discard(4)
print("(ii). Set After removing Elements :", set,"\n")



# Create a set insert some values and convert it to frozenset. Try to add and remove some elements.

set = {1,2,3,4,5}

frozenset = frozenset(set)
print(frozenset,"\n")



# Create an empty dictionary, Insert some Roll:Name into it. i). Retrieve 5th value using key, 
# ii). Retrieve all the roll numbers, iii). Retrieve all the names, iv). Change the name of the student
# having roll no. 7, v). Remove roll no 9, vi). Display the dictionary.

d = {}

d[1] = 'Mahesh'
d[2] = 'Viral'
d[3] = 'Viraj'
d[4] = 'Nilkanth'
d[5] = 'Chiranj'
d[6] = 'Renil'
d[7] = 'Ravish'
d[8] = 'Daksh'
d[9] = 'Ajay'

f = d.get(5)
print("(i). 5th Value is :", f)

lst = list(d.keys())
print("(ii). All Roll Numbers :", lst)

lst1 = list(d.values())
print("(iii). All Names :", lst1)

d[7] = 'Yatin'
print("(iv). After Change Name of Roll No. 7 :", d[7])

d.pop(9)
print("(v). After removing Roll No. 9 :", d)

print("(vi). Dictionary :", d,"\n")



# Create a list having names of months. i). Check whether December is in list or not, ii). Query the list using ‘not in’.

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

if "December" in months:
    print("(i). December is in List")
else:
    print("(i). December is not in the List")

if "June" not in months:
    print("(ii). June is not in List")
else:
    print("(ii). June is in the List \n")



# Take two integer values from the user using split(), perform basic arithmetic operation on the values.

a = input("Enter two integers separated by space :")
values  = a.split()

if len(values) != 2:
    print("Please Enter Exactly two integers")
else:
    num1 = int(values[0])
    num2 = int(values[1])

    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2

    print("Addition :", add)
    print("Subtraction :", sub)
    print("Multipliction :", mul)
    print("Divition :", div,"\n")

