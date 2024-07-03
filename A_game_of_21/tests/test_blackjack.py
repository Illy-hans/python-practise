from lib.blackjack import BlackjackGame
from lib.cards import Draw_Cards
import pytest
from unittest.mock import patch

@pytest.fixture
def blackjack_game():
    return BlackjackGame()

@patch.object(Draw_Cards, 'hit_me')
def test_blackjack_game_play(mock_hit_me, blackjack_game, capsys):
    # card values added to the last two assertions when play_game is called
    mock_hit_me.side_effect = [("10", "hearts"), ("8", "spades")]
    
    # Test case where Sam wins with Blackjack
    blackjack_game.sam_hand = [("A", "hearts"), ("K", "diamonds")]
    blackjack_game.dealer_hand = [("7", "clubs"), ("10", "spades")]
    blackjack_game.play_game()
    assert "Sam wins with Blackjack!" in capsys.readouterr().out

    # Test case where Dealer wins with Blackjack
    blackjack_game.sam_hand = [("7", "hearts"), ("10", "diamonds")]
    blackjack_game.dealer_hand = [("A", "clubs"), ("K", "spades")]
    blackjack_game.play_game()
    assert "Dealer wins with Blackjack!" in capsys.readouterr().out

    # Test case where Sam busts
    blackjack_game.sam_hand = [("Q", "hearts"), ("6", "diamonds")]
    blackjack_game.dealer_hand = [("5", "spades"), ("6", "hearts")]
    # ("10", "hearts") added to Sam's hand
    blackjack_game.play_game()    
    assert "Sam busts! Dealer wins." in capsys.readouterr().out

    # Test case where Dealer busts
    blackjack_game.sam_hand = [("7", "hearts"), ("10", "diamonds")]
    blackjack_game.dealer_hand = [("K", "hearts"), ("5", "spades")]
    # ("8", "spades") added to Dealer's hand
    blackjack_game.play_game()
    assert "Dealer busts! Sam wins." in capsys.readouterr().out


@patch.object(Draw_Cards, 'hit_me')
def test_blackjack_game_play_total_score_comparison(mock_hit_me, blackjack_game, capsys):
    # card values added to the last two assertions when play_game is called
    mock_hit_me.side_effect = [("3", "hearts"), ("9", "spades")]

    # Test case where Sam wins with higher total
    blackjack_game.sam_hand = [("6", "hearts"), ("9", "diamonds")]
    # ("3", "hearts") added
    blackjack_game.dealer_hand = [("5", "spades"), ("7", "hearts")]
    # ("9", "spades") added
    blackjack_game.play_game()
    assert "Dealer wins with a total of" in capsys.readouterr().out


