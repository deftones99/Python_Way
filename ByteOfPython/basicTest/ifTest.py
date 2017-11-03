number = 10
guess = int(input("Enter an Interger:"));

if number == guess:
    print("Yes!! You are guess the right number!")

elif number < guess:
    print("you need a little lowwer")

elif number > guess:
    print('you need a little higher')

print("Done!")
