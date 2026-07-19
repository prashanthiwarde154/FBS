#9. WAP to print all numbers in a range divisible by a given number.
start_range= int(input("Enter Start No. : "))
end_range= int(input("Enter End No. : ")) 
n = int(input("Enter No. : "))
for i in range (start_range,end_range+1):
    if(i%n==0):
        print(i)