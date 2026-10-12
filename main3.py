secret= 7
guess= int(input("Guess the number:(1-10):"))   
while guess != secret:
    print("Wrong guess! Try again.")
    guess= int(input("Guess again: "))
print("Congratulations! You guessed the number.")