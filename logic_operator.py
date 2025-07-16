#A simple calculator app
print("welcome to our simple calculator app")
print('''****************
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponential
6. Floor Division
**********************'''
)
print ("Enter two numbers to add")
#prompt a user for a number and store it
first_number = input("First Number:")
#prompt the user for number and store it 
second_number = input("Second Number:")
sum = float(first_number) + float(second_number)
print(f"{first_number} + {second_number} = {sum:.2f}")

print("**********************")
print("subtraction")

print ("Enter two numbers to subtract")
#prompt a user for a number and store it
first_number = input("First Number:")
#prompt the user for number and store it 
second_number = input("Second Number:")
sub = float(first_number) - float(second_number)
print(f"{first_number} - {second_number} = {sub:.2f}")

print("**********************")
print("Multiplication")

print ("Enter two numbers to multiply")
#prompt a user for a number and store it
first_number = input("First Number:")
#prompt the user for number and store it 
second_number = input("Second Number:")
mul = float(first_number) * float(second_number)
print(f"{first_number} * {second_number} = {mul:.2f}")

print("**********************")
print("Division")

print ("Enter two numbers to divide")
#prompt a user for a number and store it
first_number = input("First Number:")
#prompt the user for number and store it 
second_number = input("Second Number:")
div = float(first_number) / float(second_number)
print(f"{first_number} / {second_number} = {div:.2f}")

print("**********************")
print("Exponential")

print ("Enter two numbers to find the exponentials")
#prompt a user for a number and store it
first_number = input("First Number:")
#prompt the user for number and store it 
second_number = input("Second Number:")
exp = float(first_number) ** float(second_number)
print(f"{first_number} ** {second_number} = {exp:.2f}")

print("**********************")
print("Floor Division")

print ("Enter two numbers to get the floor division")
#prompt a user for a number and store it
first_number = input("First Number:")
#prompt the user for number and store it 
second_number = input("Second Number:")
floor = float(first_number) // float(second_number)
print(f"{first_number} // {second_number} = {floor:.2f}")

