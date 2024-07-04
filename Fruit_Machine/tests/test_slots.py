from Fruit_Machine.lib.slots import Slot_Colours
import pytest

@pytest.fixture
def colours():
    return Slot_Colours()

def test_slot_colours_initialization(colours):
    assert colours.colours == ["black", "white", "green", "yellow"]

def test_play_game(colours):
    result = colours.play_game()
    assert len(result) == 4
    for colour in result:
        assert colour in colours.colours

def test_no_two_games_alike(colours):
    result1 = colours.play_game()
    result2 = colours.play_game()
    assert result1 != result2