import copy

def day_5_part_1(moves, massege_data_dict):

    def moves_to_another_location(times: int, from_pos: int, to_pos: int, data_dict: dict):
        while times > 0:
            data_dict[to_pos].insert(0, data_dict[from_pos][0]) 
            data_dict[from_pos].pop(0)
            times -= 1
            
    # print(massege_data_dict)

    for i in moves:
        # print(i)
        moves_to_another_location(i[0], i[1], i[2], massege_data_dict)
        
    # print(massege_data_dict)

    print(''.join([ massege_data_dict[n][0] for n in massege_data_dict ]))
    
def day_5_part_2(moves, massege_data_dict):

    def moves_to_another_location(times: int, from_pos: int, to_pos: int, data_dict: dict):
        times_part_2: int = times
        while times > 0:
            data_dict[to_pos].insert(0, data_dict[from_pos][times - 1])
            times -= 1
       
        while times_part_2 > 0:
            data_dict[from_pos].pop(0)
            times_part_2 -= 1
            
    # print(massege_data_dict)

    for i in moves:
        # print(i)
        moves_to_another_location(i[0], i[1], i[2], massege_data_dict)
        
    # print(massege_data_dict)

    print(''.join([ massege_data_dict[n][0] for n in massege_data_dict ]))


def main():
    with open("input.txt", "r") as f:
        massege_data , moves = f.read().split("\n\n")
        massege_data = massege_data.splitlines()
        massege_data = zip(*massege_data)
        massege_data = [ i for i in massege_data if i[-2].isalpha() ]
        
        massege_data_dict = {    }
        for n in massege_data:
            massege_data_dict[int(n[-1])] = [ a for a in n[:-1] if a != " "]

        moves = [ [ int(n) for n in m.split(" ") if n.isdigit() ] for m in moves.splitlines() ]
    f.close()
    
    massege_data_dict_to_part_2 = copy.deepcopy(massege_data_dict)
    print('Part one: ', end='')
    day_5_part_1(moves, massege_data_dict)
    print('Part two: ', end='')
    day_5_part_2(moves, massege_data_dict_to_part_2)
    
main()
