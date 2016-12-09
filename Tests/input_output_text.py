import subprocess
import sys
import os
import traceback


def output_params_test(test_output, params):
    size = 0
    in_a_row = 0
    doors_count = 0
    
    if (len(test_output) == 0):
        return "Test not successful. Program's algorithm exception"
    if(len(params)):
        param_array = []
        for param in params:
            param_array.append(param)

        for param in param_array:
            if (len(param) > 5 and (param[0:5] == "size=")):
                size = param[5:len(param)]
        
            if (len(param) > 9 and (param[0:9] == "in_a_row=")):
                in_a_row = param[9:len(param)]
        
            if (len(param) > 12 and (param[0:12] == "doors_count=")):
                doors_count = param[12:len(param)]

    
    errors_desc = get_errors_description()

    if test_output[0] in errors_desc:
        return errors_desc[test_output[0]]

    previous = 0
    length = 0
    for string in test_output:
        if(string == test_output[len(test_output) - 2]):
            break
           
        coord_list = string.split('-')
        first_x_y = coord_list[0].split(':')
        second_x_y = coord_list[1].split(':')
        if (first_x_y[0] == second_x_y[0]):
            output_in_a_row = abs(int(first_x_y[1])-int(second_x_y[1]))
            length += output_in_a_row
        elif (first_x_y[1] == second_x_y[1]):
            output_in_a_row = abs(int(first_x_y[0])-int(second_x_y[0]))
            length += output_in_a_row
            
        if (output_in_a_row > in_a_row):
            return "Incorrect in_a_row treatment"
        
        previous = coord_list[1]

    doors = test_output[len(test_output) - 2].split(',')
    keys = test_output[len(test_output) - 1].split(',')
    
    try:
        size = int(size)
        doors_count = int(doors_count)
    except Exception:
        return "Incorrect input data"
    
    if (len(doors) > len(keys)):
        return "Incorrect program output. Doors count > keys count"

    if (len(doors) != doors_count):
        return "Incorrect program output. \
        Doors count not complies input doors count"
        
    if ((size*size) != length+1):
        return "Incorrect program output. Program algoritm error. \
        Size by coords not complies input size"

    return "Test successful"
        

def input_params_test(output_file, program_path, program_name):
    flag = 1
    for test_name,params in get_test_params().items():
        output_string = test_name + '\n'
        test_path = program_path + '/' + test_name
        output_path = program_path + '/test_output_' + test_name
        try:
            test_file = open(test_path, 'w')
            test_file.writelines("%s\n" % param for param in params)
            test_file.close()
            cmd = r''+ "python " + program_path + '/' +  program_name + ' ' \
                  + test_path + ' ' + output_path
            PIPE = subprocess.PIPE
            p = subprocess.Popen(cmd, shell = True)
            print(output_path)
            with open(output_path) as file:
                if(file):
                    test_output = [row.strip() for row in file]
                
            output_string += output_params_test(test_output, params) + "\n"
        except IOError:
            if(flag):
                print('Error:\n', traceback.format_exc())
                flag = 0
            output_string += "TE02\n"

        output_file.write(output_string)
        

def main_function(argv):
    if (len(argv) == 1):
        print("TE04")
        return
        
    if (argv[1]):
        try:
            output_file = open(argv[1], 'w')
        except IOError:
            print("Path doesn's exist")
            return
    else:
        print("No output file name")
        return
    
    if (argv[2]):
        program_path = argv[2]
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
        'test17': {'size=10','in_a_row=2','doors_count=3'},
        'test18': {'size=20','in_a_row=3','doors_count=5'}
        }


def get_errors_description():
    return {
        'IOE01':"Input file doesn't exist",
        'IOE02':"Incorrect input data",
        'IOE03':"Incorrect output data"
        }


if __name__ == "__main__":
    sys.exit(main_function(sys.argv))
