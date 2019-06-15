""" Write a program to ask the user to enter his name,
depending on that find the size of name and size is Even or odd.  """


name=input("Enter your name: ")
Size=len(name)
Check=Size%2                               #checking number
if(Check%2==0):
    print("This Name ",name," is of ",Size," letters and so, it is Even number ")
else:
    print("This Name ",name," is of ",Size," letters and so, it is Odd number ")

