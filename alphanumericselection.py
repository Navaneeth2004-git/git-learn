x=input("Enter the username ")
def validate_username(x):
    if x.isalnum() and 6 <=len(x)<= 15:
        print("valid username")
    else:
        print("invalid usename. Only alphabets and numbers, 6-15 characters long")
validate_username(x)