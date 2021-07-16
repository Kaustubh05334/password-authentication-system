user_details = [["user1", "jkh$h"], ["user2", "kgdf%"], ["user3", "ueod^"]]
for i in range(3):
    v=0
    user_name = input("Enter user name:\n")
    user_password = input("Enter password:\n")
    for z in range(len(user_details)):
        if user_details[z][0]==user_name:
            if user_details[z][1]==user_password:
                print("verified")
                v=1
                break

            else:
                print("wrong password")
                break
    else:
        print("invalid user name")
    if v==1:
        break

