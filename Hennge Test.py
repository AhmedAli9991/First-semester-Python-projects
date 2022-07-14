
#made by Ahmed Ali


def main():
    N = eval(input(""))
    if(N<1 or N>100):
        return main()
    
    results=repeatForX(N)
    display(results)

def repeatForX(N):    
    if(N>0):
        X=eval(input())
        if(X<1 or X>100):
            return repeatForX(N)    
        result = repeatForYn(X)
        return str(result)+" "+repeatForX(N-1)
    return ""

def repeatForYn(X):
    yn=(input())
    if(len(yn)>X+X-1+X*2 or len(yn)<X+X-1):
        repeatForYn(X)
    if(X>1):
        sums=square(yn,X)
        return sums
    else:
        sqrt=int(yn)
        sqrt=sqrt*sqrt
        return sqrt
    
def square(yn,X):
    if(" " not in yn):  
        integer=int(yn)
        if(integer<1):
            integer=0
        return integer*integer
       
    index=yn.index(" ")
    integer=int(yn[0:index])
    yn=yn[index+1:len(yn)]
    if(integer<-100 or integer>100):
        return(repeatForYn(X))
    if(integer<1):
        integer=0
    return integer*integer+square(yn,X)

def display(string):
    if(" " not in string):  
        return ""
       
    index=string.index(" ")
    print(string[0:index])
    string=string[index+1:len(string)]
    return display(string)

    
main()
