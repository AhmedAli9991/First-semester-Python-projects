'''
name:Ahmed Ali
reg no:SP29-BCS-096
class:1B
'''
'''
QUESTION-1
Write the functions with the following headers:
 # Return the reversal of an integer, e.g. reverse(456) returns # 654
def reverse(number):
 # Return true if number is a palindrome
def isPalindrome(number):
Use the reverse function to implement isPalindrome. A number is a palindrome if its reversal is
the same as itself. Write a program that prompts the user to enter an integer and reports whether
the integer is a palindrome.

'''
def reverse(number):
    x=str(number)
    y=x[::-1]
    z=int(y)
    return(z)
def isPalindrome(number):
    if number==reverse(number):
        return True
    else:
        return False
num=int(input("please enter number"))
x=reverse(num)
y=isPalindrome(num)
print(x)
print(y)

'''
QUESTION-2
Write a function capitalize (lower_case_word) that takes the lower case word and returns the
word with the first letter capitalized. E.g. print (capitalize ('word')) should print the word Word.
'''
def capitalize(word):
    a=word.title()
    return (a)
name=str(input("enter the name"))
print(capitalize (name))

'''
QUESTION-3
Given a non-negative integer n, print the nth Fibonacci number. Do this by writing a
function fib(n) which takes the non-negative integer n and returns the nth Fibonacci number. Use
the concept of recursion to complete fib(n)
'''
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    elif n==3:
        return 1
    elif  n>3:
        return fib(n-1)+fib(n-2)
n=int(input("please enter a non negative integer"))
x=fib(n)
print(x)
   
