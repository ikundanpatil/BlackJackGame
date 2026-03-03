import random
from Art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)

    return card

def score_calculate(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😊"
    elif u_score > c_score:
        return "You win 😊"
    else:
        return "You lose 😡"

def play_game():

    print(logo)

    user_card = []
    com_card = []
    com_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        com_card.append(deal_card())

    while not is_game_over:
        user_score = score_calculate(user_card)
        com_score = score_calculate(com_card)

        print(f"Your cards: {user_card},  current score: {user_score}")
        print(f"Computer's first card: {com_score}")

        if user_score == 0 or com_score == 0 or user_score > 21:
            is_game_over = True
        else:

            next = input("Type 'y' to get another card, type 'n' to pass: ")

            if next == 'y':
                user_card.append(deal_card())
            else:
                is_game_over = True

    while com_score != 0 and com_score < 17:
        com_card.append(deal_card())
        com_score = score_calculate(com_card)

    print(f"Your final hand: {user_card},  final score: {user_score}")
    print(f"Computer's final hand: {com_card},  final score: {com_score}")
    print(compare(user_score, com_score))

restart = True

while restart:
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if start == 'y':
        play_game()
    else:
        print("☠️  Go & Fuck Your Self! ☠️")
        break
