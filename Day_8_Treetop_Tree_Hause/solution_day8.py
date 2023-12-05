import numpy as np
import matplotlib.pyplot as plt
import os


def save_forest_to_png(array):
    plt.imshow(array)
    plt.xticks([])
    plt.yticks([])
    # plt.show()
    plt.savefig(os.path.join('Day_8_Treetop_Tree_Hause','8-forest.png'))


def solution1():
    input_list = open("D:\Python\#8_Advent of Code\Day_8_Treetop_Tree_Hause\input.txt", 'r').readlines()
    input_lists = np.array([[int(el) for el in current_list.strip()] for current_list in input_list])
    border_visible = 2 * ((input_lists.shape[0] - 1) + (input_lists.shape[1] - 1))
    save_forest_to_png(input_lists)

    # going from top
    visible_trees = []
    for row in range(1, input_lists.shape[0] - 1):
        current_row = input_lists[row, 1:-1]
        max_heights = np.max(input_lists[:row, 1:-1], axis=0)
        visible_trees.extend([(row, el + 1) for el in np.where(current_row > max_heights)[0]])

    # from down
    for row in range(input_lists.shape[0] - 1, 1, -1):
        current_row = input_lists[row - 1, 1:-1]
        max_heights = np.max(input_lists[row:, 1:-1], axis=0)
        visible_trees.extend([(row - 1, el + 1) for el in np.where(current_row > max_heights)[0]])

    # from left
    for column in range(1, input_lists.shape[1] - 1):
        current_column = input_lists[1:-1, column]
        max_heights = np.max(input_lists[1:-1, :column], axis=1)
        visible_trees.extend([(el + 1, column) for el in np.where(current_column > max_heights)[0]])

    # from right
    for column in range(input_lists.shape[1] - 1, 1, -1):
        current_column = input_lists[1:-1, column - 1]
        max_heights = np.max(input_lists[1:-1, column:], axis=1)
        visible_trees.extend([(el + 1, column - 1) for el in np.where(current_column > max_heights)[0]])

    return len(set(visible_trees)) + border_visible

print(solution1())