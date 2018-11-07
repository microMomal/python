# -*- coding: utf-8 -*-
"""
#Testasdfsdfds
Created on Sat Nov  3 14:42:49 2018

@author: USER
"""
#Part 1
print("Part 1")
def isPrime(n): 
    # Corner case 
    if (n <= 1): 
        return False
    # Check from 2 to n-1 
    for i in range(2, n): 
        if (n % i == 0): 
            return False
    return True  
print("isPrime(8)- ", isPrime(8))


def prime_factors(n):
    factors=[]
    d=2
    while(d*d<=n):
        while(n>1):            
            while n%d==0:
                factors.append(d)
                n=n/d
            d+=1            
    return factors 
print("Prime_factors(2058): ", prime_factors(2058))
print()


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
      break
    return factors
prime_factors(2058)


#Part 2
print("Part 2")
intersection = []
def intersect(s1, s2):
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            intersection.append(s1[i])
            i += 1
            j += 1
        elif s1[i] > s2[j]:
            j += 1
        else:
            i += 1
intersect([1, 3, 5, 20, 35, 40], [4, 5, 35, 40])
print(intersection)
print()


#Part 3
print("Part 3")
#correct one
def gregoryLiebniz(numIterations):
    total=0
    for i in range(1,numIterations):
        total += ((-1)**(i+1))/((2*i+1))
    value = 4*(1-total)
    print(value)
gregoryLiebniz(10000000)
print()


#Part 4
print("Part 4")
def jumpMaximum(list1):
    print(list1)
    max_val = 0
    first_val = list1[0]
    for i in range(0, len(list1)):
        if list1[i] > max_val:
            max_val = list1[i]
            max_val_idx = i
    list1[0]= max_val
    list1[max_val_idx]=first_val
    return list1
jumpMaximum([5,8,3,21,7,4,14])




 
           