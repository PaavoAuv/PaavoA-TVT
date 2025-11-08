

import random
random.seed(1234)


ROCK = """    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER = """     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

SCISSORS = """    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


CHOICES = {
    1: ("rock", ROCK),
    2: ("paper", PAPER),
    3: ("scissors", SCISSORS)
}


def display_choice(player_name: str, choice_num: int) -> None:
    """Print player's name, choice and ASCII art with decoration."""
    choice_name, art = CHOICES[choice_num]
    print("#########################")
    print(f"{player_name} chose {choice_name}.\n")
    print(art)
    print("#########################")
    return None


def main() -> None:
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")
    player_name = input("Insert player name: ")
    print(f"Welcome {player_name}!")
    print("Your opponent is RPS-3PO.")
    print("Game starts...\n")

   
    player_wins = 0
    player_losses = 0
    draws = 0

   
    while True:
        print("Options:")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")
        print("0 - Quit game")
        choice = input("Your choice: ").strip()

        if not choice.isdigit():
            continue
        choice = int(choice)

        if choice == 0:
            break
        elif choice not in (1, 2, 3):
            continue

        bot_choice = random.randint(1, 3)

        print("Rock! Paper! Scissors! Shoot!\n")

        
        display_choice(player_name, choice)
        display_choice("RPS-3PO", bot_choice)

        player_name_lower = CHOICES[choice][0]
        bot_name_lower = CHOICES[bot_choice][0]

      
        if choice == bot_choice:
            print(f"Draw! Both players chose {player_name_lower}.")
            draws += 1
        elif (choice == 1 and bot_choice == 3) or \
             (choice == 2 and bot_choice == 1) or \
             (choice == 3 and bot_choice == 2):
            print(f"{player_name} {player_name_lower} beats RPS-3PO {bot_name_lower}.")
            player_wins += 1
        else:
            print(f"RPS-3PO {bot_name_lower} beats {player_name} {player_name_lower}.")
            player_losses += 1
        print()

  
    print("\nResults:")
    print(f"{player_name} - wins ({player_wins}), losses ({player_losses}), draws ({draws})")
    print(f"RPS-3PO - wins ({player_losses}), losses ({player_wins}), draws ({draws})")
    print("\nProgram ending.")



main()
