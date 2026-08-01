#3. Accept no. of passengers from user and per ticket cost. Then accept age of each
#   passenger and then calculate total amount to ticket to travel for all of them based on
#   following condition :
#   a. Children below 12 = 30% discount
#   b. Senior citizen (above 59) = 50% discount
#   c. Others need to pay full.


passenger= int(input("Enter No. of Passengers : "))
cost=int(input("Enter The Cost of ticket : "))
count=1
for i in range(1,passenger+1):
    age=int(input(f'Enter Age for Passenger {count} : '))
    if(age<12):
        sum=cost*0.3
        print(f'Your Ticket Price is {sum}')
    elif(age>59):
        sum=cost*0.5
        print(f'Your Ticket Price is {sum}')
    else:
        print(f'Your Ticket Price is {cost}')
    count+=1

        
    