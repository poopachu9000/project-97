import random
number = random.randint(1,10)
chances = 5
while(chances>0):
    guess = input('Guess a Number')
    if(guess == number):
        print('You win!')
    elif(guess < number):
        print('Your guess was too low. Please try again.')
    else:
        print('Your guess was too high. Please try again.')

print(number)