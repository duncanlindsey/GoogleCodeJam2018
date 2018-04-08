import sys

s = {'up': [[-1,-1], [-1,0], [-1,1]],
    'down': [[1,-1], [1,0], [1,1]],
    'left': [[-1,-1], [0,-1], [1,-1]],
    'right': [[-1,1], [0,1], [1,1]]}

d = {'up': [-1, 0],
    'down': [1,0],
    'left': [0,-1],
    'right': [0,1]}

def build_orchard(r,c):
    return [[0 for i in range(c)] for j in range(r)]

def print_orchard(orchard):
    for row in orchard:
        print (row)

def IO(coordinates):
    print ('%s %s' % (coordinates[0], coordinates[1]))
    sys.stdout.flush()
    response = [int(s) for s in input().split(' ')]
    return response

def dig(coordinates, orchard):
    orchard[coordinates[0]][coordinates[1]] = 1
    return orchard

def check_side(c, orchard, side):
    completion = orchard[c[0] + s[side][0][0]][c[1] + s[side][0][1]] + \
                    orchard[c[0]+s[side][1][0]][c[1]+s[side][1][1]] + \
                    orchard[c[0]+s[side][2][0]][c[1]+s[side][2][1]]
    if completion == 3:
        return True
    else:
        return False
    
T = int(input())

for t in range(1, T+1):
    
    a = int(input())

    o = build_orchard(1000,1000)
    target = [500, 500]
    direction = ''
    last_response = IO(target)

    while last_response != [0,0] and last_response != [-1,-1]:

        o = dig(last_response, o)

        if direction == '':
            for key in list(s.keys()):
                found = check_side(target, o, key)
                if found:
                    direction = key
                    target = [target[0] + d[direction][0], target[1] + d[direction][1]]
        else:
            found = check_side(target, o, direction)
            if found:
                target = [target[0] + d[direction][0], target[1] + d[direction][1]]
        
        last_response = IO(target)

    if last_response == [0,0]:
        continue
    elif last_response == [-1,-1]:
        break