dict_test = {
    ((3, 3), 4): [1,3,7],
    ((3, 4), 9): [12,34,5,4],
    ((4, 0), 3): [],
    ((4, 1), 5): [],
    ((4, 2), 3): [],
    ((4, 3), 9): [],
    ((4, 4), 0): [],
}

for i in dict_test:
    print(i, dict_test[i])
print()

list_test = list()
list_test.append(999)
dict_test[((4, 2), 3)] = list_test.copy()
list_test.clear()

for i in dict_test:
    print(i, dict_test[i])
