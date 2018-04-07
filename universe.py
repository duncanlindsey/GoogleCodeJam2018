import sys

sample_input = ['6',
                '1 CS',
                '2 CS',
                '1 SS',
                '6 SCCSSC',
                '2 CC',
                '3 CSCSS']
                
def calculate_damage(P): #CHECKED
    d = 0
    charge = 1
    for p in [op for op in P]:
        if p == 'C':
            charge = charge * 2
        elif p == 'S':
            d = d + charge
    return d

def max_swaps(P): #CHECKED
    swaps = 0
    if P.count('S'):
        s_loc = [loc for loc, char in enumerate(P) if char == 'S']
        for i in range(len(s_loc)):
            swaps += s_loc[i] - i
    return swaps

def min_damage(P): #CHECKED
    return P.count('S')

def swap(P): #CHECKED
    P_i = P[::-1]
    newP_i = ''
    for char in range(len(P_i)-1):
        pair = P_i[char] + P_i[char+1]
        if pair == 'SC':
            newP_i += 'CS'
            if char < len(P_i)-2:
                newP_i += P_i[char+2::]
            break
        else:
            newP_i += P_i[char]
    newP = newP_i[::-1]
    return newP

def test(P):
    d = calculate_damage(P)
    hacks = max_swaps(P)
    for i in range(hacks):
        P = swap(P)
        new_d = calculate_damage(P)
        delta = d - new_d
        d = new_d
        print ('Program: %s, damage reduction: %s, damage: %s' % (P, delta, d))


def write_output(t, result):
    print ('Case #%s: %s' % (t, result))
    sys.stdout.flush()

#We collect the first input line consisting of a single integer = T, the total number of test cases
#T = int(input()) #SWAP
T = int(sample_input[0]) #SWAP

#We loop through each test case
for t in range(1, T+1):

    #D_string, P = [s for s in input().split(' ')] #SWAP
    D_string, P = [s for s in sample_input[t].split(' ')] #SWAP
    D = int(D_string)

    #Calculate macro properties of P
    max_hacks = max_swaps(P)
    d_min = min_damage(P)
    d_current = calculate_damage(P)
    
    #Keep a track of how many hacks have been performed
    hacks = 0

    #Begin hacking, and keep hacking, if... (a) further hacks would decrease damage, (b) the shield is unable to withstand
    # the current damage, and (c) it is possible to hack the current program to a level the shield can withstand
    while hacks < max_hacks and d_current > D and d_min <= D:
        P = swap(P) #perform a hack
        hacks += 1
        d_current = calculate_damage(P)
    
    #Write result to stdout
    if d_min > D:
        write_output(t, 'IMPOSSIBLE')
    else:
        write_output(t, hacks)