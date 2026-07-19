# 11. Accept age of five people and also per person ticket amount and then calculate total
#     amount to ticket to travel for all of them based on following condition :
#     a. Children below 12 = 30% discount
#     b. Senior citizen (above 59) = 50% discount
#     c. Others need to pay full.

age1=int(input('Enter age for Person 1 : '))
amount1=int(input("Emount for Persion 1 :"))
if(age1<=12):
    dis1=amount1*0.3
    T1=amount1-dis1
elif(age1>=59):
    dis1=amount1*0.5
    T1=amount1-dis1
else:
    dis1=amount1
    T1=amount1
#Person 1 Ends -----------------
age2=int(input('Enter age for Person 2 : '))
amount2=int(input("Emount for Persion 2 :"))
if(age2<=12):
    dis2=amount2*0.3
    T2=amount2-dis2
elif(age2>=59):
    dis2=amount2*0.5
    T2=amount2-dis2
else:
    dis2=amount2
    T2=amount2
#Person 2 Ends -----------------
age3=int(input('Enter age for Person 3 : '))
amount3=int(input("Emount for Persion 3 :"))
if(age3<=12):
    dis3=amount3*0.3
    T3=amount3-dis3
elif(age3>=59):
    dis3=amount3*0.5
    T3=amount3-dis3
else:
    dis3=amount3
    T3=amount3
#Person 3 Ends -----------------
age4=int(input('Enter age for Person 4 : '))
amount4=int(input("Emount for Persion 4 :"))
if(age4<=12):
    dis4=amount4*0.3
    T4=amount4-dis4
elif(age4>=59):
    dis4=amount4*0.5
    T4=amount4-dis4
else:
    dis4=amount4
    T4=amount4
#Person 4 Ends -----------------
age5=int(input('Enter age for Person 5 : '))
amount5=int(input("Emount for Persion 5 :"))
if(age5<=12):
    dis5=amount5*0.3
    T5=amount5-dis5
elif(age5>=59):
    dis5=amount5*0.5
    T5=amount5-dis5
else:
    dis5=amount5
    T5=amount5
#Person 5 Ends -----------------
Total=T1+T2+T3+T4+T5
print("Your Total ticket Price is for 5 person :" ,Total)