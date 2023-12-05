import matplotlib.pyplot as plt
import os

with open("D:\Python\#8_Advent of Code\Day_8_Treetop_Tree_Hause\input.txt", 'r') as f:
    data = f.read()
    
data_split = data.split("\n")

data_test =  """30373
25512
65332
33549
35390"""
data_test_split = data_test.split("\n")


def trees_no_the_edge(data: str) -> int:
    data = data.split('\n')
    number_of_trees_on_the_edge = len(data[0]) * 2
    number_of_trees_on_the_edge += len(data) * 2 - 4
    return number_of_trees_on_the_edge

### def
def day8(forest):
    ### move left, right, up and down
    moving = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    forest_dict = dict()
    for i, line in enumerate(forest):
        for j, tree in enumerate(line):
            forest_dict[(i, j)] = tree
   
    # the part of code to save and check forest dictionary         
    file = open("Day_8_Treetop_Tree_Hause/forest_dict.txt", "w")
    forest_str = str()
    for (y,x), tree in list(forest_dict.items()):
        forest_str += f"({y}, {x}), {tree}\n" 
    file.write(forest_str)
    file.close

    # list and dict is create to manual check the trees
    test_is_visible_list = list()
    test_is_visible_dict = dict()
    
    trees_visible_in_the_interior = 0
    forest_list = list(forest_dict.items())
    highest_scenic_score: int = 1
    high_scenic_score: int = 1
    temp: int = 0
    for (y, x), tree in forest_list:
        if x > 0 and x < forest_list[-1][0][-1] and y > 0 and y < forest_list[-1][0][0]:
            # print((y,x),tree)
            for dy, dx in moving:
                test_is_visible_list.clear()
                new_y, new_x = y, x
                is_visible = True
                while new_x > 0 and new_x < forest_list[-1][0][-1] and new_y > 0 and new_y < forest_list[-1][0][0] and is_visible:
                    new_y += dy
                    new_x += dx                
                    tree_to_check = forest_dict[(new_y, new_x)]
                    if tree > tree_to_check:
                        test_is_visible_list.append(((new_y, new_x), tree_to_check))
                        is_visible = True
                        temp += 1
                                    
                    if tree <= tree_to_check:
                        test_is_visible_list.clear()
                        is_visible = False
                        temp += 1
                        high_scenic_score *= temp
                        temp = 0
                        if highest_scenic_score < high_scenic_score:
                            highest_scenic_score = high_scenic_score
                            high_scenic_score = 1
                            
                            
                if is_visible:
                    test_is_visible_dict[((y, x), tree)] = test_is_visible_list.copy()
                    trees_visible_in_the_interior += 1
                    break
                
    file = open("Day_8_Treetop_Tree_Hause/forest_visable_dict.txt", "w")
    forest_dict_str = str()
    for viseble_tree in test_is_visible_dict:
        forest_dict_str += f"{viseble_tree}: {test_is_visible_dict[viseble_tree]}\n" 
    file.write(forest_dict_str)
    file.close
                                  
    print(highest_scenic_score)
    return trees_visible_in_the_interior, forest_dict

def forest_to_png(forest: list):
    plt.imshow(forest)
    plt.subplots_adjust(bottom=0.1, right=0.5, top=0.9)
    plt.xlabel('Trees in grid')
    plt.ylabel('Trees in grid')
    plt.text(x=10, y=-10 ,s='Forest grid', fontsize=10, fontweight='bold')
    plt.text(x=160, y=-35 ,s='High of trees', fontsize=10, fontweight='bold')
    cax = plt.axes([0.75, 0.1, 0.075, 0.8])
    plt.colorbar(cax=cax)
    plt.savefig(os.path.join('Day_8_Treetop_Tree_Hause','day_8_my_forest.png'))
    # plt.show()
        
# print('Part one answer:')
# trees_visible_in_the_interior, forest_dict = day8(data_split)
# print(trees_visible_in_the_interior, trees_no_the_edge(data), trees_visible_in_the_interior + trees_no_the_edge(data))
print('\nTests answer:')
trees_visible_in_the_interior_test, forest_dict_test = day8(data_test_split)
print(trees_visible_in_the_interior_test, trees_no_the_edge(data_test), trees_visible_in_the_interior_test + trees_no_the_edge(data_test))

forest_list = [[ int(tree) for tree in line ] for line in data.splitlines()]
forest_to_png(forest_list)
            
