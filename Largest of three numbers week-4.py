#2 Function to find the largest of three numbers

#here in this program i'm using if,elif,else statements to compare them


def largest(a, b, c): #will take 3 numbers as input
    if (a >= b) and (a >= c):
        largest_num = a
    elif (b >= a) and (b >= c):
        largest_num = b
    else:
        largest_num = c
    return largest_num

num1 = 100
num2 = 2589
num3 = 9

print("The largest number is:", largest(num1, num2, num3))
