#1.convert the time entered in hh , min and sec into seconds.

hours = int (input('Enter Hours :'))
min=int(input('Enter Minuts :'))
sec = int(input('Enter Seconds :'))

seconds =(hours*3600)+(min*60)+sec
print(f'Total Seconds in the given time {hours}:{min}:{sec} is :- {seconds} seconds')

