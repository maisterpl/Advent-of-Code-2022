

data = []
temp = 0
with open("input.txt", "r") as f:
    # print(f.read().split("\n\n"))
    for line in f.read().split("\n\n"):
        print(line.split())
        for c in line.split():
            temp += int(c)
        data.append(temp)
        temp = 0
        
print(sorted(data, reverse=True))
print(max(data))
print(sorted(data, reverse=True)[:3])
print("\n\n")


with open("input.txt", "r") as f:
    datav2 = sorted([ sum(int(x) for x in line.split()) for line in f.read().split("\n\n")], reverse=True)

print(f"Max value: {datav2[0]}")
print(f"Max value: { max(datav2) }")
print(f"Best 3th values: {datav2[:3]}")
print(f"Sum of best 3th values: {sum(datav2[:3])}")
