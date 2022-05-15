sport1='undefined'
faculty1='undefined'
players1='undefined'
coach1='undefined'
sport2='undefined'
faculty2='undefined'
players2='undefined'
coach2='undefined'
sport3='undefined'
faculty3='undefined'
players3='undefined'
coach3='undefined'
sport4='undefined'
faculty4='undefined'
players4='undefined'
coach4='undefined'
def adding_editing_the_record():
    global sport1
    global faculty1
    global players1
    global coach1
    global sport2
    global faculty2
    global players2
    global coach2
    global sport3
    global faculty3
    global players3
    global coach3
    global sport4
    global faculty4
    global players4
    global coach4
    sport1=input("please enter name of the sport")
    faculty1=input("please enter number of faculty members")
    players1=input("please enter numbers of players")
    coach1=input("please enter the name of the coach")
    sport2=input("please enter name of the sport")
    faculty2=input("please enter number of faculty members")
    players2=input("please enter numbers of players")
    coach2=input("please enter the name of the coach")
    sport3=input("please enter name of the sport")
    faculty3=input("please enter number of faculty members")
    players3=input("please enter numbers of players")
    coach3=input("please enter the name of the coach")
    sport4=input("please enter name of the sport")
    faculty4=input("please enter number of faculty members")
    players4=input("please enter numbers of players")
    coach4=input("please enter the name of the coach")
def edit_specific(i):
    global sport1
    global faculty1
    global players1
    global coach1
    global sport2
    global faculty2
    global players2
    global coach2
    global sport3
    global faculty3
    global players3
    global coach3
    global sport4
    global faculty4
    global players4
    global coach4
    if i==1:
        C=input("the attribute you want to edit")
        if C=='name':
            sport1=input("enter name of sport")
        elif C=='faculty':
            faculty1=input("enter number off faulty")
        elif C=='players':
            players1=input("enter number of players")
        elif C=='coach':
            coach1=input("enter name of coach")      
    elif i==2:
        C=input("the attribute you want to edit")
        if C=='name':
            sport2=input("enter name of sport")
        elif C=='faculty':
            faculty2=input("enter number off faulty")
        elif C=='players':
            players2=input("enter number of players")
        elif C=='coach':
            coach2=input("enter name of coach")            
    elif i==3:
        C=input("the attribute you want to edit")
        if C=='name':
            sport3=input("enter name of sport")
        elif C=='faculty':
            faculty3=input("enter number off faulty")
        elif C=='players':
            players3=input("enter number of players")
        elif C=='coach':
            coach3=input("enter name of coach")                                   
    elif i==4:
        C=input("the attribute you want to edit")
        if C=='name':
            sport4=input("enter name of sport")
        elif C=='faculty':
            faculty4=input("enter number off faulty")
        elif C=='players':
            players4=input("enter number of players")
        elif C=='coach':
            coach4=input("enter name of coach")      
    elif i>4:
        print("there are only four entities")   
def viewing_all():
    print("the name of the sport is",sport1)
    print("number of faculty members is",faculty1)
    print("the number of players is", players1)
    print("the name of the cooah is",coach1)
    print("the name of the sport is",sport2)
    print("number of faculty members is",faculty2)
    print("the number of players is", players2)
    print("the name of the cooah is",coach2)
    print("the name of the sport is",sport3)
    print("number of faculty members is",faculty3)
    print("the number of players is", players3)
    print("the name of the cooah is",coach3)
    print("the name of the sport is",sport4)
    print("number of faculty members is",faculty4)
    print("the number of players is", players4)
    print("the name of the cooah is",coach4)
def all_attributes_of_a_entity(n):
    if n==1:
        print("the name of the sport is",sport1)
        print("number of faculty members is",faculty1)
        print("the number of players is", players1)
        print("the name of the cooah is",coach1)
    elif n==2:
        print("the name of the sport is",sport2)
        print("number of faculty members is",faculty2)
        print("the number of players is", players2)
        print("the name of the cooah is",coach2)
    elif n==3:
        print("the name of the sport is",sport3)
        print("number of faculty members is",faculty3)
        print("the number of players is", players3)
        print("the name of the cooah is",coach3)
    elif n==4:
        print("the name of the sport is",sport4)
        print("number of faculty members is",faculty4)
        print("the number of players is", players4)
        print("the name of the cooah is",coach4)
    elif n>4:
        print("there are only four entities")
def search(B):
    if B==1:
        C=input("the attribute you want to search")
        if C=='name':
            print("the name of sport is",sport1)
        elif C=='faculty':
            print("the num;ber of faculty is",faculty1)
        elif C=='players':
            print("the number of players is",players1)
        elif C=='coach':
            print("the name of the coach is",coach1)      
    elif B==2:
        C=input("the attribute you want to search")
        if C=='name':
            print("the name of sport is",sport2)
        elif C=='faculty':
            print("the number of faculty is",faculty2)
        elif C=='players':
            print("the number of players is",players2)
        elif C=='coach':
            print("the name of the coach is",coach2)                                
    elif B==3:
        C=input("the attribute you want to search")
        if C=='name':
            print("the name of sport is",sport3)
        elif C=='faculty':
            print("the number of faculty is",faculty3)
        elif C=='players':
            print("the number of players is",players3)
        elif C=='coach':
            print("the name of the coach is",coach3)                                
    elif B==4:
        C=input("the attribute you want to search")
        if C=='name':
            print("the name of sport is",sport4)
        elif C=='faculty':
            print("the number of faculty is",faculty4)
        elif C=='players':
            print("the number of players is",players4)
        elif C=='coach':
            print("the name of the coach is",coach4)
    elif B>4:
        print("there are only four entities")
def main(m):
    if  m==1:
        return adding_editing_the_record()
    elif m==2:
        i=eval(input("enter the entity whose attribute you wish to edit"))
        edit_specific(i)
    elif m==3:
        return viewing_all()
    elif m==4:
        n=eval(input("the etity whose attributes you wish to view"))
        return all_attributes_of_a_entity(n)
    elif m==5:
        B=eval(input("the etity whose attributes you wish to view"))
        return search(B)
    else:
        ("there are only four options")
X=input("type'start'to start the pogram and 'exit' to exit it")
while X=='start':
    Y=eval(input("press 1 to add or edit the pogram 2 add or edit a single attribute of entity 3 to view all attrbutes 4 to view all atributes of a entity 5 to search"))
    while Y<6:
        main(Y)
        Y=eval(input("press 1 to add or edit the pogram 2 add or edit a single attribute of entity 3 to view all attrbutes 4 to view all atributes of a entity 5 to search"))
    X=input("type'start'to start the pogram and 'exit' to exit it")
