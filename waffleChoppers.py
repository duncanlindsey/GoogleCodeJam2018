import helperFunctions as hf

''' Functions '''

def solve():
    pass

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
        matrix.append(content_line.split(' '))
    
    print ('Test #%s\nVariables:%s\nMatrix:' % (t, variables))
    hf.print_list(matrix)