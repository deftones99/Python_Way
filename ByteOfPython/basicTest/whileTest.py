number = 10

running = True

while running:
    guess = int(input("Enter your number:"))

    if guess == number:
        print('Yes!Your are Right!')
        running = False
    elif guess > number:
        print('You need a little lowwer')
    else:
        print('You need a little higher')
else:
    print('Loop is over here')

print('Done')
