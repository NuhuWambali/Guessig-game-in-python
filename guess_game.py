#this program is for guessing the numbers
import random
print("""
    ***************************************
    *                                     *
    *      WELCOME TO NUHU PROGRAMING     *
    *                                     *
    ***************************************
THIS IS A SIMPLE GUESSING GAME 
RULES:
1.PLAYER CAN GUESS A NUMBER IN 6 TRIES ONLY
2.YOU ARE REQUIRED TO ENTER THE NUMBER BETWEEN 1 AND 20
3.YOU BEAT MY ROBOT IF YOU GUESS A CORRECT NUMBER OTHERWISE A ROBOT BEATS YOU

""")

#GOODBYE MESSAGE
def goodbye():
    print("""
    ----------------------------------
    - THANK YOU FOR USING OUR SYSTEM - 
    - contact developer via whatsapp -
    -        +255688349680           -
    ----------------------------------
    """)


secretNumber = random.randint(1, 20)
print('robot is thinking of a number between 1 to 20')
#ask a player to guess the number
for guessTaken in range(1, 7):
    print('take a guess')
    guess = int(input())
    if guess < secretNumber:
        print('your guess is too low')
    elif guess > secretNumber:
        print('your guess is too high')
    else:
        break#this condition is for correct guess
if guess == secretNumber:
    print('good job! you guessed robot number in ' + str(guessTaken) + ' guess' + 'guess number is ' + str(guess))
    goodbye()
else:
    print('nope! the number robot was thinking of was ' + str(secretNumber))
    goodbye()
