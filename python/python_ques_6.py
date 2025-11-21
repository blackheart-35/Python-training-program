'''The Electricity Bill Calculator (Tiered Calculation)
Concept:** Cumulative Logic (The "Hard" part of `elif`). 
Task:** Calculate a monthly electricity bill based on units consumed: 
First 100 units:** Free ($0/unit). 
Next 100 units (101-200):** $5 per unit. 
Above 200 units:** $10 per unit. 
Task: If a user burns 250 units, the cost is: $(100 \times 0) + (100 \times 5) + (50 \times 10) =
1000$. Write the logic to handle this cumulative cost
'''

#Solution
a= int(input("enter the uniths"))
if a <=100:
    print("by the policy of  aap you electicty bill is free")

if a>100 and a<200:
    b=a-100
    print(b*5)
if a>=200:
    a=a-100
    b =a-100
    print(b*10 + 500)    