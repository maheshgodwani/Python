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

