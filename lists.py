#list of bicycles
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#printing single elements in a list
print(bicycles[2])
print(bicycles[0])
print(bicycles[1])
print(bicycles[3])

#printing single elements in a list as capitalized
print(bicycles[2].title())
print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[3].title())

#using individual values from a list
message = "My first bicycle was a " + bicycles[2].title() + "."
print(message)

# list of guitars
guitars = ['fender', 'ibanez', 'taylor', 'gibson', 'guild']

# modifying elements in a list
guitars[1] = 'martin'
guitars[3] = 'les paul'
print(guitars)

# appending elements to the end of a list, without affecting any other elements in a list
guitars.append('takamine')
print(guitars)

# inseting elements into a list
guitars.insert(0, 'stratocaster')
print(guitars)

# removing an item using the del statement
del guitars[3]
print(guitars)

# removing an item using pop()
jedi = ['obi-wan', 'anakin', 'yoda', 'luke']
popped_jedi = jedi.pop(2)
print(jedi)

# Here I use the index of "anakin"
most_powerful = jedi.pop(1)
print(f"The most powerful jedi was {most_powerful.title()}.")

# removing an item by value
users = ['Jose', 'Maria', 'Manuel', 'Linda']

users.remove('Jose')
print(users)

inactive_user = 'Maria'

users.remove(inactive_user)
print(users)
print(f"{inactive_user.title()} is an inactive user.")

# the sort method sorts the values of a list in alphabetical order
users.sort()
print(users)