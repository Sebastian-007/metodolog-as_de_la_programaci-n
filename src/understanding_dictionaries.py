# Simple_dictionary
alien_0 = {'color': 'green', 'points': 5}

# The simpliest dicitionary
alien_1 = {'color' : 'yellow'}

# Accessing values in a dictionary
print(alien_1['color']) 
print(alien_0['points'])

# Empty dictionary
alien_2 = {}

# Modifying values in a dictionary
alien_2['color'] = 'yellow'
alien_2['color'] = 'blue'

# Adding key-value pairs
alien_2['x_positions'] = 0
alien_2['y_positions'] = 25

print(alien_2)

# Dictionary to store similar objects
favorite_languages = {
    'jen' : 'python', 
    'sarah' : 'c', 
    'edward' : 'ruby', 
    'phil' : 'python',
}

# Looping through all key-value pairs
for key, value in favorite_languages.items():
    print(f"{key.title()}'s favorite \
language is {value.title()}.")
    
# Looping through all keys and values separately
for key in favorite_languages.keys():
    print(key)

# Looping through all values    
for value in favorite_languages.values():
    print(value)