import pytest
from lib.cards import Game 

# integration tests for functionality up until and including the Game class 

@pytest.fixture
def game():
    return Game()

def test_game_flow(game):
    # Test initial deck size
    assert len(game.cards.deck.deck) == 52

    # Draw initial hands
    sam_hand = game.cards.first_hand()
    dealer_hand = game.cards.first_hand()

    # Check that 4 cards have been drawn
    assert len(game.cards.deck.deck) == 48

    # Verify hand sizes
    assert len(sam_hand) == 2
    assert len(dealer_hand) == 2

    # Calculate and check initial hand values
    sam_value = game.calculate_hand_value(sam_hand)
    dealer_value = game.calculate_hand_value(dealer_hand)
    assert sam_value > 0
    assert dealer_value > 0

    # Test hitting (drawing another card)
    hit_card = game.cards.hit_me()
    assert isinstance(hit_card, tuple)
    assert len(hit_card) == 2

    # Check that another card has been drawn
    assert len(game.cards.deck.deck) == 47

    # Add the hit card to Sam's hand and recalculate
    sam_hand.append(hit_card)
    new_sam_value = game.calculate_hand_value(sam_hand)
    assert new_sam_value > sam_value

    # Test Ace handling
    ace_hand = [('A', 'hearts'), ('K', 'spades')]
    ace_value = game.calculate_hand_value(ace_hand)
    assert ace_value == 21

    # Test busting
    bust_hand = [('K', 'hearts'), ('Q', 'spades'), ('J', 'diamonds')]
    bust_value = game.calculate_hand_value(bust_hand)
    assert bust_value == 30

def test_deck_uniqueness(game):
    # Draw all cards and ensure they're unique
    drawn_cards = []
    for _ in range(52):
        card = game.cards.deck.draw_card()
        assert card not in drawn_cards
        drawn_cards.append(card)

    # Ensure deck is empty
    assert len(game.cards.deck.deck) == 0


def test_card_representations(game):
    all_cards = game.cards.deck.deck
    
    expected_suits = {"hearts", "diamonds", "clubs", "spades"}
    actual_suits = {card[1] for card in all_cards}
    assert actual_suits == expected_suits

    # Check ranks
    expected_ranks = set("23456789") | {"10", "J", "Q", "K", "A"}
    actual_ranks = {card[0] for card in all_cards}
    assert actual_ranks == expected_ranks
