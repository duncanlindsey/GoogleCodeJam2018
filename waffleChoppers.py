import helperFunctions as hf
import numpy as np

''' Functions '''

def factor_rows(row_subtotals, col_subtotals, row_total, col_total, H, V):
    return row_total % (H + 1) == 0

def factor_cols(row_subtotals, col_subtotals, row_total, col_total, H, V):
    return col_total % (V + 1) == 0

def partition_rows(row_subtotals, col_subtotals, row_total, col_total, H, V):
    size = row_total / (H + 1)
    slices = H
    cumul = 0
    for subtotal in row_subtotals:
        if cumul == size:
            slices -= 1
            cumul = 0
        cumul += subtotal
    return slices == 0

def partition_cols(row_subtotals, col_subtotals, row_total, col_total, H, V):
    size = col_total / (V + 1)
    slices = V
    cumul = 0
    for subtotal in col_subtotals:
        if cumul == size:
            slices -= 1
            cumul = 0
        cumul += subtotal
    return slices == 0

def solve(variables, matrix):
    
    #Set default result
    result = 'POSSIBLE'

    # Get variables
    H = int(variables[2])
    V = int(variables[3])
    
    # Convert matrix to integers
    dct = {'.': 0, '@': 1}
    matrix = [list(map(lambda y: dct[y], x)) for x in matrix]
    
    # Setup check library
    check_library = [factor_rows, factor_cols, partition_rows, partition_cols]

    # Build checking data
    row_subtotals = [sum(i) for i in matrix]
    row_total = sum(row_subtotals)
    col_subtotals = [sum(i[j] for i in matrix) for j in range(len(matrix[0]))]
    col_total = sum(col_subtotals)
    
    # Run checks
    for check in check_library:
        if not check(row_subtotals, col_subtotals, row_total, col_total, H, V):
            result = 'IMPOSSIBLE'
            print ('Check failed: ''%s''' % str(check))
            break

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

    # Chop variable line into list
    variables = data_line.split(' ')

    # Read content lines
    matrix = []
    for _ in range(int(variables[0])):
        #content_line = input() #SWAP
        content_line = data[index] #SWAP
        index += 1 #SWAP
        matrix.append(list(content_line))
    
    # Check all data read successfully
    print ('Test #%s\nVariables:%s\nMatrix:' % (t, variables))
    hf.print_list(matrix)

    # Calculate result
    result = solve(variables, matrix)

    # Write result to standard out
    hf.std_write(t, result)