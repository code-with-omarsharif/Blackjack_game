import random
from art import logo
import time


# dealing cards and appending from the cards list with random package
def deal_card():
    Cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(Cards)
    return card


# comparing score for the find winner


def comparing(user_scores, computer_scores):
    if user_scores == computer_scores:
        return "Draw🤔"
    elif user_scores == 0:
        return "You win with Blackjack 😋"
    elif computer_scores == 0:
        return "You Lose. Opponent has Blackjack😣"
    elif user_scores > 21:
        return "You went over, you lose 😪"
    elif computer_scores > 21:
        return "You win. Opponent went over😅🤘💪🕺"
    elif user_scores > computer_scores:
        return "You win😎🕺🏿💃🏿💪🏿"
    else:
        return "You Lose"


# playing the game after asking the user


def playGame():
    global computer_score, user_score
    print(logo)
    time.sleep(1)

    # Calculating cards value

    def calculate_card(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    end_of_game = False
    # call the deal_card function and appending the random value in a list
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # repeating the calculation and adding the value from what user want

    while not end_of_game:

        user_score = calculate_card(user_cards)
        computer_score = calculate_card(computer_cards)
        print(f"Your cards is {user_cards}. Your current Score {user_score}")
        print(f"Computer first card is {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            end_of_game = True
        else:
            deal_with_user = input("Do you want to get another card? type 'add' or pass 'pass': ").lower()
            if deal_with_user == 'add':
                user_cards.append(deal_card())
            else:
                end_of_game = True
    # adding the computer card for the fighting with user card
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_card(computer_cards)

    # showing the final output
    print(f"Your Final hand {user_cards} and final Score {user_score}")
    print(f"Computer Final hand {computer_cards} and final Score {computer_score}")
    # Calling the compare function and showing the winner
    print(comparing(user_score, computer_score))


# playing the game or not asking user


while input("Do you want to play Blackjack game 'yes' or 'no': ").lower() == 'yes':
    playGame()
