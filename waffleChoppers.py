import helperFunctions as hf
import numpy as np

''' Functions '''

def factors(inputs):
    if inputs['row_total'] % (inputs['H'] + 1) == 0 and inputs['col_total'] % (inputs['V'] + 1) == 0:
        return inputs   
    else:
        return False

def row_slicing(inputs):
    size = inputs['row_total'] / (inputs['H'] + 1)
    slices = inputs['H']
    cumul = 0
    slice_loc = []
    for subtotal in inputs['row_subtotals']:
        if cumul == size:
            slices -= 1
            cumul = 0
        cumul += subtotal
    if slices != 0:
        return False
    else:
        return 1

def solve(variables, array):
    
    #Set default result
    result = 'POSSIBLE'

    # Get variables
    H = variables[2]
    V = variables[3]
    
    # Build test library in order of increasing computational strain
    check_library = [factors]

    # Build checking data and prepare first input
    row_subtotals = np.sum(array, axis=1)
    row_total = sum(row_subtotals)
    col_subtotals = np.sum(array, axis=0)
    col_total = sum(col_subtotals)
    inputs = {'row_subtotals': row_subtotals, 
                'row_total': row_total, 
                'col_subtotals': col_subtotals, 
                'col_total': col_total, 
                'H': H, 
                'V': V}
    
    # Run checks
    for check in check_library:
        check_result = check(inputs)
        if not check_result:
            result = 'IMPOSSIBLE'
            print ('Check failed: ''%s''' % str(check))
            break
        else:
            inputs = check_result

    return result

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

    # Read content lines
    matrix = []
    for _ in range(int(variables[0])):
        #content_line = input() #SWAP
        content_line = data[index] #SWAP
        index += 1 #SWAP
        matrix.append(list(content_line))
    
    # Parse matrix to integers and a numpy array 
    dct = {'.': 0, '@': 1}
    matrix = [list(map(lambda y: dct[y], x)) for x in matrix]
    array = np.array(matrix)

    # Check all data read successfully
    print ('Test #%s\nVariables:%s\nMatrix:' % (t, variables))
    hf.print_list(array)

    # Calculate result
    result = solve(variables, array)

    # Write result to standard out
    hf.std_write(t, result)