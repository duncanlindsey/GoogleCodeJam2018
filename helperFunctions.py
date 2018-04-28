import sys, random

def std_write(t, result):
    print ('Case #%s: %s' % (t, result))
    sys.stdout.flush()

def print_list(a_list):
    for x in a_list:
        print (x)

def import_data(filename):
    path = 'C:/Users/dunca/OneDrive/Documents/GitHub/google-codejam-07042018/%s.txt' % filename
    test_file = open(path, 'r')
    data = test_file.readlines()
    for i in range(len(data)):
        data[i] = data[i].replace('\n', '')
    return data