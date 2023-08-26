#blackjack
import art
import random

print(art.logo)

deck_of_cards = [11, 2, 3, 4, 5, 6, 7, 8 ,9 ,10, 10, 10, 10]

# Setting the initial players and dealers hands
player_hands = {}
dealers_hands = {}

# Getting 2 cards for each
p_cards = random.sample(deck_of_cards, 2)
d_cards = random.sample(deck_of_cards, 2)

# Adding cards to the hands
for card in p_cards:
    player_hands[len(player_hands) + 1] = card
    
for card in d_cards:
    dealers_hands[len(dealers_hands) + 1] = card
    
print(f"Player cards: {player_hands[1]} {player_hands[2]}")
print(f"Dealers cards: 'X' {dealers_hands[1]}")

# Calculating  total
p_total = player_hands[1] + player_hands[2]
d_total = dealers_hands[1] + dealers_hands[2]


# Hit function
def hit():
    p_hit_card = random.choice(deck_of_cards)
    return p_hit_card
    



hit_me = True

while hit_me:
    ask_for_hit = input("Hit or stay ? y/n\n")
    if ask_for_hit.lower() == "y":
        new_p_card = hit()
        player_hands[len(player_hands) + 1] = new_p_card  # Add the new card to player_hands
        t_length = len(player_hands) # Measuring the lenght
        player_cards = [str(player_hands[i]) for i in player_hands]
        player_cards_str = "Player cards: " + " ".join(player_cards)
        print(player_cards_str)
        p_total = sum(player_hands.values())  # Recalculate the total
        if d_total < 17: # AI logic
            new_d_card = hit()
            d_total += new_d_card
            print(f"Dealers cards: 'X' {dealers_hands[1]} {new_d_card}")
        if p_total > 22:
            print("BUSTED")
            hit_me = False
        if d_total > 22:
            print("BUSTED")
            hit_me = False
    else:
        if p_total > d_total and p_total < 22:
            print("Player win")
            hit_me = False
        else:
            print("Dealer win")
            hit_me = False

            