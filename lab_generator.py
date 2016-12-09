import random
from cell import Cell

class LabGenerator:
    #labyrinth string
    __lab_string = ""
    #labyrinth entrance
    __entrance = 0
    #labyrinth final exit
    __exit = 0
    #lab_keys_array
    __keys = 0
    #lab_doors_array
    __doors = 0
    
    __size = 0
    __in_a_row_count = 0
    __doors_count = 0

    
    def __init__(self, size, in_a_row_count, doors_count):
        self.__size = size
        self.__in_a_row_count = in_a_row_count
        self.__doors_count = doors_count
        self.__keys = []
        self.__doors = []

        
    def __generate_maze_array(self):
        entr = self.__entrance
        maze = []
        if(entr != 0):
            i = 0
            while(i < self.__size):
                j = 0
                maze.append([])
                while(j < self.__size):
                    maze[i].append(Cell(i,j))                   
                    j += 1
                i += 1
            i = 0
            while(i < self.__size):
                j = 0
                while(j < self.__size):
                    if((i-1) >= 0):
                        maze[i][j].put_neighbor(maze[i-1][j])   
                    if((j-1) >= 0):
                        maze[i][j].put_neighbor(maze[i][j-1])
                    if((i+1) < self.__size):
                        maze[i][j].put_neighbor(maze[i+1][j])
                    if((j+1) < self.__size):
                        maze[i][j].put_neighbor(maze[i][j+1])
                    j += 1
                i += 1
                
            maze[entr[0]][entr[1]].set_visit()
            return maze
        else:
            return "AE01"

     
    def generate(self):
        """
        Labyrinth generation by dfs's algorithm function
        
        :return: labyrinth packed as a string
        """
        
        entr = self.__make_entrance()
        maze = self.__generate_maze_array()
        i_act = self.__entrance[0]
        j_act = self.__entrance[1]
        actual = maze[i_act][j_act]
        stack = []
        maze_size = self.__size * self.__size-1
        p_doors_keys = round(maze_size/self.__doors_count)
        rand_number = 0
        start_cell = 0
        flag_i = 0
        flag_j = 0
        flag_key = 1
        flag_door = 0
        cell_count = 0
        
        while(maze_size != 0):
            rand_number = actual.have_neighbors()
            unvisited = []
            if(rand_number != 0):
                for neib in actual.get_neighbors():
                    if(neib.get_visit() == 0):
                        unvisited.append(neib)
            rand_number = len(unvisited)
            
            if(rand_number != 0): 
                if(flag_i == 0 and flag_j == 0):
                    start_cell = actual

                data = actual
                stack.append(data) 
                next_cell = self.__get_random_neighbor(rand_number, unvisited)
                if(next_cell.get_i() == i_act):
                    flag_i += 1
                    if(flag_i > self.__in_a_row_count):
                        actual.remove_neighbor(next_cell)
                        continue
                elif(next_cell.get_j() == j_act):
                    flag_j += 1
                    if(flag_j > self.__in_a_row_count):
                        actual.remove_neighbor(next_cell)
                        continue

                if(self.__doors_count != 0):
                    if(cell_count == round(random.uniform(cell_count,p_doors_keys-3)) or \
                       cell_count > p_doors_keys-3):
                        data = str(i_act)+':'+str(j_act)
                        if(flag_key and cell_count < p_doors_keys - 2 \
                           and len(self.__doors) < self.__doors_count):
                            self.__keys.append(data)
                            flag_key = 0
                            flag_door = 1
                        elif(flag_door):
                            self.__doors.append(data)
                            flag_key = 1
                            flag_door = 0
                            cell_count = 0
                    else:
                        cell_count += 1
                        
                if(next_cell.get_i() != i_act and flag_i != 0):
                    self.__put_in_string(i_act, start_cell.get_j(), i_act, j_act)
                    flag_i = 0
                    start_cell = actual    
                elif(next_cell.get_j() != j_act and flag_j != 0):
                    self.__put_in_string(start_cell.get_i(), j_act, i_act, j_act)
                    flag_j = 0
                    start_cell = actual
                    
                i_act = next_cell.get_i()
                j_act = next_cell.get_j()
                actual = maze[i_act][j_act]
                actual.set_visit()
                maze_size -= 1
                
                               
            elif(len(stack) > 0):
                if(flag_i != 0):
                    self.__put_in_string(i_act, start_cell.get_j(), i_act, j_act)    
                elif(flag_j != 0):
                    self.__put_in_string(start_cell.get_i(), j_act, i_act, j_act)
                    
                up = stack.pop()
                actual = up
                flag_i = 0
                flag_j = 0
                i_act = actual.get_i()
                j_act = actual.get_j()
                
        if(flag_i != 0):
            self.__put_in_string(i_act, start_cell.get_j(), i_act, j_act)
        elif(flag_j != 0):
            self.__put_in_string(start_cell.get_i(), j_act, i_act, j_act)


          
    def __get_random_neighbor(self, rand_number, neighbors):
        if(len(neighbors) == 0):
           return 0
        neib_num = int(round(random.uniform(0,rand_number-1)))
        return neighbors[neib_num]


    def __put_in_string(self, i1, j1, i2, j2):
        self.__lab_string += str(i1) + ':' + \
                             str(j1) + '-' + \
                             str(i2) + ':' + \
                             str(j2) + '\n'

         
    def __make_entrance(self):
        """
        :return: random entrance
        """
        size = self.__size
        i = round(random.uniform(0,size-1))
        if(i == 0 or i == size-1):
            j = round(random.uniform(0,size-1))
        else:
            j = round(random.uniform(0,1))
            if(j == 1):
                j = size-1
        self.__entrance = int(i),int(j)
        if(j == 0):
            self.__exit = round(random.uniform(0,size - 1)),size - 1
        elif(j == size - 1):
            self.__exit = round(random.uniform(0,size - 1)),0
        elif(i == 0):
            self.__exit = size - 1,round(random.uniform(0,size - 1))
        elif(i == size - 1):
            self.__exit = 0,round(random.uniform(0,size - 1))

        
    def get_lab_entr(self):
        """
        getter for __entrance
        :return: entrance cell
        """
        return self.__entrance

        
    def get_lab_exit(self):
        """
        getter for __exit
        :return: exit cell
        """
        return self.__exit


    def get_lab_string(self):
        """
        getter for __lab_string
        :return: Labyrinth as a string
        """
        return self.__lab_string


    def get_keys(self):
        return self.__keys

    def get_doors(self):
        return self.__doors
    
