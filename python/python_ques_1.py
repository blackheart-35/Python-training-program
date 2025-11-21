'''Level 1: Basics & Data Type Operations 
1. The Variable Swap Logic
Write a program that takes two inputs, `a` and `b`. Swap their values without using a third variable
(if possible) or using a temporary variable, and print the result.''' 

#Solution

a = int(input("Enter your  Number: "))
b = int(input("Enter your  Number: "))

# a= a+b
# b= a-b
# a= a-b
# print("value 1: ",a)

# print("value 2: ",b)

a,b = b,a
print(a, b)


