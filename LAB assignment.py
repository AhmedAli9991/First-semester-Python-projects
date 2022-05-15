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
X=input("Type 'start' to start the program and 'end' to end it")
while X=="start":
    Y=eval(input("press 1 to add or edit press any other number to view it the database"))
    while Y==1:
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
        Y=eval(input("press 1 to add or edit the database press any other to exit"))
    Z=eval(input("press 1 to view every attribute of every elements press 2 to search"))
    if Z==1:
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
    elif Z==2:
        A=eval(input("enter 1 to check all attributes of a element prees 2 to search a perticular attribute of a element"))
        if A==1:
            B=eval(input("please enter the number of that entity"))
            if B==1:
                print("the name of the sport is",sport1)
                print("number of faculty members is",faculty1)
                print("the number of players is", players1)
                print("the name of the cooah is",coach1)
            elif B==2:
                print("the name of the sport is",sport2)
                print("number of faculty members is",faculty2)
                print("the number of players is", players2)
                print("the name of the cooah is",coach2)
            elif B==3:
                print("the name of the sport is",sport3)
                print("number of faculty members is",faculty3)
                print("the number of players is", players3)
                print("the name of the cooah is",coach3)
            elif B==4:
                print("the name of the sport is",sport4)
                print("number of faculty members is",faculty4)
                print("the number of players is", players4)
                print("the name of the cooah is",coach4)
            elif B>4:
                print("there are only four entities")
        elif A==2:
            B=eval(input("enter the entity whose attributes you want to search"))
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
    X=input("enter 'start' to strat the porgram again enter 'end' to end the program")                
