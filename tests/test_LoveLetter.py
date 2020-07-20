"""
Lots of tests! Hopefully...

"""
import LoveLetter


def test_amount_of_cards():
    deck = LoveLetter.make_the_deck()
    current_counts = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    desired_counts = {0:16, 1:5, 2:2, 3:2, 4:2, 5:2, 6:1, 7:1, 8:1}
    for card in deck:
        current_counts[card.number] += 1
        current_counts[0] += 1

    for i in range(9):
        if current_counts[i] != desired_counts[i]:
            assert False
    assert True



def test_again():
    pass
