

def trees_no_the_edge(data: str) -> int:
    data = data.split('\n')
    number_of_trees_on_the_edge = len(data[0]) * 2
    number_of_trees_on_the_edge += len(data) * 2
    return number_of_trees_on_the_edge - 4


with open("D:\Python\#8_Advent of Code\Day_8_Treetop_Tree_Hause\input.txt", 'r') as f:
    data = f.read()


# print(trees_no_the_edge(data))

def check_trees_in_row_left(trees_in_row: str, position: int, value_to_check: int, highest_scenic_score: int = 0):
    if position > 0 and position < len(trees_in_row):
        if int(trees_in_row[value_to_check]) <= int(trees_in_row[position - 1]):
            highest_scenic_score += 1
            return 0, highest_scenic_score
        elif int(trees_in_row[value_to_check]) > int(trees_in_row[position - 1]):
            return check_trees_in_row_left(trees_in_row, position=position - 1, value_to_check=value_to_check, highest_scenic_score=highest_scenic_score + 1)
    return 1, highest_scenic_score

def check_trees_in_row_right(trees_in_row: str, position: int, value_to_check: int, highest_scenic_score: int = 0):
    if position > 0 and position < len(trees_in_row) - 1:
        if int(trees_in_row[value_to_check]) <= int(trees_in_row[position + 1]):
            highest_scenic_score += 1
            return 0, highest_scenic_score
        elif int(trees_in_row[value_to_check]) > int(trees_in_row[position + 1]):
            return check_trees_in_row_right(trees_in_row, position=position + 1, value_to_check=value_to_check, highest_scenic_score=highest_scenic_score + 1)
    return 1, highest_scenic_score

def check_trees_in_column_up(forest: list, number_of_column: int, number_of_tree: int, tree_to_check_column: int, highest_scenic_score: int = 0):
    if number_of_column > 0 and number_of_column < len(forest) - 1:
        tree_to_check_constans = forest[tree_to_check_column][number_of_tree]
        tree_to_check_2 = forest[number_of_column - 1][number_of_tree]
        if int(forest[tree_to_check_column][number_of_tree]) <= int(forest[number_of_column - 1][number_of_tree]):
            highest_scenic_score += 1
            return 0, highest_scenic_score
        elif int(forest[tree_to_check_column][number_of_tree]) > int(forest[number_of_column - 1][number_of_tree]):
            return check_trees_in_column_up(forest, number_of_column - 1, number_of_tree, tree_to_check_column, highest_scenic_score=highest_scenic_score + 1)
    return 1, highest_scenic_score

def check_trees_in_column_down(forest: list, number_of_column: int, number_of_tree: int, tree_to_check_column: int, highest_scenic_score: int = 0):
    if number_of_column > 0 and number_of_column < len(forest) - 1:
        tree_to_check_constans = forest[tree_to_check_column][number_of_tree]
        tree_to_check_2 = forest[number_of_column + 1][number_of_tree]
        if int(forest[tree_to_check_column][number_of_tree]) <= int(forest[number_of_column + 1][number_of_tree]):
            highest_scenic_score += 1
            return 0, highest_scenic_score
        elif int(forest[tree_to_check_column][number_of_tree]) > int(forest[number_of_column + 1][number_of_tree]):
            return check_trees_in_column_down(forest, number_of_column + 1, number_of_tree, tree_to_check_column, highest_scenic_score=highest_scenic_score + 1)
    return 1, highest_scenic_score

def trees_visible_in_the_interior(data: str) -> int:
    data = data.split('\n')
    trees_visible_in_the_interior = 0
    forest_without_edges = data[1:-1]
    trees_interior = []

    highest_scenic_score: int = 1
    temp: int = 1
    
    for trees_in_row in forest_without_edges:
        trees_in_row_without_edges = trees_in_row[1:-1]
        
        for tree in range(1, len(trees_in_row_without_edges) + 1):
            if int(trees_in_row[tree]) == 0:
                continue
            
            one_or_zero_in_row_left, scenic_score_from_left = check_trees_in_row_left(trees_in_row, tree, tree)
            temp *= scenic_score_from_left
            if one_or_zero_in_row_left:
                trees_interior.append(trees_in_row[tree])
                trees_visible_in_the_interior += 1
                
            
            one_or_zero_in_row_right, scenic_score_from_right = check_trees_in_row_right(trees_in_row, tree, tree)
            temp *= scenic_score_from_right
            if one_or_zero_in_row_right:
                trees_interior.append(trees_in_row[tree])
                trees_visible_in_the_interior += 1
                
            
            one_or_zero_in_col_up, scenic_score_from_up = check_trees_in_column_up(data, data.index(trees_in_row), tree, data.index(trees_in_row))
            temp *= scenic_score_from_up
            if one_or_zero_in_col_up:
                trees_interior.append(trees_in_row[tree])
                trees_visible_in_the_interior += 1
                
            
            one_or_zero_in_col_down, scenic_score_from_down = check_trees_in_column_down(data, data.index(trees_in_row), tree, data.index(trees_in_row))
            temp *= scenic_score_from_down
            if one_or_zero_in_col_down:
                trees_interior.append(trees_in_row[tree])
                trees_visible_in_the_interior += 1
                
            if temp > highest_scenic_score:
                highest_scenic_score = temp
            temp = 1
                
            
    # print(trees_interior)
    return trees_visible_in_the_interior, highest_scenic_score
        
trees_visible_in_the_interior_int, highest_scenic_score_int = trees_visible_in_the_interior(data)
print("Answer of part one:",trees_visible_in_the_interior_int + trees_no_the_edge(data))
print("Answer of part two:",highest_scenic_score_int)
print()

print('TESTS:')
data_test =  """30373
25512
65332
33549
35390"""
trees_visible_in_the_interior_int_test_1, highest_scenic_score_int_test_1 = trees_visible_in_the_interior(data_test)
print("Answer of part one:",trees_visible_in_the_interior_int_test_1 + trees_no_the_edge(data_test))
print("Answer of part two:",highest_scenic_score_int_test_1)

