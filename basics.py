import datetime

def greeting(name,age):
    now = datetime.datetime.now()
    centyear = 100 - int(age) + now.year
    message = f"Greetings {name}, the year will be {centyear} when you turn 100 years old"
    return message

user_input = input("What is your name?: ")
user_input2 = input("What is your age?: ")

print(greeting(user_input,user_input2))