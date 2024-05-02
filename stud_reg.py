import mmap,sys
print('1. To view details of all the student : ')
print('2. To view enrollment number of the student by passing his/her name : ')
print('3. To modify the enrollment number of student : ')
print('4. To Exit : ')
choice = int(input('Enter Your Choice : '))
if choice == 4:
    sys.exit()
with open('student_register.dat','r+b')  as f:
    mm = mmap.mmap(f.fileno(),0)

    if(choice == 1):
        print(mm.read().decode())
    
    if(choice == 2):
        name = input('Enter the Name of student for which you want to know the enrollment number : ')
        n=mm.find(name.encode())
        n1 = n+len(name)
        en=mm[n1:n1+3]
        print('The enrollment of said student is : ',en.decode())
    
    if(choice == 3):
        name = input('Enter the Name of student for which you want to modify the enrollment number : ')
        n = mm.find(name.encode())
        n1 = n+len(name)
        en1 = input('Enter the modified enrollment number : ')
        mm[n1:n1+3] = en1.encode()
mm.close()
