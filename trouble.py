import sys
from random import randint

sample_input = ['2',
                '5',
                '5 6 8 4 3',
                '3',
                '8 9 7']
                
def solve(V):
    list_1 = V[::2]
    list_1.sort()
    list_2 = V[1::2]
    list_2.sort()

    error = False
    error_i = None

    for i in range(len(list_2)):
        if list_2[i] < list_1[i]:
            error = True
            error_i = int(2*i)
            break
        if i < len(list_1)-1 and list_2[i] > list_1[i+1]:
            error = True
            error_i = int(2*i)+1
            break
    
    if error:
        return error_i
    else:
        return 'OK'

def write_output(t, result):
    print ('Case #%s: %s' % (t, result))
    sys.stdout.flush()

def trouble_sort(L):
    V = L
    done = False
    while not done:
        done = True
        for i in range(len(V)-2):
            if V[i] > V[i+2]:
                done = False
                new_V = []
                if i > 0:
                    new_V.extend(V[:i:])
                if i == len(V)-3:
                    new_V.extend(V[i::][::-1])
                else:
                    new_V.extend(V[i:i+3][::-1])
                    new_V.extend(V[i+3::])
                V = new_V
                break
    return V

def find_sort_error(V):

    V_sorted = sorted(V)

    error = False
    error_i = None
    
    for i in range(len(V)):
        if V_sorted[i] != V[i]:
            error = True
            error_i = i
            break

    if error:
        return error_i
    else:
        return 'OK'

def test(num_tests):
    failed = False
    fail_num = None
    fail_N = None
    fail_list = []
    fail_model = None
    fail_trouble = None
    fail_check = None

    for t in range(1, num_tests+1):
        N = randint(3,100)
        V = []
        for i in range(N):
            V.append(randint(0,10000000000))
        
        model = solve(V)
        trouble = trouble_sort(V)
        check = find_sort_error(trouble)
        
        if model != check:
            failed = True
            fail_num = t
            fail_N = N
            fail_list = V
            fail_model = model
            fail_trouble = trouble
            fail_check = check
            break

    if failed:
        print ('Test failed on test case: %s\nInput N: %s\nInput V: %s\nTrouble V: %s\nThe model returned: %s\nThe check on TROUBLE returned: %s' \
                % (fail_num, fail_N, fail_list, fail_trouble, fail_model, fail_check))
    else: 
        print ('No failures detected!')

def run():

    #We collect the first input line consisting of a single integer = T, the total number of test cases
    #T = int(input()) #SWAP
    T = int(sample_input[0]) #SWAP

    #We loop through each test case
    for t in range(1, T+1):

        N = int(sample_input[int(2*t)-1])
        V = [int(v) for v in sample_input[int(2*t)].split(' ')]

        #N = int(input())
        #V = [int(v) for v in input().split(' ')]

        write_output(t, solve(V))

test(10000)

#V = [0, 0, 2, 1, 2, 1, 3, 2, 3, 2, 6, 2, 7, 4, 7, 5, 8, 5, 8, 6, 9, 6, 9, 6, 10, 8, 10, 9, 10]
#V = [0,0,2,1,2]
#print (find_sort_error(V))
#run()