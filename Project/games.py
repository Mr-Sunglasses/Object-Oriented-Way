from answers import magic_eight_ball_answers
import random

def magic_eight_ball_game():

    while True:

        user_question = input("Ask me a Question ππ» : ")
        user_answer = random.choice(magic_eight_ball_answers)
        print(f"ππ» : {user_answer}")
        next_question = input("Any more Questions Y/N π«Άπ» : ")

        if next_question.lower() == 'y':
            continue

        elif next_question.lower() == 'n':
            print("Bye Bye π₯²")
            break
        else:
            print("I Don't UnderStand Your Input π°")
            break


def guess_the_number_game():

        while True:

            random_number = random.randint(1,10)
            max_attempts = 0

            while max_attempts <=3 :

                print("Welcome to Guess me π , ")
                guess = int(input("Please Enter the Number which you Guess π: "))

                if random_number == guess:

                    print("You Won π !!!!")
                    break

                elif max_attempts != 3:
                    print("OOPS π¬ Wrong π Guess")
                    max_attempts+=1

                else:
                    print(f"You Loose ππ» ......The Number is {guess}")
                    break

            play_again = input("Does You Want to Play Again Y/N π : ")

            if play_again.lower() == 'y':
                continue

            elif play_again.lower() == 'n':
                print("Bye Bye π")
                break
            else:
                print("I Don't UnderStand Your Input π°")
                break
