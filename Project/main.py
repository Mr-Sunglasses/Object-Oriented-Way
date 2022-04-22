from games import magic_eight_ball_game,guess_the_number_game

print("Press 1 For Magic Eight Balls Game")
print("Press 2 For Number Gussing Game")

choice = int(input("Please Enter Your Choice 👍 : "))

if choice == 1:
    magic_eight_ball_game()
elif choice ==2:
    guess_the_number_game()
else:
    print("I Don't UnderStand Your Input 😰")