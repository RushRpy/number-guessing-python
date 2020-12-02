import random
number = random.randint(1,10)

number_of_guesses=0
player_name = input('Your Name: ')
print(f'Hello {player_name} Guess a number  between 1 to 10: ')

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('guess is low')
    if guess > number:
        print('guess is high')
    if guess == number:
        break

if guess == number:
    print(f'You guessed the number in {number_of_guesses} tries')

else:
    print(f'You failed. The number was {number}')
