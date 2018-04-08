import sys

sample_input = ['2',
                '5',
                '5 6 8 4 3',
                '3',
                '8 9 7']

def solve():
    pass

def write_output(t, result):
    print ('Case #%s: %s' % (t, result))
    sys.stdout.flush()

def run():

    #We collect the first input line consisting of a single integer = T, the total number of test cases
    #T = int(input()) #SWAP
    T = int(sample_input[0]) #SWAP

    #We loop through each test case
    for t in range(1, T+1):

        N = int(sample_input[int(2*t)-1]) #SWAP
        V = [int(v) for v in sample_input[int(2*t)].split(' ')] #SWAP

        #N = int(input()) #SWAP
        #V = [int(v) for v in input().split(' ')] #SWAP

        write_output(t, solve())