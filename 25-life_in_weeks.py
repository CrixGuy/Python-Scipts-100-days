age = input("What is your current age? ")

days = 365
weeks = 52
months = 12

years_left = 90 - int(age)
days_left = years_left * days
weeks_left = years_left * weeks
months_left = years_left * months


print("You have "+ str(days_left) +" days, "+ str(weeks_left) +" weeks, and "+ str(months_left) +" months left.")

#f-string
message = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."
print(message)
