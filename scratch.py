# name_of_student = "my name is farzel"
# print(name_of_student)
#
# name = "Eric"
# message = f"hello {name}, would you like to learn some python today"
# print(message)
#
# name = "eric"
# print(name.lower())
# print(name.upper())
#
# name = "Albert Einstein"
# message = f"{name} Once said, 'a person who never made a mistake never tried anything"
# print(message)
#
# favorite_number = "45"
# words = "is my favorite number"
# message = f"{favorite_number} {words}"
# print(message)
#
# name = "farzel"
# specialties = ['good', 'brilliant', 'smart']
# message = f"{name} is {specialties[1].title()}"
# print(message)
#
#
# friends = ['alex', 'prince', 'armah']
# message = f"{friends[0]} is very foolish"
# message_f1 = f"{friends[1]} how are you?"
# message_f2 = f"{friends[2]}, i like reading"
# print(message)
# print(message_f1)
# print(message_f2)
#
# cars = ['honda', 'suzuki', 'toyota']
# message = f"{cars}"
# print(message)
#
# names = ['farzel', 'alex', 'prince']
# print(names)
# names.append('lizzy')
# print(names)
#
# cars = []
#
# cars.append('honda')
# cars.append('yamaha')
# cars.append('suzuki')
#
# print(cars)
#
# car = ['honda', 'suzuki', 'yamaha']
# car.insert(1, 'bughatti')
# print(car)
#
# cars = ['honda', 'suzuki', 'yamaha']
# del cars[2]
# print(cars)
# cars = ['honda', 'suzuki', 'yamaha']
# print(cars)
# popped_cars = cars.pop(1)
# print(cars)
# print(popped_cars)
#
# last_owned = cars.pop(-1)
# print(f"the last car i want to buy is {last_owned.title()}")
#
# cars = ['honda', 'suzuki', 'yamaha']
# cars.remove('yamaha')
# print(cars)
#
# cars = ['honda', 'suzuki', 'yamaha']
# print(cars)
# cars.remove('honda')
# print(cars)
# too_expensive = 'honda'
# print(f"A {too_expensive} is too expensive for me.")
#
# guest = ['farzel', 'alex', 'prince']
# guest.insert(1, 'Elizabth')
# guest.insert(2, 'godwin')
# del guest[0]
# del guest[3]
# print(guest)
# print(f"{guest[0].title()}, you are invited to my dinner party.")
# print(f"{guest[1].title()}, you are invited to my dinner party.")
# print(f"{guest[2].title()}, you are invited to my dinner party.")
#
#
#
# cars = ['bmw', 'sonata', 'audi', 'honda']
# cars.sort()
# print(cars)
# cars.sort(reverse=True)
# print(cars)
#
# moto = ['bmw', 'sonata', 'audi', 'honda']
# print(f"{moto[1]}, is my best car")
#
# print("Here is the original list")
# print(moto)
#
# print("Here is the sorted list:")
# print(sorted(moto))
#
# print("Here is the original list again:")
# print(moto)
#
# loco = ['fosu', 'asamankese', 'kumasi', 'accra']
# print(loco)
# print(sorted(loco))
# loco.sort(reverse=True)
# print(loco)
# loco.reverse()
# print(loco)
# loco.sort(reverse=True)
# print(loco)
# loco.sort()
# print(loco)

# THE FOR LOOPS
# magicians = ['farzel', 'prince', 'dereck']
# for magician in magicians:
#     print(magician)
#
# cats = ['jack', 'john', 'jacky']
# for cat in cats:
#     print(cat)\
#
# list_of_items = ['spoon', 'bowl', 'rug']
# for item in list_of_items:
#     print(item)
#
# magicians = ['farzel', 'prince', 'dereck']
# for magician in magicians:
#     print(f"{magician.title()}, your trick was great.")
#     print(f"We are looking forward to next trick, {magician.title()} ")
#
# print("Thank you everyone. That was a great show.")
#
# pizza = ['jango', 'good', 'jam']
# for pizzas in pizza:
#     print(f"I like {pizzas.title()} pizza very much")
# print("I love pizza")
#
# pets = ['dog', 'cat', 'snake']
# for pet in pets:
#     print(f"A {pet.title()} would make a great pet.")
#     print(f"{pet.title()}, is very nice.")
#
# print("Any of these animals would make a great pet")
#
#
# laptops = ['lenovo', 'Hp', 'Dell']
# for laptop in laptops:
#     print(f"{laptop.title()}, would make a great laptop.")
#     print(f"{laptop.title()}, is the best.")
# print(f"The one i like most is {laptops[0].title()}.")\


# THE RANGE() FUNCTIONS

# for value in range(1, 5):
#     print(value)
# for value in range(6):
#     print(value)
# for x in range(2, 7):
#     print(x)
#
# # THE LIST() FUNCTIONS
#
# numbers = list(range(1, 6))
# print(numbers)
#
# even_numbers = list(range(2, 24, 2))
# print(even_numbers)
# odd_numbers = list(range(1, 13, 2))
# print(odd_numbers)
#
# square = []
# for value in range(1, 11):
#     square.append(value**2)
# print(square)
#
# square = [value**2 for value in range(1, 11)]
# print(square)
#
# for value in range(1, 21):
#     print(value)
#
# for value in range(1, 100):
#     print(value)
#
# even_numbers = list(range(2, 21, 2))
# print(even_numbers)
# odd_numbers = list(range(1, 21, 2))
# print(odd_numbers)
#
# numb = [value**3 for value in range(1, 11)]
# print(numb)
#
#
#
# # slicing a list
#
# players = ['john', 'jack', 'joe', 'prince', 'herbert']
# print(players[:3])
#
# players = ['john', 'jack', 'joe', 'prince', 'herbert']
# print(players[0:3])
# print(players[1:4])
# print(players[2:3])
#
# players = ['john', 'jack', 'joe', 'prince', 'herbert']
# print("Here are my first 4 players")
# for player in players[:4]:
#     print(player)
#
# points = ['32', '12', '24', '35']
# print(points.sort(reverse=True))
# for point in points[:3]:
#     print(point)
#
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friends_foods = my_foods[:]
# my_foods.append('banku')
# friends_foods.append('fufuo')
# print("Here are my best foods:")
# print(my_foods)
#
# print("here are my best friend's best foods: ")
# print(friends_foods)
#
# message = 'this is my best item'
# print(message)
# items = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
# for item in items[:3]:
#     print(item)
#
# my_items = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
# my_friends = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
# my_items.append('shawarma')
# my_friends.append('peperoni pizza')
# print("The food i like best is:")
# for items in my_items:
#     print(items)
# print("The food my best friend likes best is:")
# for fitems in my_friends:
#     print(fitems)
#
# # TUPLES
#
# foods = ('pizza', 'junjle')
# dimensions = (200, 50)
# for dimension in dimensions:
#     print(dimension)
#
#
# # IF STATEMENTS
#
# car = ['van', 'bmw', 'honda']
# for cars in car:
#     if cars == 'van':
#         print(cars.upper())
#     else:
#         print(cars.title())
#
# requested_order = 'mushroom'
# if requested_order != 'mushroom':
#     print("This order is incomplete")
# else:
#     print("The order is complete")
#
# answer = '71'
# if answer != '71':
#     print("Your answer is incomplete, please try again!")
# else:
#     print("Your answer is correct!")
#
# requested_toppings = ['mushrooms', 'onions', 'pineapple']
# if 'mushrooms' == requested_toppings:
#     print("true")
# else:
#     print("false")
#
# banned_users = ['andrew', 'carolina', 'david', 'maria']
# user = 'maria'
# if user not in banned_users:
#     print(f"{user.title()}, you are not banned.")
# else:
#     print(f"{user.upper()}, you are banned!")

# age = '17'
# if age >= '18':
#     print("you are old enough for voting")
#     print("Have you voted yet?")
# else:
#     print("You are invalid to vote")
#
# age = 18
# if age < 4:
#     print("You registration fee is free ")
# elif age < 18:
#     print("Your registration fee is $25")
# else:
#     print("Your registration fee is 40$")

# import random
#
#
# def shuffle(string):
#   tempList = list(string)
#   random.shuffle(tempList)
#   return ''.join(tempList)
#
#
# uppercaseLetter1 = chr(random.randint(65, 90))
# uppercaseLetter2 = chr(random.randint(65, 90))
# lowercaseletter3 = chr(random.randint(65, 70))
# lowercaseletter4 = chr(random.randint(65, 70))
# lowercaseletter5 = chr(random.randint(65, 70))
# lowercaseletter6 = chr(random.randint(65, 70))
#
#
#
#
# password = uppercaseLetter1 + uppercaseLetter2 + lowercaseletter3 + lowercaseletter4 + lowercaseletter5 + lowercaseletter6
# password = shuffle(password)
#
#
# print(password)


# print("Your is pizza is getting ready")

# request = ['mushrooms', 'ketchup', 'onion']
# if 'mushrooms' in request:
#     print(f"\nAdding {request[0]}")
# if 'ketchup' in request:
#     print(f"Adding {request[1]}")
# if 'onion' in request:
#     print(f"Adding {request[2]}")
#
# print("\nYour pizza is ready. DIng DOng")
#
# color = 'green'
# if color == 'green':
#     print("You earned 5p")
# if color != 'green':
#     print("you earned 10p")
#
# cars = ['bmw', 'benz', 'toyota']
# if 'benz' in cars:
#     print("you passed!")
# else:
#     print("You failed")

# color = ['violet', 'blue', 'green']
# if 'green' in color:
#     print("YE 5p")
# if 'blue' in color:
#     print("YE 10p")
# if 'red' in color:
#     print("YE 15p")
#
# age = 34
# if age < 2:
#     print("You are a baby")
# else:
#     print("You aare not a baby")
# if age <= 4:
#     print("You are a toddler")
# else:
#     print("You are not a toddler.")
# if age > 4 >= 13:
#     print("You are a kid.")
# else:
#     print("You are not a Kid.")
# if age == 13 & age < 20:
#     print("You are a teenager.")
# else:
#     print("You are not a teenager.")
# if age == 20 | age <65:
#     print("You are an adult.")
# else:
#     print("You are not an adult.")
# if age > 65:
#     print("You are an elder")
# else:
#     print("You are not an elder")

# cars = ['bmw', 'benz', 'toyota']
# for car in cars:
#   if car == 'benz':
#      print("We are out of benz")
#   else:
#     print(f"Adding {car} to your list")
#
# requests = []
# for request in requests:
#     print(f"Adding {request}")
#     print("\nYour pizza is ready.")
# else:
#     print("Do you want a plain pizza?")
#
#
# available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
#
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
# for requests in requested_toppings:
#     if requests in available_toppings:
#         print(f"Adding {requests} ")
# else:
#     print(f"We are out of {requests}")
#
# users = []
# regis = []
# for user in users:
#     if user in regis:
#         print(f"{user}, you are welcome.")
#     else:
#         print(f"{user} Try to login.")
# else:
#     print("We have to get some users")
#
# current_users = ['John', 'jack', 'joe', 'joel', 'jaky']
# new_users = ['jack', 'prince', 'richard', 'jaky']
# for new_user in new_users:
#     if new_user in current_users:
#         print(f"{new_user}, you are welcome again. ")
#     else:
#         print(f"{new_user}, sign in into the site.")
#
# numbers = (1, 10)
# for numbers in range(1, 10):
#     print(numbers)

# object = ['car', 'item']
# cars = ['benz', 'bmw']
# print(list(object))
# print("Choose one from the list.")
# input()
# if input == object:
#     print("What Car do you want to Buy in future?")
#     print(list(cars))
#     print("Choose one Car")
#     input()
#     print(f"Hurry you just won a {input()}")
# else:
#     print("What Car do you want to Buy in future?")
#     print(list(cars))
#     print("Choose one Car")
#     n = input()
#     print(f"Hurry you just won a {n}")

# DICTIONARIES

# alien_0 = {'color': 'green', 'points': '67'}
# new_points = alien_0['points']
# print(f"You earned {alien_0['points']} points")
#
# alien_0 = {'color': 'green'}
# print(f"You color is {alien_0['color']}")
# alien_0['color'] = 'Yellow'
# print(f"Your color is {alien_0['color']}")
#
# alien = {'x_pose': 'o', 'y_pose': '25', 'speed': 'medium'}
# print(f"Original position: {alien['x_pose']}")
#
# if alien['speed'] == 'slow':
#     x_increment = 1
# elif alien['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
# else:
#     alien['x_pose'] = alien['x_pose'] + x_increment
# print(f"New position: {alien['x_pose']}")

# def restaurant():
#     people = int(input("How many people are waiting!:"))
#     if people > 8:
#         print("You are to wait for a table, Sorry!")
#     else:
#         print("Your table is ready!")
#
# restaurant()
#
#
# def even_odd():
#     number = int(input("Enter a number and i tell if it is a multiple of ten:"))
#     if number % 10 == 0:
#         print(f"\nThe number {number} is a multiple of 10")
#     else:
#         print(f"The number {number} is not a multiple of 10")
#
# even_odd()


# number = 1
# while number <= 5:
#     print(number)
#     number += 1
#
# prompt = "\nTell me something and i will tell you back."
# prompt += "\nEnter 'quit' to end the programme"
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# prompt = "\nTell me something and i will tell you back."
# prompt += "\nEnter 'quit' to end the programme"
# active = True
# while active:
#     message = input(prompt)
#
#     if message == 'quite':
#         active = False
#     else:
#         print(message)
#
#
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "
# while True:
#     city = input(prompt)
#     if city == 'quite':
#         break
#     else:
#         print(f"\nI would love to be in {city}")
#
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#
#     print(current_number)


# while True:
#     user = input("Enter your pizza choice:")
#     if user == 'quit':
#         break
#     else:
#         print(f"\nAdding {user} to your shopping list.")

# while True:
#     user = int(input("Enter your age:"))
#     if user <= 3:
#         print("Your ticket fee is free.")
#     elif user > 3 < 12:
#         print("You ticket fee is $10")
#     elif user == 13:
#         print("You ticket fee is $20")
#     else:
#         if user != int:
#             print("Invalid input. Try again")

# EXIT THE LOOP WHEN IT GET TO 3:
# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# i = 4
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)
#
#
# for x in range(6):
#     print(x)
# else:
#     print("Finally finished")

# for y in range(6):
#     if y == 3:break
#     print(y)
# else:
#         print("hgfghuhfthj")


# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
#
# for x in adj:
#  for y in fruits:
#         print(x, y)


# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []
#
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#
#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)
#
#     print("\nThe following users have been confirmed:")
#     for confirmed_users in confirmed_users:
#         print(confirmed_user.tittle)



# FUNCTIONS

# def greet(name):
#     print(f"Hello, {name}!")
# greet("Alice")
#
# def pet(animal, name):
#
#     print(f"I have a {animal}")
#     print(f"{name}, is the name of my pet")
# pet("dog", "Harry")
# pet("Jaguar", "Prince")
#
# # Keyword Arguments
#
# def pet(animal, name):
#
#     print(f"I have a {animal}")
#     print(f"{name}, is the name of my pet")
# pet(animal = 'dog', name = 'Harry')
#
# # OR
#
# def pet(animal = 'dog', name = 'Harry'):
#
#     print(f"I have a {animal}")
#     print(f"{name}, is the name of my pet")
# pet()


# Try work:

# def make_shirt(size, text):
#     print(f"The size of your shirt is {size}")
#     print(f"The printed name on the shirt is {text}")
# make_shirt('15(large)', 'Tw3skum')
#
# # Try work 2:
# def make_shirt(size, text):
#     print(f"Shirt size = {size}")
#     print(f"Text On Shirt = {text}")
# make_shirt('15(large)', 'Tw3skum')
# make_shirt('10(medium)', 'I love python')
#
#
# # Try work 3:
#
# def describe_city(city, country):
#     print(f"{city} is in {country}")
# describe_city(city = 'Accra', country ='Ghana')



# THE RETURN FUNCTION

# def get_name(first, last):
#     full_name = f"{first} {last}"
#     return full_name.title()
#
# name = get_name(first="farzl", last="A")
# print(name)

# def get_name(first, middle, last):
#     full_name = f"{first} {middle} {last}"
#     return full_name.title()
#
# name = get_name(first="farzl", middle="Akwasi", last="Acheampong")
# print(name)

# def get_name(first, middle, last):
#     if middle:
#         full_name = f"{first} {middle} {last}"
#     else:
#         full_name = f"{first} {last}"
#     return full_name.title()
#
# name = get_name("farzl", "Acheampong")
# print(name)
#
# name = get_name("John", "Fame", "john")
# print(name)

# def build(first, last, Age=None):
#
#     person = {'First': first, 'Last': last}
#     if Age:
#         person['Age'] = Age
#     return person
#
# my_name = build('Farzel', 'Acheampong', Age=37)
# print(my_name)


# def name_formatted(first, last):
#     """Print name neatly formatted"""
#     full_name = f"{first} {last}"
#     return full_name
# while True:
#     print("\nEnter Your name")
#     print("Press 'q' to quit")
#     f_name = input("First name:")
#     if f_name == 'q':
#         break
#     l_name = input("Last name:")
#     if l_name == 'q':
#         break
#
#     formatted_name = name_formatted(f_name, l_name)
#     print(f"\nHello {formatted_name}")

# def city_country(city, country):
#
#     full = f"{city}, {country}"
#     return full.title()
#
#
# full_name = city_country('Kumasi', 'Ghana')
# print(f"{full_name}")


# def make_album(name, title, songs=None):
#     album = {'Artist': name, 'Album': title}
#
#     if songs:
#         album['songs'] = songs
#     return album
#
# full_album = make_album('Black Sherif', 'The villain I Never Was', songs=14)
# print(f"{full_album}")

# def make_album(name, title, songs=None):
#     album = f"{name}, {title}"
#
#     if songs:
#         album['songs'] = songs
#     return album
# while True:
#     Artist = input("Enter Artist Name:")
#     Title = input("Enter Album name:")
#     break
#
# full_album = make_album(Artist, Title)
# print("Here is Your Album:")
# print(f"{full_album}")

# Passing a List

# def great(names):
#     """Greats everyone in a list"""
#     for name in names:
#         msg = f"Hello, {name.title()}"
#         print(msg)
# usernames = ['farzel', 'dereck', 'lisa']
# great(usernames)


# Modifying a list
#
# current = ['Iphone','samsung', 'Oppo']
# uncurrent = []
#
# while current:
#     current1 = current.pop()
#     uncurrent.append(current1)
#     print(f"\nCompleted: {uncurrent}")



