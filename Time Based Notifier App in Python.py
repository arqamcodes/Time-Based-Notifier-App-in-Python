import time
timestamp = time.strftime('%H:%M')
print(timestamp)

currenthour = int(time.strftime('%H'))
print("Current Hour:", currenthour)

currentmin = int(time.strftime('%M'))
print("Current Minutes:", currentmin)

if (currenthour < 12):
    print("Good morning")   
elif(currenthour > 12 and currenthour <= 17 ):
    print("Good Evening") 
else:
    print("Good Night")   



