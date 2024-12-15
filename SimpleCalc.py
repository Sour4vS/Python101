x = float (input("enter the first number "))
op = input("Enter the operator ")
y = float (input("Enter the second operator "))

if op == "+":
    print(x+y)
elif op == "-":
    print(x-y)
elif op == "*":
    print(x*y)
elif op == "/":
    print(x/y)
else:
    print("invalid number")
