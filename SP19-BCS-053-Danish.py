
'''
Name: Muhammad Danish Butt
Reg no. SP19-BCS-053
'''
'''
Class Assignment-2
'''


#-------------------------------------------------------------------------------------------------------------

'''
Question no. 1
'''

import math
side = eval(input("Enter length of side of a Pentagon : "))
area = (5*(side)**2)/(4*math.tan(math.pi/5))
print ( "The Area of pentagon is" , area )

#---------------------------------------------------------------------------------------------------------------

'''
Question no. 2
'''

name = input("Employee’s Name: ")
user_num_of_hours = eval(input("Enter The user_number of Hours Worked In A Week: "))
hourly_pay_rate = eval(input("Enter Hourly Pay Rate: "))
federal_tax = eval(input("Enter Federal Tax Withholding Rate: "))
state_tax = eval(input("Enter State Tax Withholding Rate: "))


gross_pay = user_num_of_hours * hourly_pay_rate


deduction = (federal_tax*100) + (state_tax*100)

net_pay = gross_pay - deduction
print("\n")
print("Employee Name: " + str(name))
print("Pay Rate: $" + str(hourly_pay_rate) )
print("Gross Pay: $" + str(gross_pay))
print("Deduction:")
print("\t Fedreral Withholding: $" + str(federal_tax*100)) 
print("\t State Withhloding: $" + str(state_tax*100)) 
print("\t Total Deduction: $" + str(deduction))
print("Net Pay: $" + str(net_pay))

#--------------------------------------------------------------------------------------------------------------

'''
Question no. 3
'''

integer = eval(input("Enter an Integer: "))

remainder_5 = integer%5
remainder_6 = integer%6




if remainder_5 == 0 and remainder_6 == 0:
    print("Is" , integer , "divisible by 5 and 6? Ture")

else:
    print("Is" , integer, "divisible by 5 and 6? False")
if remainder_5 == 0 or remainder_6 == 0 :
    print("Is" , integer , "divisible by 5 or 6? True")
else:
    print("Is" ,  integer , "divisible by 5 or 6? False")
if remainder_5 == 0 and remainder_6 == 0 :
    print("Is" , integer , "divisible by 5 or 6, but not both? False")
elif remainder_5 == 0 or remainder_6 == 0 :
    print("Is" ,  integer , "divisible by 5 or 6, but not both? True")
else:
    
    print("Is" ,integer , "divisible by 5 or 6, but not both? False")

 
#-------------------------------------------------------------------------------------------------------------



'''
Question no.4
'''
'''
Lottery System
'''

import random

x='r'

while x=='r':
    ram_3digits=int(random.randint(100,999))
    
    user_num=int(input('Enter a 3 digit Number,Try Your Luck! : '))

    if user_num==ram_3digits:
        print("You have won 10,000$ Hurraaaaay!")
    else:
        ram_3digits3=int(ram_3digits%10)
        ram_3digits2=int(ram_3digits//10)%10
        ram_3digits1=int(ram_3digits//100)
        user_digit3=int(user_num%10)
        user_digit2=int((user_num//10)%10)
        user_digit1=int(user_num//100)
        condition1=1
        if user_digit1==ram_3digits1 and user_digit2==ram_3digits3 and user_digit3==ram_3digits2:
            print('You have won 3000$ Have Fun. The Number was', ram_3digits)
            condition1=0
        if user_digit1==ram_3digits2 and user_digit2==ram_3digits1 and user_digit3==ram_3digits3:
            print('You have won 3000$ Have Fun. The Number was', ram_3digits)
            condition1=0
        if user_digit1==ram_3digits2 and user_digit2==ram_3digits3 and user_digit3==ram_3digits1:
            print('You have won 3000$ Have Fun. The Number was', ram_3digits)
            condition1=0
        if user_digit1==ram_3digits3 and user_digit2==ram_3digits2 and user_digit3==ram_3digits1:
            print('You have won 3000$ Have Fun. The Number was', ram_3digits)
            condition1=0
        if user_digit1==ram_3digits3 and user_digit2==ram_3digits1 and user_digit3==ram_3digits2:
            print('You have won 3000$ Have Fun. The Number was', ram_3digits)
            condition1=0


        if condition1==1:
            condition2=1
            if user_digit1==ram_3digits1 or user_digit2==ram_3digits1 or user_digit3==ram_3digits1:
                print('Your one digit is correct!. You have won 1000$. It`s Still a Good Amount To Enjoy. The Number was', ram_3digits)
                condition2=0
            elif user_digit1==ram_3digits2 or user_digit2==ram_3digits2 or user_digit3==ram_3digits2:
                print('Your one digit is correct!. You have won 1000$. It`s Still a Good Amount To Enjoy. The Number was', ram_3digits)
                condition2=0
            elif user_digit1==ram_3digits3 or user_digit2==ram_3digits3 or user_digit3==ram_3digits3:
                print('Your one digit is correct!. You have won 1000$. It`s Still a Good Amount To Enjoy. The Number was', ram_3digits)
                condition2=0
            if condition2==1:
                print('Better Luck Next Time')
    x=str(input('Press r To Try Your Luck Again, Press X To Exit: '))    

    
#---------------------------------------------------------------------------------------------------------------------



'''
Question no.5
'''

import math

(x,y)=eval(input("Enter a Point With Two Coordinates: "))
distance=math.sqrt((x**2+y**2))

if distance<=10:
    print("The Point (" , x , "," , y , ") lies within the Circle")
else:
    print("The Point (" , x , "," , y , ") is not in the Circle")

#----------------------------------------------------------------------------------------------------------------------














