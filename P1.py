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
