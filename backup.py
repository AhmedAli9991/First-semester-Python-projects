#-----------------------------------------------------------------------------
import math
S=eval(input("please eneter leangth of a side"))
pi=3.14
A=(5*(S**2))/(4*math.tan(pi/5))
print("the area is",A)
#------------------------------------------------------------------------------
name=input("enter employee's name")
hours=eval(input("enter number of hours worked in a week"))
rate=eval(input("please enter hourly pay rate"))
fedral_tax=eval(input("enter fedral withholding tax"))
state_tax=eval(input("enter state witholding tax"))
total_pay=hours*rate
fedral_cut=total_pay*fedral_tax
state_cut=total_pay*state_tax
actual_pay=total_pay-fedral_cut-state_cut
print("employee's name",name)
print("hours worked",hours)
print("pay rate",rate)
print("deductions:")
print("     fedral withholding tax",fedral_cut)
print("     state witholding tax",state_cut)
print("net pay:",actual_pay)
#-------------------------------------------------------------------------------
integer=int(input("Enter integer"))
if integer%5==0 and integer%6==0:
    print("Is integer divisible by 5 and 6? True")
else:
    print("Is integer divisible by 5 and 6? False")
if integer%5==0 or integer%6==0:
    print("Is integer divisible by 5 or 6? True")
else:
    print("Is integer divisible by 5 or 6? False")
if integer%5==0:
    print("Is integer divisible by 5 or 6 but not both? True")
elif integer%6==0:
    print("Is integer divisible by 5 or 6 but not both? True")
else:
    print("Is integer divisible by 5 or 6 but not both? False")
#--------------------------------------------------------------------------------
import random
R1=int(random.randint(0,9))
R2=int(random.randint(0,9))
R3=int(random.randint(0,9))
digit1=int(input("please enter the first digit"))
digit2=int(input("please enter the first digit"))
digit3=int(input("please enter the first digit"))
if (R1,R2,R3)==(digit1,digit2,digit3):
    print("your award is 10,000")
elif digit1== R1 or R2 or R3 and digit2== R1 or R2 or R3 and digit3== R1 or R2 or R3:
    print("your award if 3,000")
elif digit1== R1 or R2 or R3 or digit2== R1 or R2 or R3 or digit3== R1 or R2 or R3:
    print("your award is 1,000")
else:
    print("better luck next time")
#----------------------------------------------------------------------------------    
import math
(x,y)=eval(input("Enter a point with two coordinates"))
distance=math.sqrt((x**2+y**2))
print(distance)
if distance<=10:
    print("point (x,y) is within the circle")
else:
    print("point (x,y) is not within the circle")

