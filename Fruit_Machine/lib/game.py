from Fruit_Machine.lib.slots import Slot_Colours


class Game():

    def __init__(self) -> None:
        self.colours = Slot_Colours()
        self.machine_wallet: float = 98.50    
        self.player_wallet: float = 20.00
        self.bet = 0
    
    # Function to manage both wallets and the bet 
    def add_bet(self, bet: float) -> None:
        self.bet += bet
        self.machine_wallet += bet
        self.player_wallet -= bet
    
    # Function to compare slot colours, if any two consective ones are the same True is returned
    def compare_slot_colours(self, result: list[str]) -> bool:

        for i in range(len(result) - 1):
            if result[i] == result[i + 1]:  
                return True

    def check_win(self) -> str:
        result: list[str] = self.colours.play_game()

        # if all 4 colours are unique, half the machine wallet is paid out.
        if len(result) == len(set(result)):
            half_win: float = self.machine_wallet * 0.5
            self.machine_wallet -= half_win
            return f"Congratulations! You have won £{half_win}"
        
        # if all colours are uniform the jackpot is paid. 
        elif len(set(result)) == 1:
            self.machine_wallet -= self.machine_wallet
            return f"Congratulations! You have won £{self.machine_wallet}"
        
        # if two or more slot colours are the same 5x the bet is paid out.
        elif self.compare_slot_colours(result):
            prize: float = self.bet * 5
            self.machine_wallet -= prize
            self.bet -= self.bet
            return f"Congratulations! Two or more consecutive matches gives you £{prize}!"
        
        else:
            return f"Better luck next time!"
