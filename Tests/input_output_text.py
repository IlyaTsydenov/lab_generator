import subprocess
import sys
import os


def output_params_test(test_output, params):
    if ((params[0]) and (params[0][0:5] == "size=")):
        size = params[0][5:len(params[0])]
        
    if ((params[1]) and (params[0][0:9] == "in_a_row=")):
        in_a_row = params[1][9:len(params[1])]
        
    if ((params[2]) and (params[0][0:12] == "doors_count=")):
        doors_count = params[2][12:len(params[2])]
        
    errors_desc = get_errors_description()
    if (len(test_output) == 0):
        return "Test not successful. Program's algorithm exception"

    if test_output[0] in errors_desc:
        return error_desc[test_output[0]]

    previous = 0
    length = 0
    for string in test_output:
        if(string == test_output[len(test_output) - 2]):
            break
           
        coord_list = string.split('-')
        first_x_y = coord_list.split(':')
        second_x_y = coord_list.split(':')
        if (first_x_y[0] == second_x_y[0]):
            output_in_a_row = abs(first_x_y[1]-second_x_y[1])
            length += output_in_a_row
        elif (first_x_y[1] == second_x_y[1]):
            output_in_a_row = abs(first_x_y[0]-second_x_y[0])
            length += output_in_a_row
            
        if (output_in_a_row > in_a_row):
            return "Incorrect in_a_row treatment"
        
        if ((previous != 0) and (coord_list[0] != previous)):
            return "Incorrect labyrinth coords list output. \
            Next list first element doesn't start with previous \
            list final element"
        
        previous = coord_list[1]

    doors = test_output[len(test_output) - 2].split(',')
    keys = test_output[len(test_output) - 1].split(',')
    if (doors != keys):
        return "Incorrect program output. Doors count != keys count"

    if (doors != doors_count):
        return "Incorrect program output. \
        Doors count not complies input doors count"
    
    if ((size*size) != length):
        return "Incorrect program output. Program algoritm error. \
        Size by coords not complies input size"

    return "Test successful"
        

def input_params_test(output_file, program_path, program_name):
    for test_name,params in get_test_params().items():
        output_string = test_name + "\n"
        test_path = program_path + '/' + test_name
        output_path = program_path + '/test_output'
        try:
            test_file = open(test_path, 'w')
            test_file.writelines("%s\n" % param for param in params)
            test_file.close()
            cmd = r'' + proram_name + ' -p ' + test_path + ' ' + output_path
            PIPE = subprocess.PIPE
            p = subprocess.Popen(cmd, shell = True)
            with open(output_path) as file:
                test_output = [row.strip() for row in file]
                
            os.remove(output_path)
            os.remove(test_path)
            output_string += output_params_test(test_output, params) + "\n"
        except IOError:
            output_string += "TE02\n"

        output_file.write(output_string)
        

def main_function(argv):
    if (len(argv) == 1):
        print("TE04")
        return
        
    if (argv[2]):
        try:
            output_file = open(argv[2], 'w')
        except IOError:
            print("Path doesn's exist")
            return
    else:
        print("No output file name")
        return
    
    if (argv[1]):
        program_path = argv[1]
    else:
        output_file.write("TE03")
        return
    
    if (argv[3]):
        program_name = argv[3]
    else:
        output_file.write("TE03")
        return
    
    input_params_test(output_file, program_path, program_name)
    output_file.close()

       
def get_test_params():
    return {
        'test1': {},
        'test2': {'size=0','in_a_row=0','doors_count=0'},
        'test3': {'size=0','in_a_row=0'},
        'test4': {'size=0','doors_count=0'},
        'test5': {'in_a_row=0','doors_count=0'},
        'test6': {'size= 0','in_a_ row = 0','door s_coun t= 0'},
        'test7': {'size=','in_a_row=','doors_count='},
        'test8': {'size='},
        'test9': {'in_a_row='},
        'test10': {'doors_count='},
        'test11': {'size=','in_a_row=','doors_count='},
        'test12': {'size=10','in_a_row=2','doors_count=-1'},
        'test13': {'size=10','in_a_row=-1','doors_count=2'},
        'test14': {'size=-1','in_a_row=10','doors_count=1'},
        'test15': {'size=10','in_a_row=11','doors_count=5'},
        'test16': {'size=10','in_a_row=2','doors_count=51'}, 
        'test17': {'size=10','in_a_row=2','doors_count=4'},
        'test18': {'size=100','in_a_row=5','doors_count=25'}
        }


def get_errors_description():
    return {
        'IOE01':"Input file doesn't exist",
        'IOE02':"Incorrect input data",
        'IOE03':"Incorrect output data"
        }


if __name__ == "__main__":
    sys.exit(main_function(sys.argv))
