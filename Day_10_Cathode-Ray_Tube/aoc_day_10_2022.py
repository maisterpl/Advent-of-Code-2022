
def signal_strength_part_one(data: list):
    finding_signals_strength: tuple = (20, 60, 100, 140, 180, 220)
    cycle: int = 0
    x: int = 1
    signal_strengths: list = []
    signal_strengths_sum: int = 0

    for digit in data:
        if digit != 0:
            cycle += 1
            if cycle in finding_signals_strength:
                signal_strengths.append((cycle , x, (cycle ) * x))
            cycle += 1
            if cycle in finding_signals_strength:
                signal_strengths.append((cycle , x, (cycle ) * x)) 
            x += digit
        elif digit == 0:
            cycle += 1
            if cycle in finding_signals_strength:
                signal_strengths.append((cycle , x, (cycle ) * x)) 

    signal_strengths_sum = sum([signal[2] for signal in signal_strengths])
    return signal_strengths_sum, signal_strengths

def prepare_data(data: str):
    data_only_digits = [[int(integer) for integer in line.split(" ") if '-' in integer or integer.isdigit()] for line in data.splitlines()]
    new_data: list = []
    for digit in data_only_digits:
        if len(digit) == 0:
            new_data.append(0)
        else:
            new_data.append(digit[0])
    return new_data

def openfile(path: str):
    with open(path, 'r') as file:
        data = file.read()
    file.close()
    return data

def CRT_drawing(data: list):
    hash_index_position_in_sprite: list = [0, 1, 2]
    CRT_40_wide_6_high: list = [[] for i in range(6)]
    CRT_line = 0
    x: int = 1
    cycle: int = 0
    for digit in data: 
        if digit != 0:
            if cycle in hash_index_position_in_sprite:
                CRT_40_wide_6_high[CRT_line].append('#')
            else:
                CRT_40_wide_6_high[CRT_line].append('.')            
            cycle += 1
            if cycle > 39: cycle = 0 
            if len(CRT_40_wide_6_high[CRT_line]) == 40: CRT_line += 1
            if cycle in hash_index_position_in_sprite:
                CRT_40_wide_6_high[CRT_line].append('#')
            else:
                CRT_40_wide_6_high[CRT_line].append('.')  
            cycle += 1
            if cycle > 39: cycle = 0 
            if len(CRT_40_wide_6_high[CRT_line]) == 40: CRT_line += 1
            x += digit
            hash_index_position_in_sprite = [ x - 1, x, x + 1 ]

        elif digit == 0:
            if cycle in hash_index_position_in_sprite:
                CRT_40_wide_6_high[CRT_line].append('#')
            else:
                CRT_40_wide_6_high[CRT_line].append('.')  
            cycle += 1
            if cycle > 39: cycle = 0 
            if len(CRT_40_wide_6_high[CRT_line]) == 40: CRT_line += 1
    
    for line in CRT_40_wide_6_high:
        for char in line:
            print(char, end='')
        print()


def main():
    path_to_input_file: str = '.\input.txt'
    path_to_example_input: str = '.\example_part_one.txt'

    data = openfile(path_to_input_file)
    new_data = prepare_data(data)
    signal_strength_sum_of_part_one, signal_strength_list_of_cycle_and_val_X_part_one  = signal_strength_part_one(new_data)
    print('The part one answer is:',signal_strength_sum_of_part_one)
    
    CRT_drawing(new_data)

main()

