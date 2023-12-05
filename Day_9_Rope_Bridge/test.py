from copy import deepcopy
import collections

test = [[1, 0], [2, 0], [3, 0], [14, 1], [4, 2], [4, 3], [3, 4], [2, 4], [3, 3], [4, 3], [3, 2], [2, 2], [1, -2], (1, -10)] 
print(len(test))
print([4, 3] in test)
print(test.count([4, 3]))

print('=' * 50)
start = (0, 0)
asd = [start]
asd.append([0,0])

print(asd)

print(set([(0,0), (0,1),(0,2),(0,2),(0,2),(0,2)]))

tx = 0
tx += 1 if 0 > 1 else -1
print(tx)


max_x =[ pos[0] for pos in set([(222,0), (11,1111),(0,2),(0,2),(0,2),(0,2)]) ]
print(max(max_x))
max_y =[ pos[1] for pos in set([(0,0), (0,1111),(0,-22),(0,2),(0,2),(0,2)]) ]
print(min(max_y))

print(abs(max(max_x)) + abs(min(max_y)))

board = [ ['X' for _ in range(10)] for next_line in range(10) ]
for line in board:
    print(line)
    
dictionary = {1: set([(0,0), (0,1111),(0,-22),(0,2),(1230,2),(0,2), (0,1111),(0,-22),(0,2),(1230,2),(0,2)]),
                2: set([(990,0), (990,1111),(0,-22),(0,222),(0,22),(0,2)])}
print( list( max([ pos[0] for pos in value_node ]) for value_node in list(dictionary.values())) )
print( list( min([ pos[1] for pos in value_node ]) for value_node in list(dictionary.values())) )


print(21 // 2)
