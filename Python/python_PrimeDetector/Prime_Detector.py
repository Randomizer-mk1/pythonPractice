# Created on Randomizer.
# Prime Detector


def PrimeDetect(num):
    while True:
        print("\nInitializing\n\n\n")
        num = int(input("Put number here: "))
        x = int(2)

        while range(1, num):
            t = num % x
            x = x + 1

            if t == 0:
                print("\nNot Prime")
                print(" ", num, " = ", x - 1, "*", int(num / (x - 1)))
                break

            elif t == 1 and x == num:
                print("Prime")
                break
            continue
        print("\n\nJob_Done\n")


PrimeDetect(0)

# YAS!!!
