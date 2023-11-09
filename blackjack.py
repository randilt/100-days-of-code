cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random

def deal_card(card):
  return random.choice(card)

user_cards = []
computer_cards = []

user_cards.append(deal_card(cards))
user_cards.append(deal_card(cards))

computer_cards.append(deal_card(cards))
computer_cards.append(deal_card(cards))

def calculate_score(deck):
  if(sum(deck) >= 21 and 11 in deck):
    deck.remove(11)
    deck.append(1)
  if(len(user_cards) == 2 and sum(deck) >= 21):
    return 0
  return sum(deck)


stop_game = False



print(user_cards)
print(f"Your score is {calculate_score(user_cards)}")
print(f"Computer's first card is {computer_cards[0]}")

stop_adding = False

while(stop_adding == False):
  add_another_hand = input("Type y to get another card or type n to pass: ")

  
  if calculate_score(user_cards) == 0 or calculate_score(computer_cards) == 0:
    stop_adding = True
    print(f"Game over! blackjack Your score: {calculate_score(user_cards)} computer score: {calculate_score(computer_cards)}")
  elif calculate_score(user_cards) >= 21:
    stop_adding = True
    print(f"You just exceeded 21 score and you lose. Your score is {calculate_score(user_cards)}")
  
  
  elif(add_another_hand == "y" and calculate_score(user_cards) < 21):
    computer_cards.append(random.choice(cards))
    user_cards.append(random.choice(cards))
    print(f"Your current deck is {user_cards} and your score is {calculate_score(user_cards)}")
  elif(add_another_hand == "n"):
    stop_adding = True
    if calculate_score(user_cards) >= 21 and calculate_score(user_cards) > calculate_score(computer_cards):
      print(f"You lose :( Your final score is {calculate_score(user_cards)}")
    elif calculate_score(user_cards) < 21 and calculate_score(user_cards) > calculate_score(computer_cards):
      print(f"You win!\n Your score: {calculate_score(user_cards)}\n Computer Score: {calculate_score(computer_cards)}")
  else:
    print("invalid input try again")
  



