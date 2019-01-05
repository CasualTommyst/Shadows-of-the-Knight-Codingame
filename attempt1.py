import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


# the location of the next window Batman should jump to.



w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

posx = x0
posy = y0

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    if bomb_dir == "U":
        posy -= 1
                    
    elif bomb_dir == "UR":
        posy -= 1
        posx += 1
        
    elif bomb_dir == "R":
        posx += 1
        
    elif bomb_dir == "D":
        posy += 1
        
    elif bomb_dir == "DR":
        posy += 1
        posx += 1
        
    elif bomb_dir == "DL":
        posy += 1
        posx -= 1
        
    elif bomb_dir == "L":
        posx -= 1
        
    elif bomb_dir == "UL":
        posy -= 1
        posx -= 1
    
    print(posx, posy)
