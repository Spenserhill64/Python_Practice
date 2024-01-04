# write a program that takes an age and will tell you if you are able to drive; assuming a legal driving age is 16.
# Establishing variables
age = input('Please enter your age to continue...>>')
age = int(age)

# if statement
if age > 16:
    print("Here are the carkeys")
elif age == 16:
    print("Congrats shithead, you're now old enough to get tried for manslaughter")
else:
    print("Too bad pal, fuck you.")