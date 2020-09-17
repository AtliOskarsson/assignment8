
#1.Create a function for the coordinates which uses the user input
#1a) Add to the value of x or y depending on the user input
#2. Create another function to print where user can move 
#3. Have this inside of a while loop
#4. Stop running when the user is at these coordinates (3,1) and print out "victory"



def tile_directions(coordinates):
    x = int(coordinates[1])
    y = int(coordinates[3])
    input_direction = input("Direction: ").upper()
    if input_direction == 'N' and y < 3 and coordinates != "(2,2)":
        y += 1
    elif input_direction == 'E' and x < 3 and coordinates != "(2,2)" and coordinates != "(2,1)" and coordinates != "(1,1)":
        x += 1
    elif input_direction == 'S' and y > 1 and coordinates != "(2,3)":
        y -= 1
    elif input_direction == 'W' and x > 1 and coordinates != "(2,1)" and coordinates != "(3,2)":
        x -= 1
    else:
        print("Not a valid direction!")
    return '({},{})'.format(x,y)

    

def tile_numbers(coordinates):
    x = int(coordinates[1])
    y = int(coordinates[3])
    #Changes the string to int

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
    elif x == 3 and y == 2:
        directions = print("You can travel: (N)orth or (S)outh.")
    elif x == 3 and y == 3:
        directions = print("You can travel: (S)outh or (W)est.")

coordinates = '(1,1)'

print("You can travel: (N)orth.")
while coordinates != '(3,1)':
    coordinates = tile_directions(coordinates)
    tiles = tile_numbers(coordinates)
print("Victory!")


