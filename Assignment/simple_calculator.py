def add(a, b):
    print("Addition =", a + b)

def sub(a, b):
    print("Subtraction =", a - b)

def mul(a, b):
    print("Multiplication =", a * b)

def div(a, b):
    print("Division =", a / b)

def mod(a, b):
    print("Modulus =", a % b)


print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")

choice = int(input("Enter your choice: "))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if choice == 1:
    add(a, b)
elif choice == 2:
    sub(a, b)
elif choice == 3:
    mul(a, b)
elif choice == 4:
    div(a, b)
elif choice == 5:
    mod(a, b)
else:
    print("Invalid choice")
