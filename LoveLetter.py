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
import random
import json
from submodule import child

def make_the_deck():
    new_deck = []
    with open('data.json') as json_file:
        data = json.load(json_file)
        for p in data['cards']:
            for i in range(p["Count"]):
                new_deck.append(ObjectCard(p["Number"], p["Name"], p["Description"], p["Actions"]))
    return new_deck


def main_game_loop():
    # The main game.
    game = ObjectGame(number_of_players=3)
    continue_the_loop = True
    using_exit = False
    print(game.deck)
    while continue_the_loop:
        game.remaining_players[game.current_player].is_protected = False   # remove protected!
        game.deal_a_card(game.remaining_players[game.current_player])
        # game.deal_a_card(game.remaining_players[game.current_player])
        game.draw_the_card_hands()  # draw_the_game
        game.draw_the_discard()
        to_next_turn = False
        while not to_next_turn:
            the_input = input(game.players[game.current_player].name +
                              " Please type the name of the card you \n"
                              "want to play or type Exit to end the program.")

            if the_input.lower() == "exit":
                continue_the_loop = False
                to_next_turn = True
                using_exit = True
            has_countess = False
            discard_princess = False
            # CHECK FOR Countess!!!
            if "Countess" in game.remaining_players[game.current_player].cards \
                    and ("Prince" in game.remaining_players[game.current_player].cards
                         or "King" in game.remaining_players[game.current_player].cards):
                for card in game.remaining_players[game.current_player].cards:
                    if the_input.lower() == card.name.lower() == "countess":
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
                    if the_input.lower() == card.name.lower() or the_input == count:
                        print(game.remaining_players[game.current_player].name + " plays " + card.name + ".")
                        game.discard_a_card(game.remaining_players[game.current_player], card)
                        for action in card.actions:
                            turn = game.card_actions(action)
                            if turn == "Finished":
                                to_next_turn = True
                                break
        game.next_player()
    end_game(using_exit)


def process_the_input():
    the_input = input("Where would you like to go?")
    print(the_input)


def check_for_game_end(players):
    # checks if someone has won the game.
    # checks to see how many players are left in the game.
    # checks to see if there are any more cards left to be drawn.
    # If no more cards and more than 1 player player with the highest card value wins.
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


class ObjectPlayer:
    def __init__(self, name, ai=None):
        self.name = name
        self.cards = []
        self.ai = ai
        self.is_protected = False
        if self.ai:
            self.ai.owner = self

    """
    def __str__(self) -> str:
        return f"{self.name}"

    """
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, ai={self.ai!r})"


class ObjectGame:
    def __init__(self, number_of_players=2):
        self.number_of_players = number_of_players
        self.players = [ObjectPlayer("Player " + str(x)) for x in range(self.number_of_players)]
        self.deck = make_the_deck()

        # The following are used for the round and restored between rounds.
        self.current_deck = self.deck.copy()
        self.remaining_players = self.players.copy()
        self.current_player = 0
        self.current_card = None  # The current card that is being resolved.
        self.discarded_cards = []
        self.hidden_cards = []
        self.list_of_cards = ["guard", "priest", "baron", "handmaid", "prince", "king", "countess", "princess"]

        # Display all cards in the deck
        # for card in self.current_deck:
        #     print(card.name)
        # Shuffle the deck
        self.current_deck = self.shuffle_the_deck()
        # Deal a card to each player
        for player in self.players:
            self.deal_a_card(player)
        # First player starts their turn.
        # Current player draws a card and plays a card.
        # Next players turn.
        # Used for the actions:
        self.selected_player = None
        self.selected_card = None

    def player_removed_from_round(self, player_to_remove):
        # checks to see if the current player is removed.
        # If so removes current player and adjusts the current player location.
        if player_to_remove == self.remaining_players[self.current_player]:
            self.current_player = (self.current_player - 1) % len(self.remaining_players)
            self.remaining_players.remove(player_to_remove)
        else:
            # finds out who the current first player is.
            first_player = self.remaining_players[self.current_player]
            # removes the player from the round.
            self.remaining_players.remove(player_to_remove)
            # figures out who the 'current' player would then be.
            for x in range(len(self.remaining_players)):
                if self.remaining_players[x] == first_player:
                    self.current_player = x
                    break

    def setup_round(self, winning_player):
        self.current_deck = self.deck.copy()
        self.remaining_players = self.players.copy()
        for x in range(len(self.remaining_players)):
            if self.remaining_players[x] == winning_player:
                self.current_player = 0
                break

    def next_player(self):
        self.current_player += 1
        self.current_player = self.current_player % len(self.remaining_players)

    def draw_the_card_hands(self):
        for count, player in enumerate(self.remaining_players):
            if player == self.remaining_players[self.current_player]:
                continue  # This should remove the showing yourself.
            print(count, ":", player.name, end="   ")

        print("""
        """)
        for player in self.remaining_players:
            if player == self.remaining_players[self.current_player]:
                for count, card in enumerate(player.cards):
                    print("   ",count, ":", card.name)

    def draw_the_discard(self):
        # Draw/ Write the names of the cards in the discard pile.
        for card in self.discarded_cards:
            print(card, end=" ")
        print()

    def discard_a_card(self, player, card):
        # removes the card from player and adds it to the pile of discarded cards
        # CHECK FOR PRINCESS!!!
        # Do I want to return something here to deal with this?
        if card.name == "Princess":
            print(player.name + " discarded the princess. They are removed from the round.")
            self.player_removed_from_round(player)
            return "Finished"
        print("PLAYER: ", player)
        self.discarded_cards.append(card)
        player.cards.remove(card)

    def shuffle_the_deck(self):
        shuffled_deck = []
        while len(self.current_deck) > 0:
            current = random.randint(0, len(self.current_deck)-1)
            # shuffled_deck.append(self.current_deck[current])
            # self.current_deck.pop(current)
            shuffled_deck.append(self.current_deck.pop(current))

        return shuffled_deck

    def deal_a_card(self, player):
        player.cards.append(self.current_deck[0])
        self.current_deck.pop(0)

    def finish_actions(self) -> str:
        self.selected_player = None
        self.selected_card = None
        return "Finished"

    def card_actions(self, action):
        while True:
            if action == "Name a card":
                print("Which non-guard card would you like to choose?")
                print("Please type one of the following:")
                selected_card = input("priest, baron, handmaid, prince, king, countess, or princess")
                # Check to make sure the selected_card is a selectable card.
                for card in self.list_of_cards:
                    if card == 'guard':
                        continue
                    elif selected_card == card:
                        self.selected_card = card
                        print(card)
                        return selected_card
                    else:
                        "That is not one of the card choices. Please try again."

            if action == "Choose another player":
                print("Which player would you like to choose?")
                players = ""
                # Displays the other players.
                unprotected_players = 0
                total_other_players = 0
                for player in self.remaining_players:
                    if player == self.remaining_players[self.current_player]:
                        continue  # This should remove the showing yourself.
                    elif player.is_protected:
                        players += "(" + player.name + ") "
                        total_other_players += 1
                    else:
                        players += player.name + " "
                        unprotected_players += 1
                        total_other_players += 1

                target_player = input(players)
                if unprotected_players == 0:
                    print("There are no targets that you can target. The spell fizzles out.")
                    return self.finish_actions()
                for player in self.remaining_players:
                    if player == self.remaining_players[self.current_player]:
                        continue  # This should remove the ability to target yourself.
                    elif player.is_protected is True:
                        print("Sorry that player is protected. Try someone else.")
                        continue  # This should remove the ability to target a protected player.
                    elif target_player == player.name:
                        self.selected_player = player
                        return target_player

            if action == "Choose any player":
                # How much different is this than the previous one?
                print("Which player would you like to choose?")
                players = ""
                # Displays the other players.
                unprotected_players = 0
                total_other_players = 0
                for player in self.remaining_players:
                    if player.is_protected:
                        players += "(" + player.name + ") "
                        total_other_players += 1
                    else:
                        players += player.name + " "
                        unprotected_players += 1
                        total_other_players += 1

                target_player = input(players)
                if unprotected_players == 0:
                    print("There are no targets that you can target. The spell fizzles out.")
                    return self.finish_actions()
                for player in self.remaining_players:
                    if player.is_protected is True:
                        print("Sorry that player is protected. Try someone else.")
                        continue  # This should remove the ability to target a protected player.
                    elif target_player == player.name:
                        self.selected_player = player
                        return target_player

            if action == "If player has named card, player out of round":
                for card in self.selected_player.cards:
                    if card.name.lower() == self.selected_card:
                        print(self.selected_player.name + "'s card IS " + self.selected_card)
                        print(self.selected_player.name + " is now out of the round.")
                        self.remaining_players.remove(self.selected_player.name)
                    else:
                        print(self.selected_player.name + "'s card is not " + self.selected_card)
                    return self.finish_actions()

            if action == "Look at chosen players hand.":
                # Display target players hand to current player.
                print("You look at " + self.selected_player.name + " cards.")
                return self.finish_actions()

            if action == "Secretly compare hands.":
                # Display current players hand and target players hand
                # only to the current player and target player.
                print("You and " + self.selected_player.name + " compare your cards.")
                return 0  # I think this does what I want it to.

            if action == "The lower value is out of the round.":
                # Do I want this to be a different one from the previous one?
                print("The person with the lower value is out.")
                return self.finish_actions()

            if action == "Protection from other attacks":
                self.remaining_players[self.current_player].is_protected = True
                return self.finish_actions()


            if action == "Target player discards hand and draws a new card":
                print(self.selected_player.name + " discared their cards and drew a new card.")
                if self.remaining_players[self.current_player] == self.selected_player:
                    for card in self.selected_player.cards:
                        if card.name.lower() == "prince":  # This will keep the card in 'play'/'hand' to discard afterwards.
                            continue
                        fin = self.discard_a_card(self.selected_player, card)
                        if fin == "Finished":
                            return self.finish_actions()
                for card in self.selected_player.cards:
                    fin = self.discard_a_card(self.selected_player, card)
                    if fin == "Finished":
                        return self.finish_actions()
                self.deal_a_card(self.selected_player)
                return self.finish_actions()

            if action == "Player and target player swap hands.":
                temp_cards = self.remaining_players[self.current_player].cards
                self.remaining_players[self.current_player].cards = self.selected_player
                self.selected_player.cards = temp_cards
                return self.finish_actions()

            if action == "If other card is 5 or 6 discard this card":
                return self.finish_actions()

            if action == "If you discard this card you are out of round.":
                # DO I need that as it 'should' do that when discarded afterwards.
                # self.player_removed_from_round(self.remaining_players[self.current_player])
                return self.finish_actions()

            if action == "None":
                return self.finish_actions()


class ObjectCard:
    def __init__(self, number, name, description, actions):
        self.number = number
        self.name = name
        self.description = description
        self.actions = actions

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(number={self.number!r}, name={self.name!r}, description=" \
               f"{self.description!r}, actions={self.actions!r}"

    def __str__(self) -> str:
        return f"{self.name}"


class ComponentBasicAI:
    def __init__(self, player=None):
        self.owner = player

    def take_turn(self, board):
        # Returns the value of the location that the ai wants to take.
        allowed_moves = []
        opponent = []
        player = []
        for x in range(0, len(board)):
            for y in range(0, len(board[0])):
                if board[x][y] == str(y) + str(x):
                    allowed_moves.append(board[x][y])
                elif board[x][y] == self.owner.symbol:
                    player.append(str(y) + str(x))
                else:
                    opponent.append(str(y) + str(x))
        for move in allowed_moves:
            if move == "11":
                return 11
        # Checks to see if there are any cells that will allow the player to 'win'
        # if so takes one of those locations.
        # Checks to see if there are any cells that will allow the opponent to 'win'
        # if so takes one of those locations.
        # Checks to see if there are any cells that will make the player 1 away from winning
        #


if __name__ == "__main__":
    main_game_loop()
