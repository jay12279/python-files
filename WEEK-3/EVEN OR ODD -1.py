#1.checking if the number is even or odd

Number= int(input("Enter the Number:"))

if Number %2==0: #%2 is the modulas operator remainder 
    print("The Number is Even.") #if the remainder is 0 it is even 
else:
    print("The Number is Odd") #if the reminder is not 0 it is odd
