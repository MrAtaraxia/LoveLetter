# Base imports
import random
import json
# Other imports

# My imports



class Networking:
    def __init__(self):
        pass

    def make_connection(self):
        pass

    def send(self):
        pass

    def receive(self):
        pass


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


def make_the_deck():
    new_deck = []
    with open('data.json') as json_file:
        data = json.load(json_file)
        for p in data['cards']:
            for i in range(p["Count"]):
                new_deck.append(ObjectCard(p["Number"], p["Name"], p["Description"], p["Actions"]))
    return new_deck


class ObjectGame:
    def __init__(self, number_of_players=2, player_names=None):
        self.number_of_players = number_of_players
        if player_names is None:
            self.players = [ObjectPlayer("Player " + str(x)) for x in range(self.number_of_players)]
        else:
            self.players = []
            for x in range(self.number_of_players):
                try:
                    self.players.append(ObjectPlayer(player_names[x]))
                except IndexError:
                    self.players.append(ObjectPlayer("Player" + str(x)))
            # self.players = [ObjectPlayer(name) for name in player_names]
        self.deck = make_the_deck()

        # The following are used for the round and restored between rounds.
        self.current_deck = self.deck.copy()
        self.remaining_players = self.players.copy()
        self.current_player = 0
        self.current_card = None  # The current card that is being resolved.
        self.discarded_cards = []
        # discards 3 cards if playing 2 players.
        if self.number_of_players == 2:
            for x in range(3):
                self.discarded_cards.append(self.current_deck.pop(0))
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
        for card in player_to_remove.cards:
            self.discarded_cards.append(card)
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
        # Create a copy of the deck
        self.current_deck = self.deck.copy()
        # Shuffle the deck
        self.current_deck = self.shuffle_the_deck()
        # Put all players back in the game.
        self.remaining_players = self.players.copy()
        # Clears the current card that is being resolved.
        self.current_card = None  # Should not need to do this but doing it just to be safe.
        # Clear the hidden card.
        self.hidden_cards = []
        # Hides a card.
        self.hidden_cards.append(self.current_deck.pop(0))
        # Clear the played cards.
        self.discarded_cards = []
        # discards 3 cards if playing 2 players.
        if self.number_of_players == 2:
            for x in range(3):
                self.discarded_cards.append(self.current_deck.pop(0))
        # The winner of the last round goes first.
        for count, player in enumerate(self.remaining_players):
            if player == winning_player:
                self.current_player = count
            # Resets the count of the discarded/played amount for each player.
            player.discarded_amount = 0
            # Resets the cards in the hand.
            player.cards = []
            self.deal_a_card(player)

        #for x in range(len(self.remaining_players)):
        #    if self.remaining_players[x] == winning_player:
        #        self.current_player = x
        #        break

    def next_player(self):
        self.current_player += 1
        self.current_player = self.current_player % len(self.remaining_players)

    def draw_other_players(self):
        for count, player in enumerate(self.remaining_players):
            if player == self.remaining_players[self.current_player]:
                continue  # This should remove the showing yourself.
            if player.is_protected:
                print("(" + str(count) + " : " + player.name, "*"*player.score, ")", sep="", end="   ")
            else:
                print(count, ":", player.name, "*"*player.score, end="")
                for card in player.cards:
                    print(" ", card.name, end="")
                print("", end="   ")
        print("")

    def draw_the_card_hands(self):
        for player in self.remaining_players:
            if player == self.remaining_players[self.current_player]:
                for count, card in enumerate(player.cards):
                    print("   ", count, ":", card.name, "(", card.number, ")")
                    print(card.description)

    def draw_the_discard(self):
        # Draw/ Write the names of the cards in the discard pile.
        print("Discarded Cards: ", end="")
        for card in self.discarded_cards:
            print(card, end=" ")
        print()

    def draw_round_end(self, player):
        # Draw/ Write the names of the cards in the discard pile.
        print("Player {name} won the round. Their score increased by 1.".format(name=player.name))
        print("Player {name}'s current score is {score}".format(name=player.name, score=player.score))
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
        print("PLAYER:", player, "discarded a card.")
        self.discarded_cards.append(card)
        player.cards.remove(card)

    def shuffle_the_deck(self):
        shuffled_deck = []
        while len(self.current_deck) > 0:
            current = random.randint(0, len(self.current_deck) - 1)
            # shuffled_deck.append(self.current_deck[current])
            # self.current_deck.pop(current)
            shuffled_deck.append(self.current_deck.pop(current))

        return shuffled_deck

    def deal_a_card(self, player, deck="deck"):
        # print("Player", player.name, "was dealt a card")
        if deck == "deck":
            print("Player {name} was dealt a card".format(name=player.name))
            player.cards.append(self.current_deck.pop(0))
            # self.current_deck.pop(0)
        elif deck == "removed":
            print("Player {name} was dealt the hidden card".format(name=player.name))
            player.cards.append(self.hidden_cards.pop(0))


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
                    elif selected_card.lower() == card:
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
                for count, player in enumerate(self.remaining_players):
                    if player == self.remaining_players[self.current_player]:
                        continue  # This should remove the showing yourself.
                    elif player.is_protected:
                        players += "(" + str(count) + " : " + player.name + ") "
                        total_other_players += 1
                    else:
                        players += str(count) + " : " + player.name + " "
                        unprotected_players += 1
                        total_other_players += 1

                target_player = input(players)
                if unprotected_players == 0:
                    print("There are no targets that you can target. The spell fizzles out.")
                    return self.finish_actions()
                for count, player in enumerate(self.remaining_players):
                    if player == self.remaining_players[self.current_player]:
                        continue  # This should remove the ability to target yourself.
                    elif player.is_protected is True:
                        print("Sorry that player is protected. Try someone else.")
                        continue  # This should remove the ability to target a protected player.
                    elif target_player == player.name or target_player == str(count):
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
                        self.remaining_players.remove(self.selected_player)
                    else:
                        print(self.selected_player.name + "'s card is not " + self.selected_card)
                    return self.finish_actions()

            if action == "Look at chosen players hand.":
                # Display target players hand to current player.
                print("You look at " + self.selected_player.name + " cards.")
                for card in self.selected_player.cards:
                    print(card, end="")
                print("")
                return self.finish_actions()

            if action == "Secretly compare hands.":
                # Display current players hand and target players hand
                # only to the current player and target player.
                current_value = 0
                selected_value = 0
                print("You and " + self.selected_player.name + " compare your cards.")
                print(self.remaining_players[self.current_player].name, "'s cards: ", sep="", end="")
                for card in self.remaining_players[self.current_player].cards:
                    print(card.name, end=" ")
                    current_value = card.number
                print("")
                print(self.selected_player.name, "'s cards: ", sep="", end="")
                for card in self.selected_player.cards:
                    print(card.name, end=" ")
                    selected_value = card.number
                print("")
                if selected_value < current_value:
                    print("Player {selected}'s card has a lower value.".format(selected=self.selected_player.name))
                    self.player_removed_from_round(self.selected_player)
                elif selected_value > current_value:
                    print("Player {current}'s card has a lower value.".format(current=
                                                                               self.remaining_players
                                                                               [self.current_player]))
                    self.player_removed_from_round(self.remaining_players[self.current_player])
                else:
                    print("Both players had cards with the same value.")
                return self.finish_actions()

            if action == "The lower value is out of the round.":
                # THIS SHOULD NOT BE CALLED
                # Do I want this to be a different one from the previous one?
                print("THIS SHOULD NOT BE CALLED")
                return self.finish_actions()

            if action == "Protection from other attacks":
                self.remaining_players[self.current_player].is_protected = True
                return self.finish_actions()

            if action == "Target player discards hand and draws a new card":
                print(self.selected_player.name + " discared their cards and drew a new card.")

                for card in self.selected_player.cards:
                    fin = self.discard_a_card(self.selected_player, card)
                    if fin == "Finished":
                        return self.finish_actions()
                if len(self.current_deck) == 0:
                    print("There are no cards left in the deck.")
                    self.deal_a_card(self.selected_player, deck="removed")
                else:
                    self.deal_a_card(self.selected_player)
                return self.finish_actions()

            if action == "Player and target player swap hands.":
                self.remaining_players[self.current_player].cards, self.selected_player.cards = \
                    self.selected_player.cards, self.remaining_players[self.current_player].cards
                # temp_cards = self.remaining_players[self.current_player].cards
                # self.remaining_players[self.current_player].cards = self.selected_player
                # self.selected_player.cards = temp_cards
                return self.finish_actions()

            if action == "If other card is 5 or 6 discard this card":
                return self.finish_actions()

            if action == "If you discard this card you are out of round.":
                return self.finish_actions()

            if action == "None":
                return self.finish_actions()


class ObjectPlayer:
    def __init__(self, name, ai=None):
        self.name = name
        self.score = 0
        self.cards = []
        self.ai = ai
        self.is_protected = False
        if self.ai:
            self.ai.owner = self
        self.discarded_amount = 0

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, ai={self.ai!r})"


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


def main():
    pass


if __name__ == "__main__":
    main()