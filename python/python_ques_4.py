'''. Vowel or Consonant Detector
Concept:String Membership (`in`), String Methods. 
Task: Take a single character input. 
* If the input length is not 1 or not a letter, print "Invalid Input".
* If it is a vowel (a, e, i, o, u), print "Vowel".
* Otherwise, print "Consonant". '''

#Solution

a = str(input("Enter your number: "))
if len(a) == 1:
    if a == "a" or a=="e" or a=="i" or a=="o" or a=="u":
        print("its a vovel")
    else:
        print("it not a vovel ")

else:
    print("its length os too long")            



