
class Cell:
    __i = 0
    __j = 0
    __visited = 0
    __neighbors = 0

    def __init__(self,i,j):
        self.__i = i
        self.__j = j
        self.__neighbors = []


    def have_neighbors(self):
        return len(self.__neighbors)
        
    def get_neighbors(self):
        return self.__neighbors
    
    def put_neighbor(self, neighbor):
        self.__neighbors.append(neighbor)

    def remove_neighbor(self, neighbor):
        self.__neighbors.remove(neighbor)

    def set_visit(self):
        self.__visited = 1

    def get_visit(self):
        return self.__visited

    def get_i(self):
        return self.__i

    def get_j(self):
        return self.__j
