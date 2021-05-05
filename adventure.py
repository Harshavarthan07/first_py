#HI, I'M HARSHA
#SIMPLE IF/ELSE ADVENTURE PROGRAM



print('Welcome to adventure game!!')
name = str(input('What is your character name?: '))
age = int(input('What is your age?: '))
health = 10
if age >= 18:
    print('You are old enough!😄')
    wants_to_play = input('Do you want to play? :').lower()

    if wants_to_play.lower() == 'yes':
        print(f'You are starting with {health} health')
        print('Lets play!')
        left_or_right = input('First choice... Left or Right (left/right)?:')
        if left_or_right.lower() == 'left':
            ans = input('Nice, you follow the path and reach a lake , it looks like the lake is filled with aligtors...Do you want to swim across or go around the broken bridge(across/around)?:')
            if ans.lower() == 'around':
                print('You gone around the bridge but fell from the bridge and lost 5 health,\n these wood logs looked like aligators......')
                health -= 5
            elif ans.lower() == 'across':
                print('You went across the lake by swimming and reach the other side... ')
            ans = input("You notice a house and a river, which will you go to (river/house)?: ")
            if ans.lower() == 'house':
                print("You go to the house and greeted by the owner... he doesn't like you and he beat you with his stick and you lose 5 health")
                health -= 5
                if health <= 0:
                    print('You lose....')
                else:
                    print('You survived.... You win')
            else:
                print('')
        else:
            print('You fell in the river and lost')
    else:
        print('see ya..')
else:
    print('Sorry kid this game is not for you.... ☹') 

# new branch for git