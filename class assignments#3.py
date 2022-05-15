'''
name:Ahmed ALi
reg no:SP19-BCS-096
class:1B
'''
#Use nested loops that display the following patterns in four separate programs
#pattern(a)
for i in range(1,8):
    for a in range(1,i):
       print(a,end="")
    print()  
print()
#pattern(b)
for i in range(7,0,-1):
    for a in range(1,i):
        print(a,end="")
    print()
print()
#pattern(c)
m=1
for i in range(1,7):
    print(" "*(6-i),end="")
    for j in range(m,0,-1):
        print(j,end="")
    m+=1
    print()
print()   
#patten(d)
m=7
for i in range(1,7):
    print(" "*(i-1),end="")
    for j in range(1,m):
        print(j,end="")
    m-=1
    print()
print()
#pattern(e)
n=0
for i in range(0,6):
    for j in range(0,2):
        print("#",end=" "*n)
    n+=1
    print()
print()
#QUESTION-2
#a)Write a program that reads some integers between 1 and 100 and counts the occurrences of each.
list1=[]
num=int(input("enter number between 1,100"))
while 0<num<101:
    list1.append(num)
    num=int(input("enter number between 1,100"))
a=[]
for i in list1:
    if i not in a:
        a.append(i)
        count=list1.count(i)
        print(i,"occurs",count,"times")   
print()
'''
b- Given an integer n, create a two-dimensional array of size (n×n)(n×n) and
populate it as follows, with spaces between each character:
 The positions on the minor diagonal (from the upper right to the lower left
corner) receive 1.
 The positions above this diagonal receive 0.
 The positions below the diagonal receive
'''
n=int(input("give an integer"))
list1=[]
x=0
y=1
for i in range(0,n):
    list1.append([])
    for j in range(0,n-x-1):
        list1[i].append(0)
    list1[i].insert(n-x,1)
    for k in range(0,x):
        list1[i].append(2)
    x+=1
    y+=1    
for i in list1:
    for j in i:
        print(j,end="")
    print()    
        

    
        













