from Fruit_Machine.lib.slots import Slot_Colours

# Initialise class
sc = Slot_Colours()

def test_slot_colours_initialization():
    assert sc.colours == ["black", "white", "green", "yellow"]

def test_play_game():
    result = sc.play_game()
    assert len(result) == 4
    for colour in result:
        assert colour in sc.colours

def test_no_two_games_alike():
    result1 = sc.play_game()
    result2 = sc.play_game()
    assert result1 != result2