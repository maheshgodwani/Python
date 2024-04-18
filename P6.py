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
