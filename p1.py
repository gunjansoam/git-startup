# def multiplylist (mylist):
#     result = 1
#     for x in mylist:
#         result = result*x
#     return result
# list1 = [1,2,3]
# list2 = [1,3,5]
# print(multiplylist(list1))
# print(multiplylist(list2))
# import math
# def mog2(x):
#     return(math.mog10(x)
#     math.log10(2));
# def poweroftwo(n):
#     return(math.ceil(log(n)))
# def hcf(a,b):
#     if(b==0):
#         return a
#     else:
#         return hcf(b,a%b)
#     a=50
#     b=25
#     print("gcd of 50 and 25 is: " ,end="")
#     print(hcf(50,25))
# num = 13 
# if num > 1:
#     for i in range(2,int(num/2)+1):
#         if (num%i) == 0:
#             print(num,"is not the prime number")
#             break
#         else:
#             print(num,"is  the prime number")
# else:
#     print(num,"is not a prime number")   
# year = int(input("enter the year:"))
# if (year%4==0):
#     print("this is a leap year")
# else:
#     print("this is not a leap year")    
# first = int(input("enter the first number:"))
# second = int(input("enter the second number:"))
# print(first+seconnd)
# def si (p,t,r):
#     print(' the principle is',p)
#     print('the time period is',t)
#     print('the rate of intrest is',r)
#     si = (p*r*t)/100
#     print('the simple intrest is',si)
#     return si
# si(9,10,15)
# p = 1500
# t = 2
# r = 7.7
# a = p*(1+(r/100))**t
# ci = a-p
# print(ci)



# def ci(p,r,t):
#     amount = p*(pow((1+r/100),t))
#     ci = amount - p
#     print("Compond intrest is",ci)
# ci(30000,55.2,17)   
# def sum1(a,b):
#     return a+b
# a = int(input())
# b = int(input())
# print("sum of the number is:",sum1(a,b))
a,b = input().split()
output = int(a) + int(b)
print(" the sum is:",output)