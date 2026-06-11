import time
timer = int(input("Enter The Time You Want to Start Countdown: "))

print("\n Countdown Starts In :")
for i in range(timer, 0, -1):
    print(i)
    time.sleep(1)

print("\n WOHOOO! Happy New Year")