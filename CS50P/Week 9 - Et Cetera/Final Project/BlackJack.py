import inquirer
import random
import sys

# questions = [
#     inquirer.List('option',
#                   message="Select an option",
#                   choices=['Option 1', 'Option 2', 'Option 3'],
#                   ),
# ]

# answers = inquirer.prompt(questions)
# print(f"You selected: {answers['option']}")

menu_question = [
  inquirer.List('option',
                message = "What would you like to do?",
                choices=["New Game", "Quit"]
               ),
]

moves = [
  inquirer.List('option',
                message = "Do you want to Hit or Stay?",
                choices=["Hit", "Stay"]
               ),
]

suits = ["♠", "♥", "♦", "♣"]
ranks = [2, 3, 4, 5, 6, 7, 8, 9, "T", "J", "Q", "K", "A"]

cards_played = []
player_hand = []
dealer_hand = []

def main():
  play_game()

def play_game():
  global player_hand
  global dealer_hand
  playing = True
  # name = input("What's you name? ")
  print("Welcome to the game ")
  menu_select = inquirer.prompt(menu_question)

  # If player selects quit, exit the game
  if menu_select["option"] == "Quit":
    playing = False
    sys.exit("Thanks for playing")

  while (playing):
    print("Start")
    # Deal the first set of cards to the dealer and the player 
    player_hand.append(deal_card())
    player_hand.append(deal_card())
    dealer_hand.append(deal_card())
    dealer_hand.append(deal_card())

    displayHands(player_hand, dealer_hand)
    player_move = inquirer.prompt(moves)
    # If player chooses to hit, deal him another card
    print(player_move["option"])
    if player_move["option"] == "Hit":
      print("hitting")
      player_hand.append(deal_card())
      displayHands(player_hand, dealer_hand)
    else:
      # The False, will tell the function that we want to reveal the dealers full hand
      displayHands(player_hand, dealer_hand, False)
      playing = False
      sys.exit("GAME OVER")
    player_move = inquirer.prompt(moves)



# Deals a card from the global decks.
# TODO keep track of what cards have been used
def deal_card():
    global suits
    global ranks
    suit = random.randint(0, 3)
    rank = random.randint(0, 12)
    return [suits[suit], ranks[rank]]

def shuffle_deck():
  global cards_played
  cards_played = []

def displayHands(player_deck: list, dealer_deck: list, hide_dealer_hand: bool = True):

  # Checks to see if both cards should be displayed
  print("DEALER")
  if hide_dealer_hand == True:
    print(f" ---\n| {dealer_deck[0][0]} |\n| {dealer_deck[0][1]} |\n ---")
    # Print a card facing down
    print(f" ---\n| X |\n| X |\n ---")
  else:
    for card in dealer_deck:
      print(f" ---\n| {card[0]} |\n| {card[1]} |\n ---")

  print("PLAYER")
  for card in player_deck:
    print(f" ---\n| {card[0]} |\n| {card[1]} |\n ---")


if __name__ == "__main__":
  main()