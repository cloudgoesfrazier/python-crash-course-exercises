# 3-1 Names
friends = ['Marq', 'Trae', 'Hari']
print(friends[0])
print(friends[1])
print(friends[2])

# 3-2 Greetings
message_to_marq = f"{friends[0]}, what are we doing for Tech Thursday?"
message_to_trae = f"{friends[1]}, what are we doing for Tech Thursday?"
message_to_hari = f"{friends[2]}, what are we doing for Tech Thursday?"

print(message_to_marq)
print(message_to_trae)
print(message_to_hari)

# 3-3 Your Own List
cars = ['Tesla', 'Honda', 'Lincoln', 'Audi']

for car in cars:
    print(f"I would love to own a {car}")

# 3-4 Guest List
guest_list = ['Obama', 'Thierry Henry', 'Cicero', 'Lebron James']

for guest in guest_list:
    print(f"Would you like to have dinner {guest}?")

# 3-5 Changing Guest List
guest_list = ['Obama', 'Thierry Henry', 'Cicero', 'Lebron James']

for guest in guest_list:
    print(f"Would you like to have dinner {guest}?")

print('Obama')
guest_list[0] = 'Denzel Washington'

for guest in guest_list:
    print(f"Would you live to have dinner {guest}?")

# 3-6 More Guests
print("Dear Guests, I have found a bigger table and will be sending additional invitations")

guest_list.insert(0, 'Lewis Hamilton')
guest_list.insert(3, 'Gabriel Jesus')
guest_list.append('J. Cole')

for guest in guest_list:
    print(f"{guest}, you are hearby invited to my dinner party")

# 3-7 Shrinking Guest List
print('Dear Guests, I only have room for 2 people')

guest1 = guest_list.pop(0)
print(f"Sorry {guest1}, I can only invite two people to dinner.")

guest2 = guest_list.pop(0)
print(f"Sorry {guest2}, I can only invite two people to dinner.")

guest3 = guest_list.pop(0)
print(f"Sorry {guest3}, I can only invite two people to dinner.")

guest4 = guest_list.pop(0)
print(f"Sorry {guest4}, I can only invite two people to dinner.")

guest5 = guest_list.pop(0)
print(f"Sorry {guest5}, I can only invite two people to dinner.")

for guest in guest_list:
    print(f"{guest}, you are still invited to the party.")

del guest_list[0]
del guest_list[0]

print(guest_list)

# 3-8 Seeing the World
locations =['Tokyo', 'Seoul', 'Istanbul', 'Tenerife', 'Alexandria']

print(locations)

print(sorted(locations))
print(locations)

print(sorted(locations, reverse=True))
print(locations)

locations.reverse()
print(locations)

locations.sort()
print(locations)

locations.sort(reverse=True)
print(locations)

# 3-9 Dinner Guests Cont.
number_of_guest = len(guest_list)
print(f"There are {number_of_guest} amount of guests invited to my dinner.")



