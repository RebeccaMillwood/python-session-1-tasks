# Question 1:

first_int = input("enter a number ")
second_int = input("enter another number ")

print(type(first_int))

result = int(first_int) + int(second_int)

print(result)


first_float = input("enter a number ")
second_int = input("enter another number ")


result = float(first_float) + int(second_int) 

print(result)

# Question 2:

first_int = input("enter a number ")
second_int = input("enter another number ")

result = int(first_int) * int(second_int)

print(result)


first_float = input("enter a number ")
second_int = input("enter another number ")


result = float(first_float) * int(second_int) 

print(result)

# Question 3: 

kilometers = input("enter number of kilometers, e.g 10 ")

result_m = int(kilometers) * 1000
result_cm = int(kilometers) * 100000

print(f"{kilometers}km = {result_m}m")
print(f"{kilometers}km = {result_cm}cm")

kilometers = input("enter number of kilometers, e.g 10 ")

result_m = float(kilometers) * 1000
result_cm = float(kilometers) * 100000

print(f"{kilometers}km = {result_m}m")
print(f"{kilometers}km = {result_cm}cm")

# Question 4:

name = input("What is your name? ")
height = input("What is your height? (numbers only) ")

print(f"{name} is {height}cms tall.")
