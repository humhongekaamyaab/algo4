'''
Problem Statement

A series is defined in the following manner:

Given the nth and (n+1)th terms, the (n+2)th can be computed by the following relation 
Tn+2 = (Tn+1)2 + Tn

So, if the first two terms of the series are 0 and 1: 
the third term = 12 + 0 = 1 
fourth term = 12 + 1 = 2 
fifth term = 22 + 1 = 5 
... And so on.

Given three integers A, B and N, such that the first two terms of the series (1st and 2nd terms) are A and B respectively, compute the Nth term of the series.

Input Format

You are given three space separated integers A, B and N on one line.

Input Constraints 
0 <= A,B <= 2 
3 <= N <= 20

Output Format

One integer. 
This integer is the Nth term of the given series when the first two terms are A and B respectively.

Note

Some output may even exceed the range of 64 bit integer.
Sample Input

0 1 5  
Sample Output

5
Explanation

The first two terms of the series are 0 and 1. The fifth term is 5. How we arrive at the fifth term, is explained step by step in the introductory sections.

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
k = map(int,raw_input().split())
tn1 = k[0]
tn2 = k[1]
n = k[2]
k = 2
while n != k:
    tn3 = tn2**2 + tn1
    tn1 = tn2
    tn2 = tn3
    k += 1
print tn3
