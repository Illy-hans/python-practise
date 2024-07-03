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
    

# cards = Cards()
# print(cards)


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


# game = Draw_Cards()
# print("First hand:", game.first_hand())
# print("Hit me:", game.hit_me())
# game.print_remaining_deck()


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


# game = Draw_Cards()
# first_hand = game.first_hand()
# print("First hand:", first_hand)
# print("Hit me:", game.hit_me())
# game.print_remaining_deck()

# game_instance = Game()
# hand_value = game_instance.calculate_hand_value(first_hand)
# print("Hand total value:", hand_value)


class BlackjackGame:
    def __init__(self) -> None:
        self.game = Game()
        self.sam_hand = self.game.cards.first_hand()
        self.dealer_hand = self.game.cards.first_hand()

    def check_blackjack(self, hand: list[tuple[str, str]]) -> bool:
        return self.game.calculate_hand_value(hand) == 21
    
    def play_game(self) -> None:
        sam_total = self.game.calculate_hand_value(self.sam_hand)
        print("first hand sam:", self.sam_hand, sam_total)

        dealer_total = self.game.calculate_hand_value(self.dealer_hand)
        print("first hand dealer:", self.dealer_hand, dealer_total)

        if self.check_blackjack(self.sam_hand):
            print("Sam wins with Blackjack!")
            return
        elif self.check_blackjack(self.dealer_hand):
            print("Dealer wins with Blackjack!")
            return
        
        # Sam's turn
        while sam_total < 17:
            self.sam_hand.append(self.game.cards.hit_me())
            sam_total = self.game.calculate_hand_value(self.sam_hand)
            print("2nd Sam:", sam_total, self.sam_hand)
            if sam_total > 21:
                print("Sam busts! Dealer wins.")
                return

        # Dealer's turn
        while dealer_total <= sam_total and dealer_total <= 21:
            self.dealer_hand.append(self.game.cards.hit_me())
            print("2nd:", self.dealer_hand, dealer_total)
            dealer_total = self.game.calculate_hand_value(self.dealer_hand)
            if dealer_total > 21:
                print("Dealer busts! Sam wins.")
                return

        # Determine winner
        if dealer_total > sam_total:
            print("Dealer wins with a total of", dealer_total)
        else:
            print("Sam wins with a total of", sam_total)


    # def print_hands(self) -> None:
    #     print("Sam's hand:", self.sam_hand, "Total:", self.game.calculate_hand_value(self.sam_hand))
    #     print("Dealer's hand:", self.dealer_hand, "Total:", self.game.calculate_hand_value(self.dealer_hand))


blackjack_game = BlackjackGame()
print(blackjack_game.play_game())
# blackjack_game.print_hands()