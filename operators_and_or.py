name = "abc"
age = 19

if name == "abc" and age ==198:

    print("This is true")
else:

    print("both are not true that's why this is false")

name = "abc"
age = 19

if name == "abcc" or age ==198:

    print("For True, one must be true")
else:

    print("for false, both must be untrue")

## one more example

user_name = input("Please enter you name ")

user_age = input("Please enter your age : ")

user_age = int(user_age)

if user_age >=10 and (user_name[0]=='A' or user_name[0]=='S'):

    print("You can watch coco ")
else:

    print("you are not supposed to watch coco ")