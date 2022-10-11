print("initializing")

name = input("What is your name? ")
print(name)
age = int(input("What is your age "))

print("Hello", name, "you are", age, "years old. ")

#Basically clowning at this point
if 12 < age < 18:
    print("good enough")

    want_to_play = input("do you want to play?(yes/y or no/n)").lower()

    if want_to_play in {"yes", "y", "yup"}:
        print("lets play the game")

        print("BOOM \nyou are dead \nha ha \nyou suck")

    else:
        #age = BIG NUM
        age = 90000
    print("k")
if 19 < age < 26:
    print("why are you still here?")

if 27 < age < 100:
    print("you're joking right?")

else:
    print("go home bucko")
