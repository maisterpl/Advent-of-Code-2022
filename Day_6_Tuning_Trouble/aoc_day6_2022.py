

with open("input.txt", 'r') as f:
    data = f.read()
f.close()
# print(data)

def part_one(data, size):
    from_index = 0
    to_index = size

    while 1:
        ans = data[from_index: to_index]
        if len(set(ans)) == size: return to_index
        else:
            from_index += 1
            to_index += 1
        # print(to_index)
        
def better_method_to_answer_part_one_and_two(data, size):
    for i in range(len(data)):
        if len(set(data[i: i + size])) == size: return i + size

        
print(part_one("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4))        # 7
print(part_one("bvwbjplbgvbhsrlpgdmjqwftvncz", 4))          # 5
print(part_one("nppdvjthqldpwncqszvftbrmjlhg", 4))          # 6
print(part_one("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4))     # 10
print(part_one("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4))      # 11

print("Part one:",part_one(data, 4)) 


print(part_one("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14))       # 19
print("Part two:",part_one(data, 14)) 

print("Part one new method:",better_method_to_answer_part_one_and_two(data, 4)) 
print("Part two new method:",better_method_to_answer_part_one_and_two(data, 14)) 

