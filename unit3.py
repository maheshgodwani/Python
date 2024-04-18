# def odd_or_even(number):
# 	if number%2==0:
# 		print('the number is even')
# 	else:
# 		print('the number is odd')
# num1=int(input('ENTER THE NUMBER:-'))
# num2=int(input('ENTER THE NUMBER:-'))
# num3=int(input('ENTER THE NUMBER:-'))
# num4=int(input('ENTER THE NUMBER:-'))
# #calling the function
# odd_or_even(num1)
# odd_or_even(num2)
# odd_or_even(num3)
# odd_or_even(num4)


# # diff taking input before defination and taking input while calling the function


# to check whether entered number is positive,negative or zero
# def pos_neg_zer(num):
# 	if num<0:
# 		print('the entered number is negative') 
# 	elif num==0:
# 		print('the entered number is zero')
# 	else:
# 		print('the entered number is positive')
# #calling the function
# num=int(input('enter the number to check: '))
# pos_neg_zer(num)			

#returning multiple values from a function
# #to perform basic arithmatic operation
# def arithmatic(a,b):
# 	add=a+b
# 	sub=a-b
# 	mul=a*b 
# 	div=a/b 
# 	return add,sub,mul,div
# 	#calling the function
# a,s,m,d=arithmatic(10,10)
# print('the addition of two number is: ',a)
# print('the substraction of two number is: ',s)
# print('the multiplaction of two number is: ',m)
# print('the division of two number is: ',d)



#pass by object
#immutuable objects:integer, float,string,tuple
#mutable  objects:list



#program to pass an integer to a function 
# def modidify(a):
# 	a=7
# 	print('the value of a,in the body of function is',a,id(a))
# a=8
# print('the value of a,in the body of function is',a,id(a))
# 	#calling the function
# a=9
# modidify(a)
# print('the value of a,in the body of function is',a)


#	working with immutable objects
# lst=[1,2,3,4]
# def modify(lst):
# 	lst.append(7)
# 	print(lst,id(lst))
# modify(lst)
# print(lst,id(lst))

# #fromal and actual arguments
# def arith(a,b) ---> this is known as parameter
#     -----
#  #calling the function
#  s=10  --->this is known as argument
#  h=2   --->this is known as argument

#  		add=a+b
#  		sub=a-b
#  		mul=a*b
#  		div=a/b
#  		return add,sub,mul,div
#  	#calling the function
#  	a,s,m,d=arithmatic (10,2) ---> this is known as arguments
#  	#list of actual arguments (4 types):
#  	#1.positional arguments
#  	#2.keyword arguments
#  	#3.defaule argumnets
#  	#4.variable length arguments

#  	#1).positional arguments
#  	#-no .of parameter and their position must match with when calling the function
#  def conc(s1,s2):
#  	 combined=s1+s2
#  	  print(combined)
#  	#calling the function
# conc('atmiya','university')
# conc('marwadi','university','rajot')
# conc('rajkot')    	


# #2).keyword arguments
# def stud_det(enr,name):
# 	print('the enrollment of student is:',enr)
# 	print('the name of student is:',name)
# #callinhg the function
# student_det(enr=111,name='abc')
# student_det(name='abc',enr=111)	



# #3).default  arguments
# def stud_det(enr,name='abc'):
# 	print('the enrollments of student is:',enr)
# 	print('the name of student isL',name)
# #callijngthe function
# stud_det(enr=111,name='cde')
# stud_det(enr=111)	

#4).variable arguments
# def add1(farg,*args):
# 	print('formal arguments is',farg)
# 	sum=0
# 	for i in args:
# 		sum=sum+i
# 		print('the sum of all numbers:',(farg+sum))
# #calling the function
# add1(2,3)
# add1(2,3,4)
# add1(2)	

# #4).passing group of elements in a function
# def display(lst):
# 	for i in lst:
# 		print(i)

# print('enter elements separted by space: ',end='')
# lst=[i for i in input().split()]
# #calling the function
# display(lst)		


#anonymous function (also known as lambda)
#normal function
# def square(a):
# 	return a*a

# square=lambda a:a*a
# a=int(input('enter the number to know its square: '))
# print('the square of enter number is:',square(a))

#DATE-:18-03-2024
#---------------------------

#GENERATORS
#GENERATORS ARE FUNCTION THAT RETUREN A SEQUENCE OF VALUES
#GENERATORS FUNCATION ARE WRITTEN SAME AS ORDINARY FUNCTION
#IT USES 'YIELD'STATMENT
#THE YIELD STATEMENT IS USEFULT TOSTEUREN THE VALUE.

#EXAMPLE:- CREATE A GENERATORS THE RETUENS A SEQUENCE OF NUMBER FROM A

# def generator1(a,b):
# 	while a<=b:
# 		yield a
# 		a=a+1
#FILLING THE GENERATORS OBJECT
#gen=generator1(1,10)
#DISPLAYING THE VALUES
# for i in gen:
# 	print(i,end='')
#PRINT(NEXT(GEN))
#gen=generator1(1,10)		

#UNIT-3 SECOND TOPIC
#----------------------------
#FILE HANDLING
# 1.TEXT FILEES
# 2.BINARY FILES
# open() will be used to open file
# THIS FUNCTION ACCEPETS 'FILENAME'AND 'OPENMODE' TO OPEN THE FILE
# EXAMPLE:-
# file handler
#w:- to write data into the file if any data is alrady present in the file it would be delete and the new data will stored
#r:-to read data from the file the file pointer is always positioned the beginning od the file
#a:-to append data the file it will help to append the new data after the existing data file pointer is placed at the end of the file. if the is not avileble ,then it will be creted
#x:- to opened the file in exclusive creation mode the file creation will be filed the file alraedy exites
#r+:-withen w,r,a willallow both reading and writing
# file handler=open('filename','openmode')


#close()
# to crate a text file and store some data into it
# #create a file
# f=open('myfile.txt','w')
# #open a file
# #f=open('myfile.txt')
# #writing data ito the file by accepting it fromthe user
# st1=input('ENTER THE TEXT YOU WANT TO WRITE INTO THE FILE')
# f.write(st1)
# #closeing file
# f.close()


#reding the exitsing file
# f=open('myfile.txt','r')
# str1=f.read()
# #display the data on screen
# print(str1)
# f.close()


#append into an existing file
# f=open('myfile.txt','a+')
# str1=input('ENTER THE TEXT YOU WANT TO APPEND:')
# while str1!='$':
# 	#str1=input()
# 	if(str1!='$'):
# 		f.write(str1)
# 		break
# f.close()
# f=open('myfile.txt','r')
# str=f.read()
# print(str)
# f.close()


#knowing whether a file exists or not
#the opreting system os module as sub module name 'path'
#which has a method is file()
#it is used to check whether the file really exist or not

#to check whether the file is avalebile or not if avilable open the file

# import os,sys
# #to enter the file name
# fname=input('ENTER THE FILE NAME TO OPEN:')
# if os.path.isfile(fname):
# 	f=open(fname,'r')
# 	str1=f.read()
# 	print(str1)
# 	f.close()		
# else:
# 	print(fname+'doesnot exist')
#reading the file
#str1=f.read()
#display on the screen
#print(str1)
#f.close()		

#counting number of lines,word,and characters if the file is available
# import os
# #taking the file name
# fname=input('ENTER THE FILE NAME TO OPEN:')
# if os.path.isfile(fname):
# 	f=open(fname,'r')
# else:
#     print(fname+'does not exist')
# #initialising counters and setting it zero
# #cl=cw=cc=0
# cl=0
# cw=0
# cc=0
# #reding lines from the file
# for line in f:
# 	words=line.split()
# 	cl=cl+1
# 	cw=cw+len(words)
# 	cc=cc+len(line)
# print('NUMBER OF LINE IN FILE IS:',cl)
# print('NUMBER OF word IN FILE IS:',cw)
# print('NUMBER OF characters IN FILE IS:',cc)
# f.close()


#working with binary files
#it stores data in the from od bytes.
#the mode to read the file is 'rb'
#the mode to write the file is 'wb'
#the read() will be used to read the data
#the write() will be used to write the data



#-----------------------------------------------
#DATE=20-3-24
#--------------------------------------------------

#to copy img an one file to another file
# to open the file in binary mode
# f=open('download.png','rb')
# f1=open('atmiya_logo.png','wb')
# #read bytes from f and write it to f1
# img=f.read()
# f1.write(img)
# #close the file
# f.close()
# f1.close()


#THE 'with' statement
#it can be used will opening the file
#the benefit of using 'with' is that,it takes care of closing the file which is opened
#FORMET
#    with open('file_name','open_mode') as file object:
#takeing data fromthe user and store in the from of binary file
#record_lenght=10  #record_lenght is a varibal ,in which we have stored 10
#opening the file in 'wb' mode
# with open('stationery_store.py','wb') as f:
# 	n=int(input('HOW MANY ITEMS YOU WANT TO ADD:-'))
# 	for i in range(n):
# 		stat_item=input('ENTER THE NAME OF stationery:-')
# 		lenght=len(stat_item)#to find the lenght of stationery method
# 		stat_item=stat_item+(record_lenght-lenght)*' '
# 		stat_item=stat_item.encode()
# 		f.write(stat_item)
# #reading the file
# with open('stationery_store.py','rb') as f:
# 	str1=f.read()
# 	print(str1.decode())
# 	print(str1)
# 	#print(type(str1))

#Zipping the content of file
# from zipfile import*
# #createing the file
# f=ZipFile('demo.zip','w',ZIP_DEFLATED)
# #ZIP_STORED:TO JUST ZIP THE FILE
# #adding files to be  zipped
# f.write('stationery_store.py')
# f.write('stationery_store.java')
# #closing the zip file
# f.close()

# #UNZIPING THE FILE
# from zipfile import*
# z=ZipFile('demo.zip','r')
# z.extractall('E:')

# with open('stationery_store','wb') as f:
# 	n=int(input('HOW MANY ITEMS YOU WANT TO ADD:-'))
# 	for i in range(n):
# 		stat_item=input('ENTER THE NAME OF stationery:-')
# 		lenght=len(stat_item)#to find the lenght of stationery method
# 		stat_item=stat_item.encode()
# 		f.write(stat_item)
# 		f.write("\n".encode())


#------------------------------------------------------------
#date:-22-03-24
#------------------------------------------------------------

#random  accesing the binary files (using mmap)
# the from of mmap is 'memory maped file'
#format
#  mm=mmap.mmap(f.fileno(),0)
#where f represents file object
#    fileno() is a file descriptor (on handle) used to access file or i/o)
#    0 represent the whole file to be readed
# to create a register in which name of student and their enr.no is stored
# with open('student_re.dat','wb') as f:
# 	n=int(input('EMTER THE NUMBER OF RECORED TO BE INSERTED :-'))
# 	for i in range(n):
# 		name=input('ENTER THE STUDENT NAME :-')
# 		enr=input('ENTER THE STUDENT ENR NO:-')
# 		name=name.encode()
# 		enr=enr.encode()
# 		f.write(name+enr)

#IMP************************************************************
# #performing various operations on the file named student_re.dat
# import mmap,sys
# print('1. to view details of all the student :-')
# print('2. to view enr number of  the student passing his/her name:-')
# print('3. to modify the enrollment number od student :-')
# print('4. to exit')
# choice=int(input('enter your choise:-'))
# if choice=='4':
# 	sys.exit()
# with open('student_re.dat','r+b') as f:
# 	mm=mmap.mmap(f.fileno(),0)

# 	if(choice==1):
# 		print(mm.read().decode())
# 	if(choice==2):
# 		name=input('enter the name of student for which you want know the enr number:-')
# 		n=mm.find(name.encode())
# 		n1=n+len(name)
# 		en=mm[n1:n1+9]
# 		print('the enrollment of said student is: ',en.decode())
# 	if(choice==3):
# 		name=input('enter the name of student for which you want know the enr number:-')
# 		n=mm.find(name.encode())
# 		n1=n+len(name)
# 		en1=input('enter the modified enrollment number:-')
# 		mm[n1:n1+9]=en1.encode()
# mm.close()		


# --------------------------
# DATE-29/03/24
# --------------------------
# REGULAR EXPRESSION (ALSO KNOWN AS REGEX OR RE)	
#str='m\w\w'
#Exampal
# str1='this will be printed on the \nnewline'
# print(str1)
# str1=r'this will be printed on the \nnewline'
# print(str1)	

#using compile () of 're' module to compil the regular expression
# import re
# prog=re.compile(r'o\w\w')
# str1='net cat orr mat matter'
# result=prog.search(str1)
# print(result.group())# use of group(),to display the result
# str2='later orr sooner truth of man matter'
# result=prog.search(str2)
# print(result.group())

#create a regular expression to search for string starting with 'm' a having total 3 charcters using findall()
# import re
# str1='net cat mat m2atter'
# result=re.findall(r'm\w\w\w\w',str1)
# print(result)


#use of split()
#the split() spilt the given string into pieces according to the regular expression and returen
#the pieces as element of a list
#re.split(r'\w+',str1)
#here the 'capitel W' represent any non-alphanumeric
# import re
# str1='Hello! All,Good; morning'
# result=re.split(r'\W+',str1)
# print(result)


#create a regular expression that replaces a string with the new string
# import re
# str1='AITS is the best Organization'
# print(str1)
# result=re.sub(r'AITS','Atmiya Univarsity',str1)
# print(result)



# cerate a regular expression that finds the words starting with 's'.
# import re
# str1='Sun shine sooner or leter'
# result=re.findall(r's[\w]*',str1)
# print(result)


#--------------------------------------------------------------
#DATE:-30-03-2024
#--------------------------------------------------------------

# #CREATE REGULAR EXPRESSION THAT FINDS THE WORD STARTING WITH A NUMBER
# import re
# str1='the special classes are arranged on 11th and 21st of every month'
# result=re.findall(r'\d[\w]*',str1)
# print(result)



# #create a regular expression that retrieve the word having 5 charecter
# import re
# str1='Sun mon tues wedn thure frida stureday'
# result=re.findall(r'\b\w{5}\b',str1)
# print(result)


# #create a regular expression that retrieve the word having 4 or 5 charecter
# import re
# str1='Sun mon tues wedn thure frida stureday'
# result=re.findall(r'\b\w{4,5}\b',str1)
# print(result)

#create a regular expression that retrieve the word having 4 or more than 4and less than or 7 charecter
# import re
# str1='Sun mon tues wedn thure frida stureday'
# result=re.findall(r'\b\w{4,6}\b',str1)
# print(result)


#create a regular expression that reteive the word having 2,4 or by max 6 characters
# import re
# str1='Su mon tues wedn thure frida stureday'
# result=re.findall(r'\b\w{2,6}\b',str1)
# print(result)

#---------------------------------------------------
#date:-01-04-24
#------------------------------------------------------
#create a regular expression hat retrive the  wrods having 2,34 or more upto 6 character 
#import re
#str1='sun mun tues wen thrus fri stu '
#result=re.findall(r\b\w{2,6}',str1)
# print result

#create a regular expression that retrive only string digit number form the string
#import re
#str1='sun mun tues wen thrus fri stu '
#result=re.findall(r\b\d\w{2,6}',str1)
# print result


#create a regular ecpression whic retrive laty word of the string if it starts with '# import r# str1='seven eight nine seventeen# result=re.findall(r'\As[\w]*',str1# print(result)

#first character start with s
#import re
#str1='seven eight nine seventeen'
# result=re.findall(r'\As[\w]*',str1)
# print(result)

#create a regular experession to retrieve the enr number of the student
#  import re
#  str1='abc 1234'
#  result=re.findall(r'\W+',str1)
#  print(result)


#create a regular experession to retrieve the last word of a string of it startwith 's'
# import re
# str1='summer sun strong stunning strom small smell'
# result=re.findall(r's[tm][\w]*',str1)
# print(result)


#----------------------------------------------------------------
#Date:-02-04-24
#--------------------------------------------------------------

#create a regular experession to retrieve the enr number of the student
# import re
# str1='abc 1234'
# result=re.findall(r'\d+',str1)
# print(result)

#create a regular experession to retrieve the word that starts withe 'su'.
# import re
# str1='rose smells like a rose sun shine like a sun star'
# result=re.findall(r'su[\W+]*',str1)
# print(result)

#create a regular experession to retrieve the word that starts withe 'su'.
# import re
# str1='rose smells like a rose sun shine like a sun star'
# result=re.findall(r'rose[\W+]*',str1)
# print(result)

#create a regular expression to retreaive only the birthdate of the candidate
# import re
# str1='001 abc 1-10-1999,002 cde 21-10-1980,003 efg 12-11-80'
# result=re.findall(r'\d{1,2}-\d{1,2}-\d{2,4}',str1)
# print(result)

#Special chareacter in regular Expression
#CReatev a regular expression to serch whether the string starting with 'at' or not
# import re 
# str1='Atmiya University'
# result=re.search(r'^At',str1)
# if result:
# 	print( str1,'the str1 starts with At')
# else:
# 	print(str1,'the str1 does not starts with At')


#CReatev a regular expression to serch whether the ending with 'ty' or not
# import re 
# str1='Atmiya University'
# result=re.search(r'ty$',str1)
# if result:
# 	print( str1,'the str1 end with ty')
# else:
# 	print(str1,'the str1 does not end with ty')

# #create a regilar expression to retreve the price of the product
# import re
# str1='the pen is of rs. 10 pencilt of rs.2 and the reaser is of rs.5'
# result=re.findall(r'\d{1,3}',str1)
# print(result)


# import re
# str1='the pen is of rs. 10 pencilt of rs.2 and the reaser is of rs.5'
# result=re.findall('[1-10]',str1)
# print(result)


# import re
# str1='ATMIYA'
# result=re.findall('[A-Z][a-z]*',str1)
# if result:
# 	print(str1,'In the string the first charechter  is capital and rest others are small charecters')
# else:
# 	print(str1,'First letter is not capital')


#CREATE A REGULAR EXPRESSION THAT EXTERCTS THE TIME
import re
str1='the result may be declared at 1am today or at 8pm tomorrw'
result=re.findall(r'\dam|\dpm',str1)
print(result)
