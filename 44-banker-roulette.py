# Split string method
import random

names_string = input("Enter everyone's names, separated by a comma. ")
names = names_string.split(", ")


#Solution 1
#selection = random.randint(0, (len(names) - 1))
#chosen_name = names[selection]

#Solution 2
chosen_name = random.choice(names)


print(f"{chosen_name} is going to buy the meal today")
