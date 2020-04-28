### pass statement

x = 18

if x>18:

    pass

age = input("pleae enter your age : ")
age = int(age)
if age ==14:
    print("Line A")
    print("You are 14, you can play")

elif age >14:
    print("you entered right age, please play")

else:

    print("Sorry, you can't play")


winning_number = 27

user_input = input("guess a number b/w 1 and 100 : ")
user_input = int(user_input)

if user_input == winning_number:

    print("you have won !!")

else:
    if user_input < winning_number:

        print("Try one more time, numbe is too low ")
    else:
        print("number is too high ")



































