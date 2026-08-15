#3. Write a program to find the second largest element in the list.
def sec_largest(li):
    max = li[0]
    secmax = li[0]
    for i in range(0,len(li)):
        if(li[i] > max):
            max = li[i]
    for i in range(0,len(li)):
        if(li[i] > secmax and li[i] < max):
            secmax = [li[i]]
    print("Second Max of the List :-",secmax)

li = [6,5,4,3,1,88]
sec_largest(li)