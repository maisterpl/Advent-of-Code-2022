
def save_file(name: str, data: list):
    with open(name, 'w') as file:
        for d in data:
            f, s = d
            a, b = f
            c, e = s
            file.writelines(f"[{a},{b}] : [{c},{e}]\n")
    file.close()

def import_file_with_data(path: str):
    with open(path, 'r') as f:
        data = f.read()
    f.close()
    return data

def move_T_and_H(way_and_distand: list):
    START = [0, 0]
    hx, hy = START
    tx, ty = START
    MOVES_IN_WAY = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    moves_of_H = [START]
    moves_of_T = [START]
    # test_H_and_T = []

    for direction_and_distans in way_and_distand:
        direction = direction_and_distans[0]
        distans = int(direction_and_distans[1])
        for dis in range(distans):
            dx, dy = list(MOVES_IN_WAY[direction])
            hx, hy = hx + dx, hy + dy
            # moves_of_H.append([hx, hy])
            
            if abs(hx - tx) > 1 and direction == 'R':
                tx = hx - 1
                ty = hy
                if [tx, ty] not in moves_of_T:
                    moves_of_T.append([tx, ty])
            elif abs(hx - tx) > 1 and direction == 'L':
                tx = hx + 1
                ty = hy
                if [tx, ty] not in moves_of_T:
                    moves_of_T.append([tx, ty])
            elif abs(hy - ty) > 1 and direction == 'U':
                tx = hx
                ty = hy - 1
                if [tx, ty] not in moves_of_T:
                    moves_of_T.append([tx, ty])
            elif abs(hy - ty) > 1 and direction == 'D':
                tx = hx
                ty = hy + 1
                if [tx, ty] not in moves_of_T:
                    moves_of_T.append([tx, ty])
            # test_H_and_T.append(([hx, hy], [tx, ty]))

    # print("H:",len(moves_of_H))
    # print(moves_of_H)
    print("T:",len(moves_of_T))
    # print(moves_of_T)
    # print(len(test_H_and_T))
    # print(test_H_and_T)
    # save_file("check.txt", test_H_and_T)
    
def move_9T_and_H_part_2(way_and_distand: list):
    START = [0, 0]
    hx, hy = START
    tx, ty = START
    MOVES_IN_WAY = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    moves_of_H = [START]
    moves_of_T = [START]

    for direction_and_distans in way_and_distand:
        direction = direction_and_distans[0]
        distans = int(direction_and_distans[1])
        for dis in range(distans):
            dx, dy = list(MOVES_IN_WAY[direction])
            hx, hy = hx + dx, hy + dy
                


def main():
    path_of_example_file_with_data = 'D:\Python\#8_Advent of Code\Day_9_Rope_Bridge\example_aoc_d9.txt'
    data = import_file_with_data(path=path_of_example_file_with_data).splitlines()
    data = [line.split(' ') for line in data]
    # print(data)
    move_T_and_H(data)

    path_file_with_data = 'D:\Python\#8_Advent of Code\Day_9_Rope_Bridge\input.txt'
    data = import_file_with_data(path=path_file_with_data).splitlines()
    data = [line.split(' ') for line in data]
    # print(data)
    move_T_and_H(data)
    
    path_file_with_data = 'Day_9_Rope_Bridge\example_to_part_2.txt'
    data = import_file_with_data(path=path_file_with_data).splitlines()
    data = [line.split(' ') for line in data]
    # print(data)

main()
