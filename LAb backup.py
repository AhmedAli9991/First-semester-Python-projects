def add_all(n):
    global list1
    list1=[]
    for i in range(0,n):
        list1.append([])
        sport=input("please enter name of the sport")
        faculty=input("please enter number of faculty members")
        players=input("please enter numbers of players")
        coach=input("please enter the name of the coach")
        for j in (0,4):
            list1[i].append(sport)
            list1[i].append(faculty)
            list1[i].append(players)
            list1[i].append(coach)
    return list1
def add_specific_entity():
    i=eval(input("enter the entitiy's number"))
    for j in list1[i]:
        sport=input("please enter name of the sport")
        faculty=input("please enter number of faculty members")
        players=input("please enter numbers of players")
        coach=input("please enter the name of the coach")
        list1[i]=[sport,faculty,players,coach]
    return list1
def add_a_single_attribute():
    i=eval(input("enter the entitiy's number"))
    j=eval(input("enter the attributes number"))
    x=input("enter the new attribute")
    list1[i][j]=x
    return list1
def view_all():
    for i in list1:
        print("name of sport",i[0])
        print("number of faculty is",i[1])
        print("number of players is",i[2])
        print("name of coach",i[3])
def view_entity():
    x=eval(input("enter the entity whose attributes you wish to view"))
    k=x-1
    print("name of sport",list1[k][0])
    print("number of faculty is",list1[k][0])
    print("number of players is",list1[k][0])
    print("name of coach",list1[k][0])        
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
def main(a):
    if a==1 or a ==2 or a==3:
        if a==1:
            add_all(n)
        elif a==2:
            add_specific_entity()
        elif a==3:
            add_a_single_attribute()
    else:
        if a==4:
            view_all()
        elif a==5:
            view_entity()
        elif a==6:
            searh()
X=eval(input("press 1 to start the program or press any other to close it"))
n=eval(input("enter how many entities you want in database"))
while X==1:
    a=eval(input("press 1 to add or edit the pogram 2 to add to a single entity 3 add or edit a single attribute of entity 4 to view all attrbutes 5 to view all atributes of a entity 6 to search"))
    main(a)
    X=eval(input("press 1 to run the program  again or press any other to close it"))
