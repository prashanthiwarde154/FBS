#12. Write a program to create three lists of numbers, their squares
#   and cubes
li = [1,2,3,4,5,6,7,8,9,10]
sq=0
cu=0
square=[]
cube=[]
for i in range(len(li)):
    sq = li[i]**2
    square.append(sq)
    cu = li[i]**3
    cube.append(cu)
print(f'Square List :- {square}')
print(f'Cube List :- {cube}')