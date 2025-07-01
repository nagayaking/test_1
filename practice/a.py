import random

class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["ハート", "ダイヤ", "スペード", "クラブ"]:
            for number in range(1, 14):
                card = Card(suit,number)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards

    def draw_card(self):
        return self.cards.pop(0)


deck = Deck()
deck.shuffle()
for i in range(5):
    a = Deck.draw_card(deck)
    print(f"{a.suit}{a.number}")