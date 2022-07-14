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
