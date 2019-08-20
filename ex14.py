#Exercise 14 Prompting and passing
'''
from sys import argv

script, user_name, user_surename = argv
start_point = '> '

print(f"Hi {user_name} {user_surename}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name} {user_surename}?")
likes = input(start_point)

print(f"Where do you live {user_name} {user_surename}?")
lives = input(start_point)

print(f"What kind of computer do you have {user_name} {user_surename}.")
computer = input(start_point)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have {computer} computer. Nice.
""")
'''

#Rewrite of the exercise 14

from sys import argv

script, first_name, last_name = argv

prompt = ">> "

print(f"Hi. {first_name} {last_name} I'm a {script}.")
print("Say what do you think about Python programming language?")
opinion = input(prompt)

print(f"In which city do you leave {first_name} {last_name}?")
city = input(prompt)

print(f"What cell phone do you use {first_name} {last_name}")
cellphone = input(prompt)

print(f'''
Ok {first_name} {last_name}. So you think that python {opinion}.
You leave in {city} and you use {cellphone}. Fare enough.
''')
