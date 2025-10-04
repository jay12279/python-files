#Fibonacci Sequence
#Defines as a sequence of numbers where each term equals the sum of the two previous terms
#The formula that i'm using for displaying the sequence Fn=Fn-1 + Fn-2

#Fibonacci sequence print the first n terms

n = int(input("How many terms:"))

a, b=0, 1 # start with F0=0 and F1=1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
