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