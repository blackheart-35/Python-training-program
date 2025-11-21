'''The "Last Digit" Checker
Concept: Modulus Operator, Basic `If`. 
Task:** Take an integer input. Write a program to check if the **last digit** of the number is
divisible by 3. 
Hint Use `% 10` to isolate the last digit. '''

#Solution

a = int(input("enter the number :  "))

b = a%10
if (b%3==0):
    print("Number is devisible ")
else:
    print("Number is not divisible ")    
print(b)