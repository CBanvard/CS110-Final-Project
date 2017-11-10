import deuces

def main():
	print("### Testing card model ###")
	test_Card = card.Card();
	other_Card = other.Other();

	print("=== Card Type Test ===")
	cardDeck = [one, two, three, four, five, six, seven, eight, nine, ten, jack, queen, king, ace] 
	cardDeck = cardDeck * 4
	assert cardDeck.count(two) == 4

	print("=== Input Test ===")
	assert deuces.get_suit_int(test_Card) > deuces.get_suit_int(other_Card):

	
