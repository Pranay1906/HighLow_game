import random
import art
from game_data import data
# from replit import clear


def select():
    return random.choice(data)


def display():
    print(f"{select()['name']}, {select()['description']}, {select()['country']}")
    return select()['follower_count']


def main(user_input, choose1, choose2, score):
    if user_input == "A" and choose1 > choose2:
        score += 1
        print(f"You are right!!. Current score is {score}")
        game_start(score)
    elif user_input == "B" and choose2 > choose1:
        score += 1
        print(f"You are right!!. Current score is {score}")
        game_start(score)
    elif choose1 == choose2:
        print("Both are equal")
    else:
        print(f"Sorry that's wrong. Final score is {score}")


def game_start(score):
    # clear()
    print(art.logo)
    print(f"Your score is {score}")
    print('Compare A : ',end='')
    choose1 = display()
    print(art.vs)
    print('Compare B : ', end='')
    choose2 = display()
    user_input = input('Who has more followers : Type "A" or "B" :')
    main(user_input, choose1, choose2, score)


game_start(score=0)
