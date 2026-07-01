#Nested If
#****PASSWORD CHECKING*****
#Mainly user should whether his name is correct else and also password
#1) List + membership operator checking
l1 = ["sneha","rashmi","jitesh","ragu"]
name = input("Enter the Name of the user\n")
if name in l1:
    l2 = [1234,3453,5234,6754]
    password = int(input("Enter the password\n"))
    if password in l2:
        print("Password is correct")
        print("***Login Successful***")
    else:
        print("Invalid password")
else:
    print("Wrong username")

#2) Dict + membership operator
dict1 = {"sneha":1234,"rashmi":3453,"raghu":5234,"jayram":6674}
name = input("Enter the name\n")
if name in dict1:
    password = int(input("Enter the password:\n"))
    if password == dict1[name]:
        print("Login Successful\n")
    else:
        print("Invalid Password\n")
else:
    print("Wrong username")

#3)Using Membership +Identity+Nested if+ Match Case
users_info = {"sneha":1234,"rashmi":4567,"sejal":7834,"vaish":6789}
print("****** Login System ******")
name = input("Enter the username:\n")
if name in users_info: #membership operator
    password = int(input("Enter the user's password:\n"))
    match password:
        case p if p == users_info[name]: #guarded case
            login = True
            #Identity operator
            if login is True:
                role = "Use_r"
                if role == "Use_r":
                    print("password Correct")
                    print("You are ready to go ", name)
                    print("*** Login Successful ***")
        case _:
            print("Invalid password")
else:
    print("Invalid username")


















