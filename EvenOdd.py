"""Enter the number from the user and Depending on whether the number is 'EVEN' or 'ODD' ,
    Print out an Appropriate message to the user"""

num=int(input("Enter the number: "))
Check=num%2                               #checking number
if(Check%2==0):
    print("This number ",num," is Even number ")
else:
    print("This number ",num," is Odd number ")
