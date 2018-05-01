import helperFunctions as hf
import numpy as np
import sys

''' Helper Functions '''

def std_write(t, result):
    print ('Case #%s: %s' % (t, result))
    sys.stdout.flush()

''' Problem-specific Functions '''

def score(votes, N):
    return round((votes/N)*100) - ((votes/N)*100)

def solve(variables, content):
    N = variables[0]
    score_sheet = list(map(lambda x: score(x, N), [_ for _ in range(N+1)]))
    U = N - sum(content)
    for _ in range(U):
        content.append(0)
    options_matrix = []
    for base in content:
        options_list = []
        for option in range(1, U+1):
            options_list.append((score_sheet[base+option]-score_sheet[base])/option)
        options_matrix.append(options_list)
    '''numerators = [i for i in range(1, U+1)]
    for vote in content:
        for extra in [i for i in range(U+1)]:
            possible_vote = vote + extra
            try:
                numerators.index(possible_vote)
            except ValueError:
                numerators.append(possible_vote)
    perc = list(map(lambda x: (x/N)*100, numerators))
    options = dict(zip(numerators, perc))'''
    return options_matrix

''' Main '''

# Import test data
data = hf.import_data('exampleData')

# Track data input index
index = 0

# Read first line
#T = int(input()) #SWAP
T = int(data[index]) #SWAP
index += 1 #SWAP

# Loop through test cases
for t in range(1, T+1):

    # Read variable line
    #data_line = input() #SWAP
    data_line = data[index] #SWAP
    index += 1 #SWAP

    # Chop variable line into list and parse to integers
    variables = data_line.split(' ')
    variables = list(map(int, variables))

    # Read content line
    #content_line = input() #SWAP
    content_line = data[index] #SWAP
    index += 1 #SWAP

    # Chop content line into list and parse to integers
    content = content_line.split(' ')
    content = list(map(int, content))

    # Check all data read successfully
    print ('Test #%s\nVariables:%s\nContent:%s' % (t, variables, content))

    # Calculate result
    #result = solve(variables, array)
    result = solve(variables, content)

    # Write result to standard out
    std_write(t, result)