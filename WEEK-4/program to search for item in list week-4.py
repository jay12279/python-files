#4. program to search for item in list

# Program to search for an item in a list using loop
# im using in keyword to search an item in list

numbers = [10, 20, 30, 40, 50]

item = int(input("Enter number to search: "))

found = False

for num in numbers:
    if num == item:
        found = True
        break #exists the loop no need to check if once found

if found:
    print(item, "is found in the list.")
else:
    print(item, "is not found in the list.")
