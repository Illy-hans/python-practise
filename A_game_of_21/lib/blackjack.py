from lib.cards import Game

class BlackjackGame:
    def __init__(self) -> None:
        self.game = Game()
        self.sam_hand: list[tuple[str,str]] = self.game.cards.first_hand()
        self.dealer_hand: list[tuple[str,str]] = self.game.cards.first_hand()

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
