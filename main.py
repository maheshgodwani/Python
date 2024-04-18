#1 Write a program that prints your name and your college name.
print("Mahesh")
print("Atmiya University \n")

#2) Write a program that prints your address with name, all in new lines

print("Mahesh Morbi \n")

#3) Write a program that accept two numbers and perform all basic mathematical operations.
a=5
b=7

print("Addition :",a+b)
print("Subtraction :",a-b)
print("Multiplication :",a*b)
print("Division :",a/b,"\n")

#4) Write a program to calculate simple interest.

p=1000
r=10
n=1

print("Simple Interest : ",p*r*n/100,"\n")

#5) Write a program to calculate 10% bonus of salary.
salary = 5000
res = (salary*10)/100;
print("10% bonus of salary is ",res,"\n")

#6) Write a program to convert KM into Meter
km = 5
meter = km * 1000
print("km to meter is ", meter,"\n")


#7) The distance between two cities is input through keyboard. Write a program to convert and
#   print this distance in feet, meter, inch and centimeter.

km = float(input("Enter Distance between two cities : "))
feet = km * 3280.8
meter = km * 1000
inch = km * 39370.07
centimeter = km * 100000

print("KM to feet is ", feet)
print("KM to meter is ", meter)
print("KM to inch is ", inch)
print("KM to centimeter is ", centimeter)



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




# 1. Get the basic salary from the employee and display the net salary by calculating the following
# conditions: Applicable TA 4%, DA 30%, HRA 15% on basic salary. Applicable 3% tax, 12% PF on
# basic salary.

# print("\n\t SALARY PROGRAM \n")
# basic=float(input("Enter Basic Salary :"))
# da=float(basic*0.30)
# hra=float(basic*0.15)
# pf=float(basic*0.12)
# ta=float(basic*0.04)
# tax= float(basic*0.03)
# grosspay=float(basic+da+hra+ta)
# netpay=float(grosspay-pf-tax)

# print("\n==============================================")
# print(" BASIC SALARY : ",basic)
# print(" DEARNESS ALLOW. : ",da)
# print(" HOUSE RENT ALLOW.: ",hra)
# print(" TRAVEL ALLOW. : ",ta)
# print("==============================================")
# print("\n==============================================")
# print(" GROSSO PAYMENT : ",grosspay)
# print(" PROVIDENT FUND : ",pf)
# print(" TAX            : ",tax)
# print("==============================================")
# print("\n==============================================")
# print(" NET SALARY PAY : ",netpay)
# print("==============================================")



# 2. Get the marks of 5 subjects at the command line and display the total of marks, and percentage.

# print("\n\tEnter marks of five subjects\n")
# print("==============================================")
# S1=float(input("Subject 1 : "))
# S2=float(input("Subject 2 : "))
# S3=float(input("Subject 3 : "))
# S4=float(input("Subject 4 : "))
# S5=float(input("Subject 5 : "))
# print("==============================================")
# total = S1+S2+S3+S4+S5
# print("Total is ", total)
# print("==============================================")
# percentage = total * 100 / 500
# print("percentage is ", percentage)
# print("==============================================")



# 3. Rajkot Corporation wants to make simple application to calculate Water Bill of Rajkotians. Water
# is being delivered by the Corporation on per litre charges as below:
# Upto 90 litres – Rs. 0/ltr
# Upto 015 litres – Rs. 2/ltr
# Upto 250 litres – Rs. 5/ltr
# More than 250 – Rs. 10/ltr

# ltr = float(input("How many liter Water is consumed : "))
# if ltr <=90:
#     charges1 = ltr * 0
#     print("Amount to Pay is ", charges1)
# elif ltr>=90 and ltr<=150:
#     charges2 = ltr * 2
#     print("Amount to Pay is ", charges2)
# elif ltr>=150 and ltr<=250:
#     charges3 = ltr * 5
#     print("Amount to Pay is ", charges3)
# elif ltr>250:
#     charges4 = ltr * 10
#     print("Amount to Pay is ", charges4)



# 4. A tuition class owner wants to make a simple application to allocate grade to the students on
# the basis of marks student have scored. Accept marks from the students.
# Marks more than 90 – A1 grade
# Marks 80 or less than or equal 90 – A grade
# Marks 70 or less than or equal 80 – B1
# Marks 60 or less than or equal 70 – B
# Marks 50 or less than or equal 60 – Can do Better!
# Marks <50 – Need to work hard.


# marks = float(input("Enter Marks : "))
# if marks>90:
#     print("A1")
# elif marks>=80 and marks<=90:
#     print("A")
# elif marks>=70 and marks<=80:
#     print("B1")
# elif marks>=60 and marks<=70:
#     print("B")
# elif marks>=50 and marks<=60:
#     print("Can do Better!")
# elif marks<50:
#     print("Need to work hard.")



# 5. Income Tax department wants to make an application that calculates tax on the basis of the
# income. Accept yearly income earned by the taxpayer as an input and calculate tax to be paid.
# The tax slab is as below:
# Income up to 8 lakhs – No tax
# Income more than 8 lakh and less than 10 lakhs – 15% of income
# Income more than 10 lakhs and less than 20 lakhs – 20% of income
# Income more than 20 lakhs – 30% of income



# income=float(input('ENTER YOUR INCOME:-'))
# if income<800000:
# 	print('No tax')
# elif income>=800000 and income<1000000:
# 	tex1=float(income*0.15)
# 	print('Tax is ',+tex1)
# elif income>=1000000 and income<2000000:
# 	tex2=float(income*0.20)
# 	print('Tax is',+tex2)
# elif income>=2000000:
# 	tex3=float(income*0.30)
# 	print('Tax is ',+tex3)	



# 6. Accept two integer values in separate variable, display the small value and big value out of it.


# no1=int(input('ENTER THE FIRST NO:-'))
# no2=int(input('ENTER THE SECOND NO:-'))	
# if no1 < no2:
#     smaller = no1
#     bigger = no2
# else:
#     smaller = no2
#     bigger = no1

# print("Smaller value:", smaller)
# print("Bigger value:", bigger)



# 7. Accept marks from 4 students, display which mark is highest among all.


# marks = []
# for i in range(4):
#     mark = int(input(f"Enter marks for student {i+1}: "))
#     marks.append(mark)

# highest_mark = max(marks)

# print("The highest mark among all students is:", highest_mark)



# 8. An online selling app wants to develop a application to calculate shipping charges on the
# purchase. Accept amount from the user and calculate the shipping charges.
# The shipping charges are as below:
# Shopping amount less than 1500 – The shipping charges is Rs. 100/-
# --Type the message: Please purchase (1500-amount) to avail shipping charge of Rs. 80/-
# --Please pay (amount+100)
# Shopping amount more than 1500 and less than 3000 – The shipping charges is Rs. 70/-
# --Type the message: Please purchase (3000-amount) to avail shipping charge of Rs. 50/-
# --Please pay (amount+70)
# Shopping amount more than 3000 – Free shipping + 7% discount on amount
# --Type a message: You saved (amount*7/100)
# --Please pay (amount – discount)



# amount = float(input("Enter the shopping amount: "))

# shipping_charges = 0
# discount = 0
# if amount < 1500:
#     shipping_charges = 100
#     discount = 0
# elif amount > 1500 and amount <= 3000:
#     shipping_charges = 70
#     discount = 0
# else:
#     shipping_charges = 0
#     discount = amount * 7 / 100

# if shipping_charges > 0:
#     message = f"Please purchase {max(1500-amount, 0)} to avail shipping charge of Rs. 80/-"
#     total_amount = amount + shipping_charges
# else:
#     message = f"You saved {discount}"
#     total_amount = amount - discount

# print(message)
# print(f"Please pay {total_amount}")


# 1. Accept two integer values from the user; display the number which is smaller and the number which is bigger.

# no1 = int(input('Enter Number 1 : '))
# no2 = int(input('Enter Number 2 : '))

# if no1 < no2:
# 	print(no1, 'is small Number')
# 	print(no2, 'is big Number')
# elif no2 < no1:
# 	print(no2, 'is small Number')
# 	print(no1, 'is big Number')
# else:
# 	print('Equal Number')



# 2. Accept one integer value from the user; check whether entered number is divisible by 5 or not.

# no = int(input('Enter Number : '))
# if no % 5 == 0:
# 	print(no, 'is divisible by 5')
# else:
# 	print(no, 'is not divisible by 5')



# 3. Accept one integer value from the user; check whether entered number is between 0-100 or not.

# no = int(input('Enter Number : '))

# if no>0 and no<100:
# 	print(no, 'is between 0-100')
# else:
# 	print(no, 'is not between 0-100')



# 4. Accept one integer value from the user; display the length of the entered number, also display
# that the entered number is of four digits or not.

# no = int(input('Enter Number : '))
# length = len(str(no))
# print('lenth of entered no is', length)

# if length == 4:
# 	print(no, 'is four digit Number')
# else:
# 	print(no, 'is not four digit Number')



# 5. Accept one integer value from the user; display appropriate day of the week.

# no = int(input('Enter Number : '))

# if no == 1:
# 	print('Monday')
# elif no == 2:
# 	print('Tuesday')
# elif no == 3:
# 	print('Wednesday')
# elif no == 4:
# 	print('Thursday')
# elif no == 5:
# 	print('Friday')
# elif no == 6:
# 	print('Saturday')
# elif no == 7:
# 	print('Sunday')
# else:
# 	print('Invalid Number')



# 6. Take choice from the user, and perform the arithmetic operation as per the choice.
# Choices: 1) Addition, 2) Subtraction, 3) Multiplication 4) Division

# no1 = int(input('\nEnter Number 1 : '))
# no2 = int(input('Enter Number 2 : '))

# print('\nEnter 1 for Addition')
# print('Enter 2 for Subtraction')
# print('Enter 3 for Multiplication')
# print('Enter 4 for Division')

# a = int(input('\nEnter Number of your choise : '))

# if a == 1:
# 	print('\nAddition is ', no1 + no2)
# elif a == 2:
# 	print('\nSubtraction is ', no1 - no2)
# elif a == 3:
# 	print('\nMultiplication is ', no1 * no2)
# elif a == 4:
# 	print('\nDivision is ', no1 / no2)
# else:
# 	print('\nInvalid Number')



# 7. Accept the string from the user; display the count of vowels and consonants.

# string_name = input("Enter String : ")
# vowels = "aeiouAEIOU"

# vowelcount = sum(string_name.count(vowel) for vowel in vowels)
# length = len(string_name)
# concount = length - vowelcount

# print("Vowel count is : ", vowelcount)
# print("Constraint count is : ", concount)



# 8. Accept one integer value from the user; display the table of it.

# no = int(input('Enter Number : '))

# for i in range(1,11):
#  	print(no, "*", i, "=", (no*i))



# 9. Display square and cube of numbers 1-10.

# for i in range(1,11):
# 	print('Square ',i,' = ',(i*i),' \tCube ',i,' = ',(i*i*i))



# 10. Accept string from the user; convert the string to upper case.

# str = input('Enter String : ')
# print(str.upper())



# 11. Display the following output using loop:
# 		i. 1 to 10
# 		ii. 10 to 1
# 		iii. 1 3 5 7 9
# 		iv. 2 4 6 8 10

# for i in range(1,11):
# 	print(i)

# for i in range(10,0,-1):
# 	print(i)

# for i in range(1,10,2):
# 	print(i)

# for i in range(2,11,2):
# 	print(i)



# 12. Print 1 2 4 8 16 32 64 128 256 512 1024

# sequence = 1
# for i in range(11):
#     print(sequence, end=" ")
#     sequence *= 2



# 13. Accept the number from the user; display the table of that number.

# no = int(input('Enter Number : '))

# for i in range(1,11):
#  	print(no, "*", i, "=", (no*i))



# 14. Accept numbers from the user; display the sum of the entered numbers.

# numbers = input("Enter Integer Number:- ")
# total = sum(int(num) for num in numbers)
# print("The sum of the entered numbers is:", total)



# 15. Accept numbers from the user; display the count of the entered numbers.

# number = input("Enter Integer Number:- ")
# count = len(number)
# print("The count of the entered numbers is:", count)



# 16. Accept numbers from the user; find and display number of zeros available in the number.

# number = input('Enter Number : ')
# zero = number.count('0')
# print("The number of zeros in the entered number is : ", zero)



# 17. Accept an integer from the user; tell user that whether entered number is even or odd.

		# Required output:
		# Enter the number: 7
		# 7 is an odd number
		# Do you want to check another number? Y
		# Enter the number: 2
		# 2 is an even number
		# Do you want to check another number? N

# while True:
#     number = int(input("Enter the number: "))
#     if number % 2 == 0:
#        	print(number, 'is even number')
#     else:
#        	print(number, 'is odd number')
        
#     another = input("Do you want to check another number? (Y/N): ")
#     if another.upper() != 'Y':
#     	break




# 1.Create a list containing several strings. Take input from the user (search string); display
whether entered string is available in the list or not.
string_list = ["apple", "banana", "orange", "grape", "pineapple"]
search_string = input("Enter a string to search in the list: ")
if search_string in string_list:
print(f"The string '{search_string}' is available in the list.")
else:
print(f"The string '{search_string}' is not available in the list.")



#2. Accept the string from the user; display the message whether the entered string is
palindrome or not.
def is_palindrome(string):
string = string.lower().replace(" ", "")
return string == string[::-1]
input = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(input):
print(f"The string is a palindrome.")
else:
print(f"The string is not a palindrome.")



#3. Accept the string from the user; display the string in the reverse order.
input = input("Enter a string: ")
reversed_string = input[::-1]
print("The string in reverse order is:", reversed_string)



# 4.Accept the string from the user; allow user to choose from the following options and
perform
# the task as per user’s choice. i). Convert to the upper case, ii). Convert to the lower case,
iii).
# Convert to the swap case, iv). Convert to the title case
def perform_operation(string, choice):
if choice == '1':
return string.upper()
elif choice == '2':
return string.lower()
elif choice == '3':
return string.swapcase()
elif choice == '4':
return string.title()
else:
return "Invalid choice"
input = input("Enter a string: ")
print("Options:")
print("1. Convert to uppercase")
print("2. Convert to lowercase")
print("3. Convert to swap case")
print("4. Convert to title case")
choice = input("Enter your choice (1/2/3/4): ")
result = perform_operation(input,choice)
print("Result:", result)



# 5.Allow users to enter multiple strings in the list; arrange the entered string into
alphabetical order and display.
def arrange_in_alphabetical_order(strings):
return sorted(strings)
list = []
num = int(input("Enter the number of strings you want to enter: "))
for i in range(num):
string = input(f"Enter string {i + 1}: ")
list.append(string)
sorted_strings = arrange_in_alphabetical_order(list)
print("Strings in alphabetical order:")
for string in sorted_strings:
print(string)



#6. Create a tuple and display it. Enter 25 at the third position and display it again.
my_tuple = (10, 20, 30, 40, 50)
print("Original Tuple:", my_tuple)
my_tuple = my_tuple[:2] + (25,) + my_tuple[2:]
print("Modified Tuple:", my_tuple)



#7. Create a dictionary named library with following keys (Bookid, Title, Author, Price,
Publisher).
# a. Display the dictionary, b. Display the name of Author, c. Display the Bookid
# d. Display the length of the dictionary, e. Update the price, f. Insert year as the new key
# and display the dictionary again.
library = {
"Bookid": "ISBN123",
"Title": "Python Programming",
"Author": "John Doe",
"Price": 29.99,
"Publisher": "PublisherX"
}
print("Dictionary:", library)
print("Author:", library["Author"])
print("Bookid:", library["Bookid"])
print("Length of Dictionary:", len(library))
# e. Update the price
library["Price"] = 39.99
library["Year"] = 2023
print("Updated Dictionary:", library)



#8. Create a numeric array and perform following operations on it: Add 2 to each elements,
# Subtract 3 from each element, Multiply each element with 3, Divide each element by 2,
Find
# max and min, find the average of all elements.
import numpy as np
array = np.array([10, 20, 30, 40, 50])
added_array = array + 2
subtracted_array = array - 3
multiplied_array = array * 3
divided_array = array / 2
max_value = np.max(array)
min_value = np.min(array)
average_value = np.mean(array)
print("Original Array:", array)
print("Array after adding 2:", added_array)
print("Array after subtracting 3:", subtracted_array)
print("Array after multiplying by 3:", multiplied_array)
print("Array after dividing by 2:", divided_array)
print("Maximum value:", max_value)
print("Minimum value:", min_value)
print("Average of all elements:", average_value)



# 9.Create a numeric array and do the following: append the element, pop the element,
insert an
# element at the desired postion, reverse the elements in the array, convert the array to list.
# # Importing array module
from array import array
array = array('i', [1, 2, 3, 4, 5])
num_array.append(6)
print("After appending 6:", num_array)
popped_element = num_array.pop()
print("Popped element:", popped_element)
print("After popping:", num_array)
num_array.insert(2, 10) # Inserting 10 at index 2
print("After inserting 10 at index 2:", num_array)
num_array.reverse()
print("After reversing:", num_array)
num_list = list(num_array)
print("Converted to list:", num_list)



#10. Create a numeric array and do the following: append the element, pop the element,
insert an
# element at the desired postion, reverse the elements in the array, convert the array to list.
# Importing array module
import array
num_array = array.array('i', [1, 2, 3, 4, 5])
num_array.append(6)
print("After appending 6:", num_array)
popped_element = num_array.pop()
print("Popped element:", popped_element)
print("After popping:", num_array)
num_array.insert(2, 10)
print("After inserting 10 at index 2:", num_array)
num_array.reverse()
print("After reversing:", num_array)
num_list = list(num_array)
print("Converted to list:", num_list)



# 11. Accept numeric elements from the user, store it to the array and display. Ask user to
enter
# search element. Display the position of the searched element.
def accept_elements():
elements = []
n = int(input("Enter the number of elements: "))
print("Enter the elements:")
for i in range(n):
element = float(input())
elements.append(element)
return elements
def display_elements(arr):
print("Elements in the array:", arr)
def search_element(arr, search_elem):
positions = [i for i, elem in enumerate(arr) if elem == search_elem]
if positions:
print("Positions of the searched element:", positions)
else:
print("Searched element not found in the array.")
def main():
elements = accept_elements()
display_elements(elements)
search_elem = float(input("Enter the element to search: "))
search_element(elements, search_elem)
if name == " main ":
main()



# 12. Take two arrays enter 5 digits in both arrays. Compare the corresponding element from each
# array and display only the bigger number.
def compare_arrays(arr1, arr2):
result = []
for num1, num2 in zip(arr1, arr2):
result.append(max(num1, num2))
return result
def main():
array1 = [int(input("Enter a digit for the first array: ")) for _ in range(5)]
array2 = [int(input("Enter a digit for the second array: ")) for _ in range(5)]
result = compare_arrays(array1, array2)
print("Result after comparison:", result)
if name == " main ":
main()



# 14.. Create a function to calculate the simple interest.
def calculate_simple_interest(principal, rate, time):
interest = (principal * rate * time) / 100
return interest
principal_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the interest rate (in percentage): "))
time_period = float(input("Enter the time period (in years): "))
simple_interest = calculate_simple_interest(principal_amount, interest_rate, time_period)
print("Simple Interest:", simple_interest)



# 15. Create a function to perform basic arithmetic operations on the number.
def arithmetic_operations(num1, num2):
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
# Avoiding division by zero
division = num1 / num2 if num2 != 0 else float('inf')
return (addition, subtraction, multiplication, division)
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
results = arithmetic_operations(number1, number2)
print("Addition:", results[0])
print("Subtraction:", results[1])
print("Multiplication:", result[2])



# 16. Accept multiple strings and store it into the list using function.
accept_strings():
strings_list = []
True:
string = input("Enter a string (or type 'done' to finish): ")
if string.lower() == 'done':
strings_list.append(string)
strings_list
strings = accept_strings()
print("List of strings:", strings)



# 17. Find the biggest number from three values using lambda.
value1 = float(input("Enter the first value: "))
value2 = float(input("Enter the second value: "))
value3 = float(input("Enter the third value: "))
biggest_number = max(value1, value2, value3, key=lambda x: x)
print("The biggest number is:", biggest_number)
# 18. Demonstrate the use of: i). break and ii). pass.
for i in range(1, 11):
if i == 5:
print("Breaking the loop at", i)
break
print("Current value:", i)



# 1.Create a file with file name sample.txt, accept some data from the user and store it in the file.

# f = open('sample.txt','w')
# str1 = input('Enter the text you want to write into the file : ')
# f.write(str1)
# f.close()



# 2.Display the data stored in the sample.txt file (created in question 1).

# f = open('sample.txt','r')
# str1 = f.read()
# print(str1)
# f.close()



# 3. Accept some data from the user and append it into the file sample.txt (created in question 1), also the data in the file.

# f = open('sample.txt','a+')
# str1 = input('Enter the text you want to append : ')
# while str1!='$':
# 	if(str!='$'):
# 		f.write(str1)
# 		break
# f.close()



# 4. Accept the file name from the user, check the availability of the file: i). If the file exists display
# the data on the screen, ii). If the file is not available, display the appropriate message.

# import os,sys
# fname = input('Enter the file name to open : ')
# if os.path.isfile(fname):
# 	f=open(fname,'r')
# 	str1 = f.read()
# 	print(str1)
# 	f.close()
# else:
# 	print(fname + ' dose not exist')



# 5. Accept the file name from the user, check the availability of the file:
# a. If the file exists, display: i). No. of characters, ii). No. of words and iii). No. of lines
# b. If the file does exist, than display the appropriate message.

# import os,sys
# fname = input('Enter the file name to open : ')
# if os.path.isfile(fname):
# 	f=open(fname,'r')
# 	cl=cw=cc=0
# 	for line in f:
# 		words = line.split()
# 		cl = cl+1
# 		cw = cw+len(words)
# 		cc = cc+len(line)
# 	print('Number of lines',cl)
# 	print('Number of Words',cw)
# 	print('Number of Characters',cc)
# 	f.close()
# else:
# 	print(fname + ' dose not exist')



# 6. Create and open the binary file with ‘with’ option. Store names of all the subjects you study in
# semester 2. Ask user to enter the subject number they wanted to see and display that subject
# name.

# Writing subjects to the binary file
# with open('sub.bin', 'wb') as f:
#     n = int(input('Enter Number Of Subjects in Sem - 2: '))
#     for i in range(n):
#         sub = input('Enter Subject of Sem - 2: ')
#         sub = sub.encode()  # Encode subject name to bytes
#         f.write(sub + b'\n')  # Add a newline character to separate subjects

# # Reading subjects from the binary file
# with open('sub.bin', 'rb') as f:
#     subjects = f.readlines()  # Read all lines from the file

# # Ask user to enter the subject number they want to see
# subject_number = int(input("Enter the subject number you want to see: "))
# if 1 <= subject_number <= len(subjects):
#     print(f"Subject {subject_number}: {subjects[subject_number - 1].decode().strip()}")
# else:
#     print("Invalid subject number")



# 7. Create a file named ‘img1’, store an image into it. Open another file named ‘img2’, copy the
# same image as in the file ’img1’. Also store both files into the zip file named ‘imp_img’.

# from zipfile import ZipFile

# # Open the image file for reading
# with open('img1.png', 'rb') as f:
#     img_data = f.read()

# # Open another file for writing and copy the image data
# with open('img2.png', 'wb') as f1:
#     f1.write(img_data)

# # Create a zip file and add both images to it
# with ZipFile('Imp_img.zip', 'w') as zip:
#     zip.write('img1.png')
#     zip.write('img2.png')



# 8. Create a file with ‘with’ option, name it as ‘marks.dat’.
# i). Accept subject name and marks from the user, store the data in the file.
# ii). Give three options to the user: a). To view whole file, b). Accept and edit the marks of a
# subject user want to change.
# iii). Exit

# import sys

# while True:
#     print('1. Enter Subject Name and Marks...')
#     print('2. Show the File...')
#     print('3. Edit Marks of a Subject...')
#     print('4. Exit')

#     ch = input('Enter Your Choice: ')

#     if ch == '1':
#         with open('marks.dat', 'a') as f:  # Open file in append mode
#             n = int(input('Enter Number Of Subjects You Want To Insert: '))
#             for i in range(n):
#                 sub = input('Enter Subject Name: ')
#                 mark = input('Enter Mark of Subject: ')
#                 f.write("{}: {}\n".format(sub, mark))
    
#     elif ch == '2':
#         try:
#             with open('marks.dat', 'r') as f:
#                 for line in f:
#                     print(line.strip())
#         except FileNotFoundError:
#             print("File 'marks.dat' does not exist.")
    
#     elif ch == '3':
#         subject_to_edit = input("Enter the name of the subject you want to edit: ")
#         new_mark = input("Enter the new mark for {}: ".format(subject_to_edit))
        
#         try:
#             with open('marks.dat', 'r') as f:
#                 lines = f.readlines()
    
#             with open('marks.dat', 'w') as f:
#                 for line in lines:
#                     if subject_to_edit in line:
#                         f.write("{}: {}\n".format(subject_to_edit, new_mark))
#                     else:
#                         f.write(line)
#         except FileNotFoundError:
#             print("File 'marks.dat' does not exist.")
    
#     elif ch == '4':
#         sys.exit()
    
#     else:
#         print("Invalid choice. Please choose a number from 1 to 4.")



# 9. Create a regular expression that:
# a). Identifies and display the string starting with ‘s’ and having 4 characters.
# b). Splits the string where some special characters are found.
# c). Display the word starting with number.
# d). Display the word having 3 or 4 or 5 characters.
# e). Display only the dates from the string.
# f). Create a string with name of the person and his Aadhar number, display only Aadhar
# number.
# g). Display all the words that starts with ‘at’ or ‘ap’.
# h). Check if the string starts with ‘at’ than display appropriate message and otherwise.

# import re

# # a) Identifies and display the string starting with 's' and having 4 characters
# str1 = "sparrows sing sweetly as they soar swiftly through the sky."
# result_a = re.findall(r'\bs\w{3}\b', str1)

# # b) Splits the string where some special characters are found
# str2 = "Hello!Iam MCAStudent. Iam Study In AtmiyaUniversity."
# result_b = re.split(r'\W+', str2)

# # c) Display the word starting with a number
# str3 = "1one two three four 5five"
# result_c = re.findall(r'\b\d\w*\b', str3)

# # d) Display the word having 3 or 4 or 5 characters
# str4 = "one two three four five. this is a number of one to five."
# result_d = re.findall(r'\b\w{3,5}\b', str4)

# # e) Display only the dates from the string
# str5 = "001 abc 02-03-2022, 002 bcd 04-12-2011, 003 efg 4-2-10"
# result_e = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', str5)

# # f) Display only Aadhar numbers from a string
# str6 = "abc 123456789012, bcd 234567890123, efg 1243567809"
# result_f = re.findall(r'\b\d{12}\b', str6)

# # g) Display all the words that start with 'at' or 'ap'
# str7 = "atmiya university android application"
# result_g = re.findall(r'\b[ap]t\w*\b', str7)

# # h) Check if the string starts with 'at' and display an appropriate message
# str8 = "atmiya university android application"
# result_h = "String starts with AT.." if re.match(r'at\w*', str8) else "Sorry, but the string does not start with AT.."

# # Display results
# print("a) Strings starting with 's' and having 4 characters:", result_a)
# print("b) Splitting the string where special characters are found:", result_b)
# print("c) Words starting with a number:", result_c)
# print("d) Words having 3 or 4 or 5 characters:", result_d)
# print("e) Dates from the string:", result_e)
# print("f) Aadhar numbers:", result_f)
# print("g) Words starting with 'at' or 'ap':", result_g)
# print("h) Check if the string starts with 'at':", result_h)



# 10. Do as directed:
# a). Name the package used to deal with data frame.
# b). Name the package used to deal with data .xlsx file.
# c). Name the function used to read the .csv file.
# d). Name the function used to read the .xlsx file.
# e). Name the function used to read the tuple.



# 11. Create a dictionary which stores (at least 10 records)empid, name, city, salary and perform
# following operations:
# a). Display first three records
# b). Display last five records
# c). Display only Name and City
# d). Display employee who belongs to Mumbai
# e). Display employee name who belongs to Mumbai
# f). Display employee whose salary is more than 25000

# import pandas as pd

# employees = {
#     101: {'name': 'John', 'city': 'New York', 'salary': 6000},
#     102: {'name': 'Alice', 'city': 'Los Angeles', 'salary': 75000},
#     103: {'name': 'Bob', 'city': 'Chicago', 'salary': 5000},
#     104: {'name': 'Emily', 'city': 'Houston', 'salary': 62000},
#     105: {'name': 'Michael', 'city': 'San Francisco', 'salary': 80000},
#     106: {'name': 'Sophia', 'city': 'Mumbai', 'salary': 7000},
#     107: {'name': 'David', 'city': 'Seattle', 'salary': 72000},
#     108: {'name': 'Emma', 'city': 'Mumbai', 'salary': 9000},
#     109: {'name': 'Daniel', 'city': 'Atlanta', 'salary': 8000},
#     110: {'name': 'Olivia', 'city': 'Mumbai', 'salary': 63000}
# }

# df = pd.DataFrame.from_dict(employees, orient='index')

# print('====================================================')
# print('1. Display First Three Records')
# print(df.head(3))
# print('====================================================')
# print('2. Display Last Five Records')
# print(df.tail(5))
# print('====================================================')
# print('3. Display Only Name And City')
# print(df[['name', 'city']])
# print('====================================================')
# print('4. Display employees who belong to Mumbai')
# mumbai_employees = df[df['city'] == 'Mumbai']
# print(mumbai_employees)
# print('====================================================')
# print('5. Display employee names who belong to Mumbai')
# mumbai_names = df.loc[df['city'] == 'Mumbai', 'name']
# print(mumbai_names)
# print('====================================================')
# print('6. Display employees whose salary is more than 25000')
# high_salary_employees = df[df['salary'] > 25000]
# print(high_salary_employees)



# 12. Create an xlsx file store marks of five subjects, plot the data on the bar graph.

# import pandas as pd
# import matplotlib.pyplot as plt

# # Sample data
# data = {
#     'subject': ['Math', 'Science', 'English', 'History', 'Geography'],
#     'marks': [85, 92, 78, 88, 90]
# }

# # Create a DataFrame
# df = pd.DataFrame(data)

# # Save DataFrame to Excel file
# df.to_excel('Mark.xlsx', index=False)

# # Read the Excel file
# df = pd.read_excel('Mark.xlsx')
# print(df)

# # Extract subject and marks data
# x = df['subject']
# y = df['marks']

# # Plot the data on a bar graph
# plt.bar(x, y, label="Mark Sheet")
# plt.xlabel('Subject')
# plt.ylabel('Marks')
# plt.title('Mark Sheet')
# plt.legend()
# plt.show()



# 13. Take five income source of the Government and display it on the pie chart.

# import pandas as pd
# import matplotlib.pyplot as plt

# # Sample data
# data = {
#     'source': ['Tax', 'Grants', 'Fees', 'Fines', 'Investment'],
#     'amount': [5000000, 3000000, 2000000, 1500000, 2500000]
# }

# # Create a DataFrame
# df = pd.DataFrame(data)

# # Save DataFrame to Excel file
# df.to_excel('Government.xlsx', index=False)

# # Read the Excel file
# df = pd.read_excel('Government.xlsx')
# print(df)

# # Extract source and amount data
# sources = df['source']
# amounts = df['amount']

# # Plot the data on a pie chart
# plt.figure(figsize=(8, 6))
# plt.pie(amounts, labels=sources, autopct='%1.1f%%', startangle=140)
# plt.title('Government Income Sources')
# plt.show()



# 14. Draw the line chart representing BSE (Bombay Stock Exchange) index in last 10 years.

# import matplotlib.pyplot as plt

# years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
# bsc = [89, 59, 74, 84, 85, 94, 16, 45, 36, 47]

# plt.plot(years, bsc, color='teal', label='BSE Index')
# plt.title("Bombay Stock Exchange")
# plt.xlabel('Years')
# plt.ylabel('BSE Index')
# plt.legend()
# plt.show()



# 15. Plot the grouped bar graph using the appropriate data.

# import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt

# # Employee id and their salary of Production department
# x = [101, 102, 105, 107, 110]
# y = [25000, 26000, 20000, 21000, 23000]

# # Employee id and their salary of QA department
# x1 = [103, 104, 106, 108, 109]
# y1 = [19000, 16000, 18000, 22000, 21000]

# # Define the width of the bars
# width = 0.35

# # Plot the grouped bar graph
# plt.bar([i - width/2 for i in x], y, width, label="Production Department", color="teal")
# plt.bar([i + width/2 for i in x1], y1, width, label="QA Department", color="yellow")

# # Add labels and title
# plt.xlabel('Employee Id')
# plt.ylabel('Employee Salary')
# plt.title('TCS')

# # Add tick marks for employee IDs
# plt.xticks([i for i in range(101, 111)])

# # Add legend and show the plot
# plt.legend()
# plt.show()
