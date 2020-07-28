#! usr/bin/env python3
"""
python LoveLetter.py
A basic LoveLetter Game.

DONE:
Have the cards.
Have the cards be able to be shuffled
Have players draw cards.



TODO:
TODO - Move card to 'play area' after playing it!
# I think this will fix most of the issues I can see having with things. Though it WILL
require me to redo a lot of things, I think, to make it work.
Allow for more than 2 players
Bury the first card.
Have the card that is 'in play' be out of the hand.

Look Up:
How to do Tests with random?
If card is __ then do __ but how do you know you will get the card to do the tests on?

I want to add tests to all of these games.

TODO:
Add networking/socket things to have this work like a client server.
# Basically make it ACTUALLY work... yep.






"""
# Base imports
import random
import json
# Other imports

# My imports
from submodule import child
import LoveLetterServer as server




def main_game_loop(*args, **kwargs):
    # The main game.
    game = server.ObjectGame(*args, **kwargs)
    continue_the_loop = True
    using_exit = False
    # print(game.deck)
    while continue_the_loop:
        print("Player {name}'s turn".format(name=game.remaining_players[game.current_player].name))
        game.remaining_players[game.current_player].is_protected = False  # remove protected!
        game.deal_a_card(game.remaining_players[game.current_player])
        # game.deal_a_card(game.remaining_players[game.current_player])
        to_next_turn = False
        while not to_next_turn:
            game.draw_other_players()   # Draw the other players
            print()
            game.draw_the_card_hands()  # Draw the cards in your hand
            print()
            game.draw_the_discard()     # Draw the discard pile
            the_input = input(game.remaining_players[game.current_player].name +
                              " Please type the name or number of the card you \n"
                              "want to play or type Exit to end the program.")

            if the_input.lower() == "exit":
                continue_the_loop = False
                to_next_turn = True
                using_exit = True
                break
            # has_countess = False
            # discard_princess = False
            # CHECK FOR Countess!!!
            if "Countess" in game.remaining_players[game.current_player].cards \
                    and ("Prince" in game.remaining_players[game.current_player].cards
                         or "King" in game.remaining_players[game.current_player].cards):
                for card in game.remaining_players[game.current_player].cards:
                    if the_input.lower() == card.name.lower() == "countess":
                        print(game.remaining_players[game.current_player].name + " plays " + card.name + ".")
                        game.discard_a_card(game.remaining_players[game.current_player], card)
                        for action in card.actions:
                            turn = game.card_actions(action)
                            if turn == "Finished":
                                to_next_turn = True
                                break
                                # This break 'should' get me out of having the issue
                                # with 2 cards that are the same name.
                    else:
                        print("You must play the Countess since you have")
                        print("the Prince or King in your hand.")

            # Non Countess Path.
            else:
                for count, card in enumerate(game.remaining_players[game.current_player].cards):
                    if the_input.lower() == card.name.lower() or the_input == str(count):
                        print(game.remaining_players[game.current_player].name + " plays " + card.name + ".")
                        game.remaining_players[game.current_player].discarded_amount += card.number
                        game.discard_a_card(game.remaining_players[game.current_player], card)
                        for action in card.actions:
                            turn = game.card_actions(action)
                            if turn == "Finished":
                                to_next_turn = True
                                break
        round_winner = check_for_round_end(game.remaining_players, game.current_deck)
        game.next_player()
        if round_winner != "no":
            game.draw_round_end(round_winner)
            game.setup_round(round_winner)
        check_for_game_end(game.players)
    end_game(using_exit)


def process_the_input():
    the_input = input("Where would you like to go?")
    print(the_input)


def check_for_round_end(current_players, current_deck) -> str:
    # checks to see if only one player is left, if so they are the victor.
    if len(current_players) == 1:
        for player in current_players:
            player.score += 1
            return player
    # checks to see if there are any more cards left to be drawn.
    if len(current_deck) == 0:
        # If no more cards and more than 1 player player with the highest card value wins.
        high_card = 0
        high_player = ""
        for player in current_players:
            for card in player.cards:
                if card.number > high_card:
                    high_card = card.number
                    high_player = player
        # WHAT HAPPENS IF THEY ARE TIED CARDS?
        # I DON"T REMEMBER WHAT HAPPENS THERE...
        return high_player

    return "no"


def check_for_game_end(all_players, winning_score=3):
    # checks if someone has won the game. enough wins
    for player in all_players:
        if player.score > winning_score:
            return player
    pass


def end_game(if_exit):
    end = False
    if if_exit:
        end = True
    while not end:
        the_input = input("Would you like to play again Y/N?")
        if the_input.lower() == "y" or the_input.lower() == "yes" or the_input.lower() == "(y)es":
            main_game_loop()
            end = True  # This will make it so there are not multiple of these afterwards.
        elif the_input.lower() == "n" or the_input.lower() == "no" or the_input.lower() == "(n)o":
            end = True
        elif the_input.lower() == "o" or the_input.lower() == "or":
            print("Seriously...")
        else:
            print("Please enter (Y)es or (N)o")



if __name__ == "__main__":
    main_game_loop(number_of_players=3, player_names=["Chris", "Dan"])
