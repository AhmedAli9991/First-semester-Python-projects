x=eval(input("press 1 to start program"))
while x==1:
    cost1=float(input("Enter cost of transport"))
    cost2=float(input("Enter cost of food"))
    cost3=float(input("Enter cost of hotel"))
    cost4=float(input("Enter cost of airport pickup"))
    cost5=float(input("Enter misileanious costs")) 
    y=eval(input("Additional costs"))
    count=0
    cost6=0
    while count<y:
        z=float(input("Enter extra cost"))       
        cost6+=z
        count+=1
    cost7=cost1+cost2+cost3+cost4+cost5+cost6    
    m=float(input("Enter percentage"))
    r1=(m/100)*cost1
    r2=(m/100)*cost2
    r3=(m/100)*cost3    
    r4=(m/100)*cost4
    r5=(m/100)*cost5
    r6=(m/100)*cost6
    r7=r1+r2+r3+r4+r5+r6
    a1=cost1+r1
    a2=cost2+r2
    a3=cost3+r3   
    a4=cost4+r4
    a5=cost5+r5
    a6=cost6+r6
    a7=a1+a2+a3+a4+a5+a6
    print()
    print("Original costs")
    print()
    print("cost of transport",cost1)
    print("cost of food",cost2)
    print("cost of hotel",cost3)         
    print("cost of airport pickup",cost4)
    print("missalenious costs",cost5)
    print("additional cost",cost6)
    print("total cost",cost7)
    print("percentage",m)
    print()
    print()
    print("percentage of cost")
    print()
    print("cost of transport",r1)
    print("cost of food",r2)
    print("cost of hotel",r3)         
    print("cost of airport pickup",r4)
    print("missalenious costs",r5)
    print("additional cost",r6)
    print("total cost added",r7) 
    print()
    print()
    print("final costs")
    print()
    print("cost of transport",a1)
    print("cost of food",a2)
    print("cost of hotel",a3)         
    print("cost of airport pickup",a4)
    print("missalenious costs",a5)
    print("additional cost",a6)
    print("total final cost",a7)
    x=eval(input("press 1 to start program"))
