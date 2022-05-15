'''
made by: Ahmed Ali(SP19-BCS-096)
         Ahmed Raza(SP19-BCS-095)
'''
#add_all if the function that allows us to edit and add to the record
def add_all(n):
#the while loop prevents the program from adding more entities after the first run
    while n!=0:
        global list1
        list1=[]
        for i in range(0,n):
            list1.append([])
        n=0
#when a is 1 add to record all atributes of entities are assigned
    if a==1:
        for i in range (0,m):
            sport=input("please enter name of the sport")
            faculty=input("please enter number of faculty members")
            players=input("please enter numbers of players")
            coach=input("please enter the name of the coach")
            for j in range(0,4):
                list1[i].append(sport)
                list1[i].append(faculty)
                list1[i].append(players)
                list1[i].append(coach)
#when a is 2 all attributes of a single entity are added
    elif a==2:
        i=eval(input("enter the entitiy's number"))
        sport=input("please enter name of the sport")
        faculty=input("please enter number of faculty members")
        players=input("please enter numbers of players")
        coach=input("please enter the name of the coach")
        list1[i-1]=[sport,faculty,players,coach]
        return list1
#when a is 3 only aingle attribute of an entity can be edit
    elif a==3:
        i=eval(input("enter the entitiy's number"))
        j=eval(input("enter the attributes number"))
        x=input("enter the new attribute")
        list1[i-1][j-1]=x
        return list1
#view_all function allows us to view the whole reord
def view_all():
    for i in list1:
        print("name of sport",i[0])
        print("number of faculty is",i[1])
        print("number of players is",i[2])
        print("name of coach",i[3])
#view_entity allows us to view all attributes of an entity
def view_entity():
    x=eval(input("enter the entity whose attributes you wish to view"))
    k=x-1
    print("name of sport",list1[k][0])
    print("number of faculty is",list1[k][1])
    print("number of players is",list1[k][2])
    print("name of coach",list1[k][3])        
#searh function allows us to search the reord for purticular atribute of an entity
def searh():
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
        print("name of coach",list1[i][j])
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
X=eval(input("press 1 to start the program or press any other to close it"))
n=eval(input("enter how many entities you want in database"))
m=n
#while loop allows us to run the program forever how long as we wish and prevents data of the previous run from being deleted
while X==1:
    a=eval(input("press 1 to add or edit the pogram 2 to add to a single entity 3 add or edit a single attribute of entity 4 to view all attrbutes 5 to view all atributes of a entity 6 to search"))
    main(a)
    n=0
    X=eval(input("press 1 to run the program  again or press any other to close it"))
