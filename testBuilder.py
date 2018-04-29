import random

def generate_test_data(T, var_ineq, filename):
    path = 'C:/Users/dunca/OneDrive/Documents/GitHub/google-codejam-07042018/%s.txt' % filename
    test_file = open(path, 'w')

    test_data = []
    test_data.append(str(T))
    test_file.write(str(T) + '\n')

    for _ in range(T):
        
        # Write variables line
        lead_line_list = []
        for i in range(len(var_ineq)):
            low_bound = var_ineq[i][0]
            up_bound = var_ineq[i][1]
            if up_bound is None:
                if i == 2:
                    up_bound = int(lead_line_list[0]) - 1
                elif i == 3:
                    up_bound = int(lead_line_list[1]) - 1
            var = random.randint(low_bound, up_bound)
            lead_line_list.append(str(var))
        lead_line = ' '.join(lead_line_list)
        test_data.append(lead_line)
        test_file.write(lead_line + '\n')

        # Write content matrix
        members = ['.', '@']
        for j in range(int(lead_line_list[0])):
            content_line_list = []
            for k in range(int(lead_line_list[1])):
                content = random.sample(members, 1)[0]
                content_line_list.append(content)
            content_line = ''.join(content_line_list)
            test_data.append(content_line)
            test_file.write(content_line + '\n')

    return test_data

var_ineq = [(2, 10), #R
            (2, 10), #C
            (1, 1), #H
            (1, 1)] #V

generate_test_data(1, var_ineq, 'singleTest')

