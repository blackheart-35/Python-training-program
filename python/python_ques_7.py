''' Employee Bonus & Tax System** 
Concept:** Complex Business Logic. 
Task: Take an employee's `salary` and `years_of_service`. 
* If `years_of_service` > 10, give a 10% bonus**. 
* If `years_of_service` is between 5 and 10, give a **5% bonus
* After adding the bonus, check the **Total Amount**:
* If Total > 50,000, deduct 10% as tax.
* Else, deduct no tax.
* Print the final "In-Hand Salary". '''
#solution


a = int(input("Enter your salary: "))
b = int(input("Enter your years of service: "))

if b>10:
    c=a/10
    a=a+c
    if a>50000:
        d=a/10
        a = a-d
        print(a,"your salary after tax")        
    else:

        print(f"{a}you will recive 10% bonus")

elif b>=5 and b<=10:
    c=a/5
    a=a+c
    if a>50000:
        d=a/10
        a = a-d
        print(a,"your salary after tax")        
    else:

        print(f"{a}you will recive 5% bonus")


else:
    print(a,"your salary")