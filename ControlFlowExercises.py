print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a:

print(x[:5])
# this is slicing


print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:

for num in x:
    if num % 2 == 0:
        print(num)

print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:
for num in x:
    if num % 2 == 0:
        print(x[:5])

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:

names = [name.split()[0][0] for name in names]
print(names)

print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:
#x = [names.index("  ") for name in names]
#print(x)



print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]
names = [name.split()[0][0] + name.split()[1][0] for name in names]
print(names)

# A2c:


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = ([1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"])
new_lists = list(set(list_of_lists))
print(new_lists)

# A3a:


# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:

user_input = input("Please enter a number")
number = int(user_input)
if number > 100:
    user_input = input("Try again, please enter a number")
else:
    print("thank you")


print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:
