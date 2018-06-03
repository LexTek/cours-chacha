import sys
import random
import time

def print_world(wo):
    for y in range(0, len(wo[0])):
        for x in range(0, len(wo)):
            if wo[x][y] == 1:
                sys.stdout.write('o')
            else:
                sys.stdout.write(' ')
        print()

def scan(wo, x, y):
    cpt = 0
    for o1 in range(-1, 2):
        for o2 in range(-1, 2):
            if x + o1 >= 0 \
               and y + o2 >= 0 \
               and x + o1 <= len(wo) - 1 \
               and y + o2 <= len(wo[x]) - 1 \
               and (o1 != 0 or o2 != 0):
                cpt += wo[x + o1][y + o2]
    return cpt

width = 80
height = 40

world = []

for x in range(0, width):
    col = []
    for y in range(0, height):
        col.append(random.randint(0, 1))
    world.append(col)

print_world(world)

while True:
    next_world = []
    for x in range(0, len(world)):
        col = []
        for y in range(0, len(world[x])):
            nblive = scan(world, x, y)
            if world[x][y] == 0:
                if nblive == 3:
                    col.append(1)
                else:
                    col.append(0)
            else:
                if nblive < 2:
                    col.append(0)
                elif nblive <= 3:
                    col.append(1)
                else:
                    col.append(0)
        next_world.append(col)
    world = next_world
    print_world(world)
    print('-------------------------')
    time.sleep(0.1)