import random
from typing import Union

class Cards():  
    def __init__(self) -> None:
        suits: list[str] = ["hearts", "diamonds", "clubs", "spades"]
        ranks: list[str] = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        self.deck: list[tuple[str, str]] = [(rank, suit) for suit in suits for rank in ranks]
        # for suit in suits: 
        #     for rank in ranks:
        #         self.cards.append((rank, suit))


    def draw_card(self) -> tuple[str,str]:
        random_card: tuple[str, str] = random.choice(self.deck)
        self.deck.remove(random_card)
        return random_card  

    def remaining_cards(self) -> list[tuple[str, str]]:
        return self.deck
    

class Draw_Cards(): 
    def __init__(self) -> None:
        self.deck = Cards()

    def first_hand(self) -> list[tuple[str,str]]:
        hand: list[tuple[str,str]] = [self.deck.draw_card(), self.deck.draw_card()]
        return hand
    
    def hit_me(self) -> tuple[str,str]:
        another_card: tuple[str,str] = self.deck.draw_card()
        return another_card
    
    def print_remaining_deck(self) -> None:
        remaining_deck: list[tuple[str,str]]= self.deck.remaining_cards()
        print("Remaining cards in the deck:")
        for card in remaining_deck:
            print(card)


class Game():
    def __init__(self) -> None:
        self.cards = Draw_Cards()

    # union allows cards to accept two parameters
    def calculate_hand_value(self, cards: Union[list[tuple[str, str]], tuple[str, str]]) -> int:
        if isinstance(cards, tuple):
            cards = [cards]

        aces = 0
        hand_total = 0

        for card in cards:
            rank, _ = card
            if rank in ["J", "Q", "K"]:
                hand_total += 10
            elif rank == "A":
                hand_total += 11
                aces += 1
            else:
                hand_total += int(rank)

        # Adjust for Aces if total exceeds 21
        while hand_total > 21 and aces > 0:
            hand_total -= 10
            aces -= 1

        return hand_total
