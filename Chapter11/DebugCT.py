import random

guess = ''
choices = ['tails', 'heads']

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1)

if guess == choices[toss]:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if guess == choices[toss]:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
