import random 

class Slot_Colours(): 

    def __init__(self) -> None:
        self.colours: list[str] = ["black", "white", "green", "yellow"]

    def slot_colour(self) -> str:
        slot_space: str = random.choice(self.colours)
        return slot_space

    def play_game(self) -> list[str]:
        result: list[str] = [self.slot_colour() for i in range(4)]
        return result





