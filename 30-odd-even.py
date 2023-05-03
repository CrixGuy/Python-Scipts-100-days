print("Odd or Even ")
num = input("Enter a number: ")

num_as_int = int(num)

if num_as_int % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
