year = int(input("Which year do you want to check? "))

print("Solution 1")
# Solution 1
if year % 400 == 0:
    print("It's a leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("It's a leap year")
else:
    print("Not a leap year")


print("Solution 2")
# Solution 2
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("2 - It's a leap year")
        else:
            print("2 - Not a leap year")
    else:
        print("2 - It's a leap year")
else:
    print("2 - Not a leap year")