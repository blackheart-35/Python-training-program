'''Basic Calculator with Error Handling.
Concept:** `if-elif-else`, Input Handling. 
Task:** Take two numbers and one operator (`+`, `-`, `*`, `/`) as input. Perform the operation. 
Crucial Step:** Handle the "Division by Zero" error using an `if` condition before performing
division. If the user tries to divide by 0, print "Undefined". '''

#Solution

a = int(input("Enter your first number: "))
b = int(input("Enter your second number:"))

c = input("which operation do you want: ")
if c == "+":
    print(a+b)
elif c == "-":
    print(a-b)

elif c == "*":
    print(a*b)

elif c =="/":
    if a ==0 or b==0:
        print("zernot allowed")
    else:

        print(a/b)

else:
    print("invalid input")   