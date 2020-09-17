def tile_directions(coordinates):
    x = int(coordinates[1])
    y = int(coordinates[3])
    while True:
        input_direction = input("Direction: ").upper()
        if input_direction == 'N' and y != 3 and coordinates != "(2,2)":
            y += 1
            break
        elif input_direction == 'E' and x != 3 and coordinates != "(1,1)" and coordinates != "(2,2)" and coordinates != "(2,1)":
            x += 1
            break
        elif input_direction == 'S' and y != 1 and coordinates != "(2,3)":
            y -= 1
            break
        elif input_direction == 'W' and x != 1 and coordinates != "(2,1)" and coordinates != "(3,1)" and coordinates != "(3,2)":
            x -= 1
            break
        else:
            print("Not a valid direction!")
    return '({},{})'.format(x,y)
    

def tile_numbers(coordinates):
    x = int(coordinates[1])
    y = int(coordinates[3])

    if x == 1 and y == 1:
        directions = print("You can travel: (N)orth.")
    elif x == 1 and y == 2:
        directions = print("You can travel: (N)orth or (E)ast or (S)outh.")
    elif x == 1 and y == 3:
        directions = print("You can travel: (E)ast or (S)outh.")
    elif x == 2 and y == 1:
        directions = print("You can travel: (N)orth.")
    elif x == 2 and y == 2:
        directions = print("You can travel: (S)outh or (W)est.")
    elif x == 2 and y == 3:
        directions = print("You can travel: (E)ast or (W)est.")
    elif x == 3 and y == 1:
        False
    elif x == 3 and y == 2:
        directions = print("You can travel: (N)orth or (S)outh.")
    elif x == 3 and y == 3:
        directions = print("You can travel: (S)outh or (W)est")

coordinates = '(1,1)'

print("You can travel: (N)orth.")
while True:
    coordinates = tile_directions(coordinates)
    tiles = tile_numbers(coordinates)
    if coordinates == '(3,1)':
        break

print("Victory!")
