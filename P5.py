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