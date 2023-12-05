
def open_file(file: str):
    with open(file, 'r') as f:
        monkey = f.read().split('Monkey')
        monkey_dict = {}
        for i, n in enumerate(monkey):
            temp = n.split()

            if len(temp) > 1:
                monkey_dict[int(temp[0][0])] = {
                    'Items': [ int(i.replace(',', '')) if len(i) > 2 else int(i) for i in temp[temp.index('items:')+1 : temp.index('Operation:')] ],
                    'Operation': temp[temp.index('Operation:')+3 : temp.index('Test:')],
                    'divisible_by': int(temp[temp.index('by')+1 : temp.index('If')][0]),
                    'if_true': temp[temp.index('true:')+4],
                    'if_false': temp[temp.index('false:')+4],
                    }
        
    return monkey_dict 
    