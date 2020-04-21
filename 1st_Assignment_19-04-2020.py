#1st Assignment 19-04-2020
#Calculator Functions
#Muhammad Asim
#Roll No: PIAIC 138498
#Batch-7 AI Karachi

print("----------------------------------------------------------")
print("\t\t Mathematical Functions")
print("----------------------------------------------------------")

a = input('''Select Following Digit to Perform Mathematical Function:
\n1 for addition +
2 for subtraction -
3 for division /
4 for multiplication *
5 for modulus %
\nYou Enter: ''')
print("----------------------------------------------------------")

fnum=int(input("Please Enter 1st Number:  "))
snum=int(input("Please Enter 2nd Number:  "))

print("----------------------------------------------------------")

if a == '1':
    print("Addition of "+ str(fnum)+ " and "+ str(snum)+ " is : ",fnum+snum)

elif a == '2':
    print("Subtraction of "+ str(fnum)+ " and "+ str(snum)+ " is : ",fnum-snum)

elif a == '3':
    print("Division of "+ str(fnum)+ " and "+ str(snum)+ " is : ",fnum/snum)

elif a  == "4":
    print("Multiplication of "+ str(fnum)+ " and "+ str(snum)+ " is : ",fnum*snum)
  
elif a  == "5":
    print("Modulus of "+ str(fnum)+ " and "+ str(snum)+ " is : ",(fnum / snum * 100))
    
print("----------------------------------------------------------")    
    
