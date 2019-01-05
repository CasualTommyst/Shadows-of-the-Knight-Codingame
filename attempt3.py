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
        posy = posy - posy//2
                    
    elif bomb_dir == "UR":
        posy = posy - posy//2
        posx = (posx + (w - (w-((posx+1)))//2)) if (posx + (w - (w-((posx+1)))//2)) <= w else w-1
        
    elif bomb_dir == "R":
        posx = (posx + (w - (w-((posx+1)))//2)) if (posx + (w - (w-((posx+1)))//2)) <= w else w-1
        
    elif bomb_dir == "D":
        posy = (posy + (h - (h-((posy+1)))//2)) if (posy + (h - (h-((posy+1)))//2)) <= h else h-1
        
    elif bomb_dir == "DR":
        posy = (posy + (h - (h-((posy+1)))//2)) if (posy + (h - (h-((posy+1)))//2)) <= h else h-1
        posx = (posx + (w - (w-((posx+1)))//2)) if (posx + (w - (w-((posx+1)))//2)) <= w else w-1
        
    elif bomb_dir == "DL":
        posy = (posy + (h - (h-((posy+1)))//2)) if (posy + (h - (h-((posy+1)))//2)) <= h else h-1
        posx = posx - posx//2
        
    elif bomb_dir == "L":
        posx = posx - posx//2
        
    elif bomb_dir == "UL":
        posy = posy - posy//2
        posx = posx - posx//2
    
    print(posx, posy)
