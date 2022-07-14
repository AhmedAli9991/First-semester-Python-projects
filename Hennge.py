
#name Ahmed Ali
#Email ahmedalibalti2000@gmail.com


def main():
    try:
        N = int(input(""))
        if(N<1 or N>100):
            return main()
        else:
            results=repeatForX(N)
            print("main",results)
            if("err" in results):
                print("as")
                return main()
            display(results)
    except  ValueError:
        return main()
    
def repeatForX(N):    
    try:
        if(N>0):
            X=int(input())
            if(X<1 or X>100):
                return ("err")   
            result = repeatForYn(X)
            print("X",result)
            if(result=="err"):
                return("err")
            return str(result)+" "+repeatForX(N-1)
        return ""
    except:
    	return ("err")


def repeatForYn(X):
    yn=(input())
    try:
        if(X>1):
            sums = square(yn,X,0)
            print("sums",sums)    
            if(sums=="err"):
                return ("err")
            else:
                print("sums",sums)
                return sums

        else:
            sqrt=int(yn)
            if(sqrt<-100 or sqrt>100) :
                return ("err")
            sqrt=sqrt*sqrt
            return sqrt
    except:
        return ("err")
   

def square(yn,X,Y):
    try:    
        if(" " not in yn):  
            integer=int(yn)
            Y=Y+1
            if(integer<-100 or integer>100 or Y!=X):
                return("err")
            elif(integer<1):
                integer=0
            return integer*integer
        
        index=yn.index(" ")

        integer=int(yn[0:index])
        if(yn[index+1]==" "):
            return("err")   
        elif(integer<-100 or integer>100):
            return("err")
        else:
            if(integer<1):
                integer=0
            yn=yn[index+1:len(yn)]
            return integer*integer+square(yn,X,Y+1)
    except:
        return ("err")
def display(string):
    if(" " not in string):  
        return ""
       
    index=string.index(" ")
    print(string[0:index])
    string=string[index+1:len(string)]
    return display(string)

    

if __name__ == "__main__":
    main()
