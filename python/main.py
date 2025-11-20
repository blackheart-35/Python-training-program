x = 4
result = x << 1
print(result) 


x = 4
result = x >> 1
print(result)  

a = 10
b = 20

# == equal
if a == 10:
    print("a == 10")
else:
    print("a is not 10")

# != not equal
if a != b:
    print("a != b")
else:
    print("a == b")

# > greater than
if b > a:
    print("b > a")
else:
    print("b <= a")

# < less than
if a < b:
    print("a < b")
else:
    print("a >= b")

# >= greater or equal
if a >= 10:
    print("a >= 10")
else:
    print("a < 10")

# <= less or equal
if a <= b:
    print("a <= b")
else:
    print("a > b")

# and
if a == 10 and b == 20:
    print("Both conditions (AND) are true")
else:
    print("AND condition is false")

# or
if a == 10 or b == 0:
    print("At least one condition (OR) is true")
else:
    print("OR condition is false")

# not
if not (a == b):
    print("a is NOT equal to b (NOT)")
else:
    print("a is equal to b (NOT)")
