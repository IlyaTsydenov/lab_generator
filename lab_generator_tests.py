from lab_generator import LabGenerator
import time

 
class LabGenerator_tests():

    __output_string = ""

    def __get_size_array_for_tests(self):
        return {
            'test1': 10,
            'test2': 20,
            'test3': 40,
            'test4': 80,
            'test5': 160,
            'test6': 320
            }
    
    def generate_maze_array_test_in_size_return_array_size(self):
        """e.g. size = 10
        array_size = 100"""
        answer = "correct"
        size_array = self.__get_size_array_for_tests()
        for size in size_array:
            size = int(size_array[size])
            generator = LabGenerator(size,2,1)
            generator._LabGenerator__make_entrance()
            maze = generator._LabGenerator__generate_maze_array()
            size = size
            if(len(maze)*len(maze[0]) != size*size):
                answer = "incorrect"
            else:
                answer = "correct"
            self.__output_string += "size_test size = " + str(size) +\
                                    "array_size = " + str(len(maze)*len(maze[0])) +\
                                    ":" + answer + '\n'

    def make_entrance_test_in_size_return_entrance_and_exit(self):
        """e.g. size = 10
        entrance = 0,1
        exit = 9,1
        check out of range coords"""
        answer = "correct"
        size_array = self.__get_size_array_for_tests()
        for size in size_array:
            size = int(size_array[size])
            generator = LabGenerator(size,2,1)
            generator._LabGenerator__make_entrance()
            entr = generator._LabGenerator__entrance
            ex = generator._LabGenerator__exit
            if(entr[1] == 0 or entr[1] == size - 1):
                answer = "correct"
            elif(entr[0] == 0 or entr[0] == size -1):
                answer = "correct"
            else:
                answer = "incorrect"

            self.__output_string += "entr_exit_text size = " + str(size) +\
                                     "entrance:" + answer
            if((ex[1] == 0 or ex[1] == size - 1) and ex[0] != entr[0]):
                answer = "correct"
            elif((ex[0] == 0 or ex[0] == size -1) and ex[1] != entr[1]):
                answer = "correct"
            else:
                answer = "incorrect"

            self.__output_string += "; exit:" + answer + '\n'

    

    def get_all_tests(self):
         self.generate_maze_array_test_in_size_return_array_size()
         self.make_entrance_test_in_size_return_entrance_and_exit()
         return self.__output_string
        
