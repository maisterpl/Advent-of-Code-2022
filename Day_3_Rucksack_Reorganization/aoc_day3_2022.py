

lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = lowercase.upper()
points = 0

with open("D:\Python\#8_Advent of Code\Day_3_Rucksack_Reorganization\input.txt", "r") as f:
    data = [ line for line in f.read().split("\n")] 
    
    # Part one:
    for r in data:
        size = len(r)
        r1 = r[:int(size/2)]
        r2 = r[int(size/2):]

        #print('=' * 50)
        #print(r)
        #print(r1, r2)
        
        for x in r1:
            if x in r2:
                #print(x)
                if x in lowercase:
                    points += (lowercase.index(x) + 1)
                    #print(lowercase.index(x) + 1)
                    break
                else:
                    points += (uppercase.index(x) + 27)
                    #print(uppercase.index(x) + 27)
                    break
      
    # Part two:
    data2 = []
    temp = []
    points2 = 0
    high_r = ''
    for i in data:
        if data.index(i) > 0 and data.index(i) % 3 == 0:
            data2.append(temp)
            temp = []
        temp.append(i) 
        
    for r3 in data2:
        print(r3)
        for r in r3:
            if len(high_r) < len(r):
                high_r = r

        r3.remove(high_r)
        print(high_r)
        print(r3)
        for r1 in high_r:
            print(r1)
            if r1 in r3[0] and r1 in r3[1]:
                if r1 in lowercase:
                    points2 += (lowercase.index(r1) + 1)
                    print(lowercase.index(r1) + 1)
                    break
                else:
                    points2 += (uppercase.index(r1) + 27)
                    print(uppercase.index(r1) + 27)
                    break
        high_r = ''
        
##########################################################################################
    data3 = []
    temp = []
    high_r = ''
    points3 = 0
    for j, i in enumerate(data):
        if j>0 and j % 3 == 0:
            data3.append(temp)
            temp = []
        temp.append(i)

    for i in data3:
        try:
            #print(i)
            s = (set(i[0]) & set(i[1]) & set(i[2])).pop()  
            #print(s)   
            if s in lowercase:
                points3 += (lowercase.index(s) + 1)
                #print(lowercase.index(s) + 1)

            else:
                points3 += (uppercase.index(s) + 27)
                #print(uppercase.index(s) + 27)
            #print(f"Part two_v2: { points3 }")
        except:
            print(KeyError)
    #print(len(data3))

                

f.close()

print(f"Part one: { points }")

print(f"Part two: { points2 }")
print(f"Part two_v2: { points3 }")
