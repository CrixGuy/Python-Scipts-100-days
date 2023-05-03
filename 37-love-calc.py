print("Welcome to the Love Calculator")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

tcount = 0
lcount = 0

for letter in "true":
    lower_case_name1 = name1.lower()
    lower_case_name2 = name2.lower()
    tcount += lower_case_name1.count(letter)
    tcount += lower_case_name2.count(letter)

for letter in "love":
    lower_case_name1 = name1.lower()
    lower_case_name2 = name2.lower()
    lcount += lower_case_name1.count(letter)
    lcount += lower_case_name2.count(letter)

score = int(str(tcount)+str(lcount))

if score < 10 or score > 90:
    print(f"Your score is {score}% - you go together like coke and mentos")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}% - you are alright together")
else:
    print(f"Your score is {score}%")
