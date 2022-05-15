'''
made by: Ahmed Ali(SP19-BCS-096)
         Ahmed Raza(SP19-BCS-095)
'''
#add_all if the function that allows us to edit and add to the record
def add_all(n):
#the while loop prevents the program from adding more entities after the first run
    while n!=0:
        global list1
        global list2
        list2=[]
        list1=[]
        for i in range(0,n):
            list1.append([])
            list2.append([])
        n=0
#when a is 1 add to record all atributes of entities are assigned
    if a==1:
        for i in range (0,m):
            sport=input("please enter name of the sport")
            faculty=eval(input("please enter number of faculty members"))
            players=eval(input("please enter numbers of players"))
            area=eval(input("please enter the area of ground"))
            rate1=eval(input("please enter the pay for of players"))
            rate2=eval(input("please enter the pay for each faculty member"))
            rate3=eval(input("please enter the cost to mentain unit are of the ground"))
            cost1=players*rate1
            cost2=faculty*rate2
            cost3=area*rate3
            cost4=cost1+cost2+cost3
            for j in range(0,4):
                list1[i].append(sport)
                list1[i].append(faculty)
                list1[i].append(players)
                list1[i].append(area)
                list2[i].append(cost1)
                list2[i].append(cost2)
                list2[i].append(cost3)
                list2[i].append(cost4)
#when a is 2 all attributes of a single entity are added
    elif a==2:
        i=eval(input("enter the entitiy's number"))
        sport=input("please enter name of the sport")
        faculty=eval(input("please enter number of faculty members"))
        players=eval(input("please enter numbers of players"))
        area=input("please enter the area of ground")
        cost1=players*rate1
        cost2=faculty*rate2
        cost3=area*rate3
        cost4=cost1+cost2+cost3
        list1[i-1]=[sport,faculty,players,area]
        list2[i-1]=[cost1,cost2,cost3,cost4]
        return list1
        return list2
#when a is 3 only aingle attribute of an entity can be edit
    elif a==3:
        i=eval(input("enter the entitiy's number"))
        j=eval(input("enter the attributes number"))
        if j ==1:
            x=input("enter the new attribute")
            list1[i-1][j-1]=x
        else:
            x=eval(input("enter the new attribute"))
            list1[i-1][j-1]=x
            if j==2:
                cost1=x*rate1
                list2[i-1][j-2]=cost1
            elif j==3:
                cost2=x*rate2
                list2[i-1][j-2]=cost1
            elif j==4:
                cost3=x*rate3
                list2[i-1][j-2]=cost1
            cost4=cost1+cost2+cost3
            list2.append[i-1][3]=cost4
        return list1
        return list2
#view_all function allows us to view the whole reord
def view_all():
    for i in list1:
        print("name of sport",i[0])
        print("number of faculty is",i[1])
        print("number of players is",i[2])
        print("area of ground is",i[3])
        print()
    for i in list2:
        print("the total pay of players",i[0])
        print("the total pay for faculty",i[1])
        print("total cost for ground mentainance",i[2])
        print("total expense", i[3])
        print()
#view_entity allows us to view all attributes of an entity
def view_entity():
    x=eval(input("enter the entity whose attributes you wish to view"))
    k=x-1
    print("name of sport",list1[k][0])
    print("number of faculty is",list1[k][1])
    print("number of players is",list1[k][2])
    print("area of ground is",list1[k][3])
    print()
    print("total pay for players",list2[k][0])
    print("total pay for faculty",list2[k][1])
    print("total cost for ground mentainace",list2[k][2])
    print("total expense",list2[k][3])        
#searh function allows us to search the reord for purticular atribute of an entity
def searh():
    w=eval(input("do you wish to view from fist database or secomd"))
    if w==1:
        i=eval(input("enter the entity whose attributes you wish to view"))
        j=eval(input("enter the attribute which you wish to view"))
        i=i-1
        j=j-1
        if j==0:
            print("name of sport",list1[i][j])
        elif j==1:
            print("number of faculty is",list1[i][j])
        elif j==2:
            print("number of players is",list1[i][j])
        elif j==3:
            print("area of ground is",list1[i][j])
    elif w==2:
        i=eval(input("enter the entity whose attributes you wish to view"))
        j=eval(input("enter the attribute which you wish to view"))
        i=i-1
        j=j-1
        if j==0:
            print("total pay for players",list2[i][j])
        elif j==1:
            print("total pay for faculty",list2[i][j])
        elif j==2:
            print("total cost for ground mentainace",list2[i][j])
        elif j==3:
            print("total expenses",list2[i][j])        
        
#main allows us to call the functions and allows us to create a menu for the user
def main(a):
    if a==1 or a ==2 or a==3:
        add_all(n)
    elif a==4:
        view_all()
    elif a==5:
        view_entity()
    elif a==6:
        searh()
print(" ----------------------------------------------------")
print("| press[1] to startthe program or anyother to exit it|")
print(" ----------------------------------------------------")
X=eval(input(""))
print(" ------------------------------")
print("| how may enitities do you want|")
print(" ------------------------------")
n=eval(input(""))
m=n
#while loop allows us to run the program forever how long as we wish and prevents data of the previous run from being deleted
while X==1:
    print(" ----------------------------------------------------------------------------------------------")
    print("| press[1] to add to an entity                  press[2] to add or edit a single entity        |")
    print("| press[3] to add or edit a single attribute    press[4] to view all attributes of all entities|")
    print("| press[5] to view attribute of a entry         press[6] to search                             |")
    print(" ----------------------------------------------------------------------------------------------")
    a=eval(input(""))
    main(a)
    n=0
    print(" ----------------------------------------------------")
    print("| press[1] to startthe program or anyother to exit it|")
    print(" ----------------------------------------------------")
    X=eval(input(""))
