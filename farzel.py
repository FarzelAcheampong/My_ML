name_of_student = "my name is farzel"
print(name_of_student)

name = "Eric"
message = f"hello {name}, would you like to learn some python today"
print(message)

name = "eric"
print(name.lower())
print(name.upper())

name = "Albert Einstein"
message = f"{name} Once said, 'a person who never made a mistake never tried anything"
print(message)

favorite_number = "45"
words = "is my favorite number"
message = f"{favorite_number} {words}"
print(message)

name = "farzel"
specialties = ['good', 'brilliant', 'smart']
message = f"{name} is {specialties[1].title()}"
print(message)


friends = ['alex', 'prince', 'armah']
message = f"{friends[0]} is very foolish"
message_f1 = f"{friends[1]} how are you?"
message_f2 = f"{friends[2]}, i like reading"
print(message)
print(message_f1)
print(message_f2)

cars = ['honda', 'suzuki', 'toyota']
message = f"{cars}"
print(message)

names = ['farzel', 'alex', 'prince']
print(names)
names.append('lizzy')
print(names)

cars = []

cars.append('honda')
cars.append('yamaha')
cars.append('suzuki')

print(cars)

car = ['honda', 'suzuki', 'yamaha']
car.insert(1, 'bughatti')
print(car)

cars = ['honda', 'suzuki', 'yamaha']
del cars[2]
print(cars)
cars = ['honda', 'suzuki', 'yamaha']
print(cars)
popped_cars = cars.pop(1)
print(cars)
print(popped_cars)

last_owned = cars.pop(-1)
print(f"the last car i want to buy is {last_owned.title()}")

cars = ['honda', 'suzuki', 'yamaha']
cars.remove('yamaha')
print(cars)

cars = ['honda', 'suzuki', 'yamaha']
print(cars)
cars.remove('honda')
print(cars)
too_expensive = 'honda'
print(f"A {too_expensive} is too expensive for me.")

guest = ['farzel', 'alex', 'prince']
guest.insert(1, 'Elizabth')
guest.insert(2, 'godwin')
del guest[0]
del guest[3]
print(guest)
print(f"{guest[0].title()}, you are invited to my dinner party.")
print(f"{guest[1].title()}, you are invited to my dinner party.")
print(f"{guest[2].title()}, you are invited to my dinner party.")



cars = ['bmw', 'sonata', 'audi', 'honda']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

moto = ['bmw', 'sonata', 'audi', 'honda']
print(f"{moto[1]}, is my best car")

print("Here is the original list")
print(moto)

print("Here is the sorted list:")
print(sorted(moto))

print("Here is the original list again:")
print(moto)

loco = ['fosu', 'asamankese', 'kumasi', 'accra']
print(loco)
print(sorted(loco))
loco.sort(reverse=True)
print(loco)
loco.reverse()
print(loco)
loco.sort(reverse=True)
print(loco)
loco.sort()
print(loco)
