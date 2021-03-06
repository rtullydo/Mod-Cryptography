## Elliptic Add Algorithm
## Nick Bellinger
## Mod Cryptography
## 3/27/2019

import time
import FastInverseAlgorithm

# Given A, p, P, and Q, return R

start = time.time()

A = 1
p = 7

#P
x1 = 6
y1 = 5

#Q
x2 = 6
y2 = 5

def EllipticAdd(x1,y1,x2,y2,A,p):
    # P != Q && Q != P'
    def case1(x1,y1,x2,y2,p):
        temp1 = y2 - y1
        temp2 = x2 - x1
        m = (temp1 * FastInverseAlgorithm.FastInverse(temp2,p)) % p
        #m = temp1 * pow(temp2,p-2,p)  This works too.
        x3 = ((pow(m,2)) - x1 - x2) % p
        y3 = (m * (x1 - x3) - y1) % p
        print("R = (" + str(x3) + "," + str(y3) + ")")
        return x3,y3

    # P = Q
    def case2(x1,y1,x2,y2,A,p):
        m = ((3 * (pow(x1,2)) + A) * pow((2*y1),p-2,p)) % p
        x3 = ((pow(m,2)) - x1 - x2) % p
        y3 = (m * (x1 - x3) - y1) % p  
        print("R = (" + str(x3) + "," + str(y3) + ")")
        return x3,y3

    # Q = P'
    def case3():   
        R = '∞'   
        print("R = " + R)

    # Q = ∞
    def case4():   
        x3 = x1
        y3 = y1   
        print("R = (" + str(x3) + "," + str(y3) + ")")

    if x1 != x2 and y1 != (y2 - 2 * y2):
        case1(x1,y1,x2,y2,p)

    if x1 == x2 and y1 == y2:
        case2(x1,y1,x2,y2,A,p)

    if x2 == x1 and y2 == (y1 - 2 * y1):
        case4()
EllipticAdd(x1,y2,x2,y2,A,p)
end = time.time()

#Prints runtime of program
print("Runtime: " + str(end-start))