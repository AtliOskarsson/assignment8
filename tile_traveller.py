def tile_directions():
    input_direction = input("Direction: ")
    if input_direction == 'N' or input_direction == 'n':
        y += 1
    elif input_direction == 'E' or input_direction == 'e':
        x += 1
    elif input_direction == 'S' or input_direction == 's':
        y -= 1
    elif input_direction == 'W' or input_direction == 'w':
        x -= 1
    else:
        print("Not a valid direction!")
    return (x,y)
    

def tile_numbers(x):
    if x == (1,1):
        directions = print("You can travel: (N)orth")
    elif x == (1,2):
        directions = print("You can travel: (N)orth or (E)ast or (S)outh")
    elif x == (1,3):
        directions = print("You can travel: (E)ast or (S)outh")
    elif x == (2,1):
        directions = print("You can travel: (N)orth")
    elif x == (2,2):
        directions = print("You can travel: (E)ast or (S)outh or (W)est")
    elif x == (2,3):
        directions = print("You can travel: (E)ast or (W)est")
    elif x == (3,1):
        False
    elif x == (3,2):
        directions = print("You can travel: (N)orth or (S)outh")
    elif x == (3,3):
        directions = print("You can travel: (S)outh or (W)est")

x = 1
y = 1

print("You can travel: (N)orth")
while True:
    coordinates = tile_directions(x,y)
    tiles = tile_numbers(coordinates)

print("Victory!")
