# SLICING 
players = ["cr7", "messi", "Travis", "chicha", "corona"]
print(players[0:3])
# Slice es trabajar con un grupo específico de elementtos de una lista
print(players[1:4]) # ['messi', 'Travis', 'chicha']
print(players[:4]) # ['cr7', 'messi', 'Travis', 'chicha']
print(players[2:]) # ['Travis', 'chicha', 'corona']

print(players[-3:])
print(players[-3:-1])
print(players[4:2])

# Slicing en for
players_ = ["cr7", "messi", "Travis", "chicha", "corona"]
first_three_players = players_[0:3]
print("First three player: ", first_three_players)

print("Aqui vienen los tres mejores del salón: ")
for player in players_ [0:3]:
    print(player.upper())

# Copia de listas
my_food = ['pizza', 'gorditas de jaumave', 'machacado']
# copy_of_dood = my_food #Manera errónea de copiar una lista
copy_of_food = my_food[:]
copy_of_food_2 = my_food.copy()
copy_of_food_3 = list(my_food)

# Modificando elementos
cars = ["bwm", "porch", "masda", "totoya", "ford"]
cars[0] = "bmw" 
cars[1] = "porshe"
cars[2] = "mazda"
cars[3] = "toyota"

print(cars)