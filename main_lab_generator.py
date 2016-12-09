import sys
from lab_generator import LabGenerator

def main_function(argv):
    if(len(argv) == 1):
        print("IOE04")
        return
    
    input_file_name = argv[1]
    output_file_name = argv[2]
    output_file = 0;
    input_file = 0;
    
    try:
        output_file = open(output_file_name, 'w')
    except IOError:
        print("Path doesn't exist")
        return
        
    try:
        input_file = open(input_file_name)
    except IOError:
        if(output_file):
            output_file.write("IOE01")
            output_file.close()
            return
        else:
            print("Input file doesn't exist")
            return
    
    input_list = input_file.readlines()
    if(len(input_list) != 3):
        output_file.write("IOE02")
        output_file.close()
        return
    
    for string in input_list:
        if((len(string) > 5) and (string[0:5] == "size=")):
            input_size = string[5:len(string)]
        elif((len(string) > 9) and (string[0:9] == "in_a_row=")):
            input_in_a_row = string[9:len(string)]
        elif((len(string) > 12) and (string[0:12] == "doors_count=")):
            input_doors_count = string[12:len(string)]
        else:
            output_file.write("IOE02")
            output_file.close()
            return
    try:
        input_size = int(input_size)
        input_in_a_row = int(input_in_a_row)
        input_doors_count = int(input_doors_count)
    except ValueError:
        output_file.write("IOE02")
        output_file.close()
        return
    
    
    if(input_size <= 0):
        output_file.write("IOE02")
        output_file.close()
        return
    
    if(input_in_a_row <= 0):
        output_file.write("IOE02")
        output_file.close()
        return
    
    if(input_doors_count < 0):
        output_file.write("IOE02")
        output_file.close()
        return
    
    generator = LabGenerator(input_size, input_in_a_row,
        input_doors_count)
    generator.generate()
    
    if(generator.get_lab_string()):
        output_file.write(generator.get_lab_string()\
                          + str(generator.get_doors()) + '\n' \
                          + str(generator.get_keys()))
        output_file.close()
    else:
        output_file.write("IOE03")
        output_file.close()
            


    
    
if __name__ == "__main__":
    sys.exit(main_function(sys.argv))

        
