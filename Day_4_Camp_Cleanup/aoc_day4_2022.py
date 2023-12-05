

with open("input.txt", "r") as f:
    data = f.read().splitlines()
    data = [ [ [ int(g) for g in k.split("-") ] for k in e.split(",") ] for e in data ]  
f.close()

'''
print(data)
print()
print(data[0])
print(data[0][0])
print(data[0][0][0])
'''

elves = 0
for one in data:
    if int(one[0][0]) >= int(one[1][0]) and int(one[0][1]) <= int(one[1][1]):
        # print("First: ", one[0][0], one[1][0], one[0][1], one[1][1])
        elves += 1
    elif int(one[0][0]) <= int(one[1][0]) and int(one[0][1]) >= int(one[1][1]):
        # print("Second: ", one[0][0], one[1][0], one[0][1], one[1][1])
        elves += 1
        
print(f"\nPart one: { elves }")

elves_v2 = 0
for sec in data:
    if sec[0][0] in range(sec[1][0], sec[1][1] + 1):
        elves_v2 += 1
        #print(f"1: {sec}")
    elif sec[0][1] in range(sec[1][0], sec[1][1] + 1):
        elves_v2 += 1
        #print(f"2: {sec}")
    elif sec[1][0] in range(sec[0][0], sec[0][1] + 1):
        elves_v2 += 1
        #print(f"3: {sec}")
    elif sec[1][1] in range(sec[0][0], sec[0][1] + 1):
        elves_v2 += 1
        #print(f"4: {sec}")
    else:
        #print(f"5: {sec}")
        pass
        
print(f"\nPart two: { elves_v2 }")
