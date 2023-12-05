from open_file import open_file
from monkey import Monkey

def day11(rounds: int = 20, file: str = 'D:\Python\#8_Advent of Code\Day_11_Monkey_in_the_Middle\\test_input.txt', divided_by_3_true_partone_false_part_two: bool = True):

    monkey_dict = open_file(file)
    monkey_class_list = []
    modulo = 1
    for i in monkey_dict:
        # print(i, monkey_dict[i])
        monkey_class_list.append(Monkey(i, monkey_dict[i]['Items'], monkey_dict[i]['Operation'],
                                        monkey_dict[i]['if_true'], monkey_dict[i]['if_false'],
                                        monkey_dict[i]['divisible_by']))
        modulo *= monkey_dict[i]['divisible_by']


    while rounds > 0:
        for monkey in monkey_class_list:
            if len(monkey.items) > 0:
                for item in monkey.items:
                    monkey.times_inspected += 1
                    new_item = monkey.make_operation(item, modulo)
                    if divided_by_3_true_partone_false_part_two == True:
                        new_item = monkey.divided_by_3(new_item)
                    #print(new_item)
                    test_return_true_or_false = monkey.test(new_item)
                    #print(test_return_true_or_false)
                    if test_return_true_or_false == True:
                        for monkey_number in monkey_class_list:
                            if monkey_number.monkey_number == monkey.if_true:
                                #print(monkey_number.monkey_number, monkey.if_true)
                                monkey_number.add_item(new_item)
                            #else: print('Error', monkey_number.monkey_number, monkey.if_true)
                    elif test_return_true_or_false == False:
                        for monkey_number in monkey_class_list:
                            if monkey_number.monkey_number == monkey.if_false:
                                #print(monkey_number.monkey_number, monkey.if_false)
                                monkey_number.add_item(new_item)
                            # else: 
                            #     print('Error', monkey_number.monkey_number, monkey.if_false)
                            #     print(type(monkey_number.monkey_number), type(monkey.if_false))
                    
                # if monkey.items.index(item) == len(monkey.items) - 1:
                monkey.clear_list()
                        
        # for i in monkey_class_list:
        #     print(i)
        # print(50*'=')
        # # input('Enter:')
                    
        rounds -= 1

    print(50*'=')
    monkey_list_of_inspected_items_times: list = []
    for monkey in monkey_class_list:
        print(f'Monkey: {monkey.monkey_number}, inspected items {monkey.times_inspected} times.')
        monkey_list_of_inspected_items_times.append(monkey.times_inspected)
    monkey_list_of_inspected_items_times.sort(reverse=True)
    print(50*'=')
    print(f'Monkey list sorted: {monkey_list_of_inspected_items_times}.')
    print(f'Answer part one: {monkey_list_of_inspected_items_times[0] * monkey_list_of_inspected_items_times[1]}.')

day11(rounds=20, divided_by_3_true_partone_false_part_two=True, file='input.txt')
day11(rounds=10_000, divided_by_3_true_partone_false_part_two=False, file='input.txt')
