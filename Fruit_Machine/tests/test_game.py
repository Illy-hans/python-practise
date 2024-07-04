from Fruit_Machine.lib.game import Game
import pytest

@pytest.fixture
def game():
    return Game()

@pytest.fixture
def mock_results():
    return [
        ["white", "black", "green", "yellow"],  
        ["green", "green", "green", "green"],        
        ["yellow", "yellow", "black", "green"],     
        ["white", "black", "green", "white"]      
    ]


# tests if the bet has affected the player, and machine wallet
def test_add_bet(game):
    initial_player_wallet = game.player_wallet
    initial_machine_wallet = game.machine_wallet
    bet_amount = 5.00

    game.add_bet(bet_amount)

    assert game.bet == bet_amount
    assert game.player_wallet == initial_player_wallet - bet_amount
    assert game.machine_wallet == initial_machine_wallet + bet_amount


# tests win condition when all colours are unique
def test_check_win_all_unique(game, mock_results, mocker):
    mocker.patch.object(game.colours, 'play_game', return_value=mock_results[0])
    game.add_bet(10.00)
    initial_machine_wallet = game.machine_wallet

    result = game.check_win()

    assert "Congratulations! You have won £54.25" in result
    assert game.machine_wallet == initial_machine_wallet - 54.25


# tests win condition if all colours are the same
def test_check_win_all_same(game, mock_results, mocker):
    mocker.patch.object(game.colours, 'play_game', return_value=mock_results[1])
    game.add_bet(10.00)

    result = game.check_win()

    assert f"Congratulations! You have won £{game.machine_wallet}" in result
    assert game.machine_wallet == 0


# tests two consecutive colours win condition 
def test_check_win_two_consecutive(game, mock_results, mocker):
    mocker.patch.object(game.colours, 'play_game', return_value=mock_results[2])
    bet_amount = 10.00
    game.add_bet(bet_amount)
    initial_machine_wallet = game.machine_wallet

    result = game.check_win()

    assert f"Congratulations! Two or more consecutive matches gives you £{bet_amount * 5}!" in result
    assert game.machine_wallet == initial_machine_wallet - (bet_amount * 5)
    assert game.bet == 0


# tests no win game
def test_check_no_win(game, mock_results, mocker):
    mocker.patch.object(game.colours, 'play_game', return_value=mock_results[3])
    game.add_bet(10.00)
    initial_machine_wallet = game.machine_wallet

    result = game.check_win()

    assert "Better luck next time!" in result
    assert game.machine_wallet == initial_machine_wallet

