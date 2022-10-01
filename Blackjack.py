import random

cards = ['A',2,3,4,5,6,7,8,9,10,'K','Q','V']
cards_figures = {'A': 11,
                 'K': 10,
                 'Q': 10,
                 'V': 10}

card1 = random.choice(cards)
card2 = random.choice(cards)
card3 = random.choice(cards)
card4 = random.choice(cards)

playerHand = []
sumHand = 0

def cardToValue(card):
    cardValueFigure = 0
    aceCardValue = 0
    cardValueNumber = 0
    if(card == 'A'):
        aceCardValue = int(input("You got an Ace ! You can choose between 1/11 (Type '1' or '11') :"))
    if(card in cards_figures and card != 'A'):
        cardValueFigure = cardValueFigure + cards_figures[card]
    if(isinstance(card,int)):
        cardValueNumber = cardValueNumber + card
    return [aceCardValue,cardValueNumber,cardValueFigure]

def dealPlayerCards(list):
    print(f"Your hand is : {list}" )
    hand = list
    allCards = []
    sumHand = 0
    for card in hand:
        allCards = cardToValue(card)
        sumHand = sumHand + allCards[0] + allCards[1] + allCards[2]
    while(sumHand <= 21):
        cardValue = 0
        drawCard = input("You want to draw another card ?: ")
        if(drawCard == 'y'):
            card = random.choice(cards)
            hand.append(card)
            cardValue = cardToValue(card)
            sumHand = sumHand + cardValue[0] + cardValue[1] + cardValue[2] 
    return [hand, sumHand]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


willPlay = input("Do you want to play a blackjack game ? (Type 'y' or 'n') : ")

if(willPlay == 'y'):
    houseHand = [card1, '?']
    playerHand = dealPlayerCards([card3, card4])
    if(playerHand[1] > 21):
        print(f"You lost : \nYour Hand : {playerHand[0]}")

else:
    print("OK, see you next time !")