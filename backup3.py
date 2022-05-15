import random
R1=int(random.randint(0,9))
R2=int(random.randint(0,9))
R3=int(
    random.randint(0,9))
print(R1,R2,R3)
lottery_ticket_no=int(input("please enter the three digit number"))
digit1=lottery_ticket_no//100
digit2=((lottery_ticket_no)-(digit1*100))//10
digit3=((lottery_ticket_no)-(digit1*100)-(digit2*10))
X=R1+R2+R3
if (R1,R2,R3)==(digit1,digit2,digit3):
    print("your award is 10,000")    
elif digit1== R1:
    if digit2== X-R2-digit1 or digit2==X-R3-digit1:
        if digit3==X-digit1-digit2:
            print("your award is 3,000")
elif digit1==R2: 
    if digit2== X-R1-digit1 or digit2==X-R3-digit1:
        if digit3==X-digit1-digit2:
            print("your award is 3,000")
elif digit1==R3: 
    if digit2== X-R1-digit1 or digit2==X-R2-digit1:
        if digit3==X-digit1-digit2:
            print("your award is 3,000")            
else:
    if digit1== R1 or R2 or R3:
        print("your award is 1,000")
    elif digit2== R1 or R2 or R3:
        print("your award is 1,000")
    elif digit3== R1 or R2 or R3:
        print("your award is 1,000")

