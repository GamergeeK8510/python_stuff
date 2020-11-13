import random2

questions = [
    "\nROCK     (1)"
    "\nPAPER    (2)"
    "\nSCISSORS (3)\n"
    "\nPlease enter your choice:\n",
    "\nComputer chose "
]


def play(player, cpu):
    if int(player) == 1 and cpu == 3:
        print("\nYou Win!\n")
    elif int(player) == 3 and cpu == 1:
        print("\nYou Lose! Try again!\n")
    elif int(player) == cpu:
        print("\nIt was a tie! Go again!\n")
    elif int(player) > cpu:
        print("\nYou Win!\n")
    elif int(player) < cpu:
        print("\nYou Lose! Try again!\n")


while True:
    player_choice = input(questions[0])
    if player_choice == "stop":
        break
    elif player_choice in ["1", "2", "3"]:
        computer_choice = random2.randint(1, 3)
        if computer_choice == 1:
            print(questions[1] + "Rock.\n")
        elif computer_choice == 2:
            print(questions[1] + "Paper.\n")
        elif computer_choice == 3:
            print(questions[1] + "Scissors.\n")
        play(player_choice, computer_choice)
    else:
        print("\nPlease enter '1', '2', or '3'\n")
