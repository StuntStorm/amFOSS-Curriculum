import re

password = input("Enter Password : ")
eightletter = re.compile(r'[\w\d\s\W\D\S]{8,}')
upperCase = re.compile(r'[A-Z]+')
lowerCase = re.compile(r'[a-z]+')
Digit = re.compile(r'\d+')

if not eightletter.search(password):
    print("Password is not Strong!, Your Password need to have atleast 8 Character")
elif not upperCase.search(password):
    print("Password is not Strong!, Your Password need to have atleast one Uppercase Character")
elif not lowerCase.search(password):
    print("Password is not Strong!, Your Password need to have atleast one Lowercase Character")
elif not Digit.search(password):
    print("Password is not Strong!, Your Password need to have atleast one Digit")
else:
    print("Yes, Your Password is Strong!")
