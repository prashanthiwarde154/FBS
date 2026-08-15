li = [[1,3],[2,4],[4,1],[3,2]]
min=0
valList = []
for i in range(len(li)):
    # print(li[i][1]>min)
    val = li[i][1]
    valList.append(val)
valList.sort()
print(valList)
    
