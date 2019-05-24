import re
password = input("Enter string to test: ")
if re.match(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})', password):
    print("Password cumple")
else:
    print("Password no cumple")