from copy import deepcopy

class Rope():
    def __init__(self, way_and_distand: list, rope_lenght: int = 10) -> None:      
        self.list_of_node = []
        self.way_and_distand = way_and_distand
        self.rope_lenght = rope_lenght

    def print_all_position_of_nodes(self):
        for node in self.list_of_node:
            number_node = str(self.list_of_node.index(node))
            print(number_node + ':')
            node.print_list_of_position()
            print()
            
    def print_all_position_of_nodes_without_repetitions(self):
        for node in self.list_of_node:
            print(len(node.list_of_position_with_out_repetitions()))
        
    def init_the_rope_lenght(self, rope_lenght):
        for _ in range(rope_lenght):
            self.list_of_node.append(Node())
            
    def get_all_position_from_nodes_without_repetitions(self):
        all_position_from_nodes_without_repetitions: dict() = {}
        for node in self.list_of_node:
            number_of_node = self.list_of_node.index(node)
            all_position_from_nodes_without_repetitions[number_of_node] = node.list_of_position_with_out_repetitions()
        return all_position_from_nodes_without_repetitions
                
    def move_node(self):
        MOVES_IN_WAY = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
        for direction_and_distans in self.way_and_distand:
            direction = direction_and_distans[0]
            distans = int(direction_and_distans[1])
            for dis in range(distans):
                dx, dy = list(MOVES_IN_WAY[direction])
                for number_of_node in range(len(self.list_of_node)):
                    if (number_of_node) > len(self.list_of_node) - 2:
                        break            
                    node_previous = self.list_of_node[number_of_node]
                    node_behind =  self.list_of_node[number_of_node + 1]
                    
                    hx = (node_previous.list_of_postposition[-1][0])
                    hy = (node_previous.list_of_postposition[-1][1])
                    
                    if node_previous == self.list_of_node[0]:
                        hx += dx
                        hy += dy 
                        node_previous.list_of_postposition.append([hx, hy])  
                                         
                    tx = node_behind.list_of_postposition[-1][0]
                    ty = node_behind.list_of_postposition[-1][1]
                    
                    if abs(hx - tx) > 1:
                        tx += 1 if hx > tx else -1
                        if abs(hy - ty) != 0:
                            ty += 1 if hy > ty else -1
                        node_behind.list_of_postposition.append([tx, ty])
                    elif abs(hy - ty) > 1:
                        ty += 1 if hy > ty else -1
                        if abs(hx - tx) != 0:
                            tx += 1 if hx > tx else -1
                        node_behind.list_of_postposition.append([tx, ty])
                    else:
                        node_behind.list_of_postposition.append([tx, ty])
            

class Node():
    def __init__(self) -> None:
        self.start_position = [0, 0]
        self.list_of_postposition = [self.start_position]
        self.number_of_diferent_position: int = 0
        
    def print_list_of_position(self):
        for pos in range(len(self.list_of_postposition)):
            print(f"{pos}: {self.list_of_postposition[pos]}", end=" ")
        print(f"Node moves: {len(self.list_of_postposition)}")
        
    def list_of_position_with_out_repetitions(self):
        list_of_position_with_out_repetitions = []
        for pos in self.list_of_postposition:
            list_of_position_with_out_repetitions.append(tuple(pos))
            self.number_of_diferent_position = len(set(list_of_position_with_out_repetitions))
        return set(list_of_position_with_out_repetitions)
    

class Board():
    def __init__(self, all_position_lenght_rope: dict) -> None:
        self.all_position_lenght_rope = all_position_lenght_rope
        self.max_x, self.min_x, self.max_y, self.min_y = self.__get_max_and_min_value_from_dictionary()
        self.x_dimention = abs(self.max_x) + abs(self.min_x)
        self.y_dimention = abs(self.max_y) + abs(self.min_y)
        self.board = [ ['.' for _ in range(self.y_dimention + 2)] for next_line in range(self.x_dimention + 2) ]
        
    def __get_max_and_min_value_from_dictionary(self):
        
        max_x = max(list(max([ pos[0] for pos in value_node ]) for value_node in list(self.all_position_lenght_rope.values())))
        max_y = max(list(max([ pos[1] for pos in value_node ]) for value_node in list(self.all_position_lenght_rope.values())))
        min_x = min(list(min([ pos[0] for pos in value_node ]) for value_node in list(self.all_position_lenght_rope.values())))
        min_y = min(list(min([ pos[1] for pos in value_node ]) for value_node in list(self.all_position_lenght_rope.values())))
        # print(max_x, min_x, max_y, min_y)
        return max_x, min_x, max_y, min_y
        
    def print_empty_board(self):
        for line in self.board:
            for char in line:
                print(char, end='')
            print()
        
    def write_last_node_positions_on_board(self):
        node_on_board = self.board.copy()
        last_node = list(self.all_position_lenght_rope.values())[-1]
        min_x_from_last_node = abs(min( [pos[0]] for pos in last_node )[0])
        min_y_from_last_node = abs(min( [pos[1]] for pos in last_node )[0])
        for pos_x in range(len(node_on_board[0])):
            for line_y in range(len(node_on_board)):
                for last_node_x, last_node_y in last_node:
                    if (last_node_x + min_x_from_last_node, last_node_y + min_y_from_last_node) == (pos_x, line_y):
                        node_on_board[last_node_y + min_y_from_last_node][last_node_x + min_x_from_last_node] = '#'    
        return node_on_board
    
    
def import_file_with_data(path: str):
    with open(path, 'r') as f:
        data = f.read()
    f.close()
    return data    
        
def main():
    # path_file_with_data = 'Day_9_Rope_Bridge\example_to_part_2.txt'
    # path_file_with_data = 'D:\Python\#8_Advent of Code\Day_9_Rope_Bridge\\test_data_input.txt'
    path_file_with_data = 'D:\Python\#8_Advent of Code\Day_9_Rope_Bridge\input.txt'
    data = import_file_with_data(path=path_file_with_data).splitlines()
    data = [line.split(' ') for line in data]
    
    rope = Rope(way_and_distand=data)
    rope.init_the_rope_lenght(rope_lenght=10)
    rope.move_node()
    rope.print_all_position_of_nodes_without_repetitions()
    dictionaty_with_key_nodes_and_value_all_position_node = rope.get_all_position_from_nodes_without_repetitions()
    
    board = Board(dictionaty_with_key_nodes_and_value_all_position_node)
    print()
    
    last_node_on_board = board.write_last_node_positions_on_board()
    for line in last_node_on_board:
        for char in line:
            print(char, end='')
        print()
    
main()