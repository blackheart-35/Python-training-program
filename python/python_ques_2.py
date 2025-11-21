'''Time Converter (Modulus & Floor Division)** 
Concept:Arithmetic Operators (`//`, `%`). 
Task: Take an integer input representing a total number of seconds. Convert this into `Hours`,
`Minutes`, and `Remaining Seconds`. 
Example: Input `3665` $\rightarrow$ Output: `1 Hour, 1 Minute, 5 Seconds`. '''

#Solution
a = int(input("Enter number of seconds: "))

if a > 3600:
    hours = a // 3600
    minutes_01 = a % 3600
    minutes = minutes_01  // 60
    seconds = minutes_01 % 60
    print(f"{hours} Hours: {minutes} Minutes: {seconds} Seconds")
elif a < 3600:
    hours = 0
    minutes_01 = a % 3600
    minutes = minutes_01 // 60
    seconds = minutes_01 % 60
    print(f"{hours} Hours: {minutes} Minutes: {seconds} Seconds")

elif a <= 6:
    seconds = a
    hours = 0
    minutes = 0
    print(f"{hours} Hours: {minutes} Minutes: {seconds} Seconds")

