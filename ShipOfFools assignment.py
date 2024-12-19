import random


class Die:
    #roll the dies for random values 1 to 6
    def __init__(self) -> None:
        #call roll method and returns none
        self.__value = 0
        self.roll()

    def get_value(self) -> int:
        #returns the value
        return self.__value

    def roll(self) -> None:
        #returns random value between 1 and 6 to init function 
        self.__value = random.randint(1, 6)


class DiceCup:
    #This class  banks and releases the dice and checks for die is banked or not
    def __init__(self) -> None:
	#set all values to false and roll the dice
        self.listBank = [False]*5
        self.__diceValues = [Die() for roll_the_die in range(5)]

    def value(self, index: int) -> int:
        #Returns the dice value of type int
        return self.__diceValues[index].get_value()

    def bank(self, index: int) -> None:
        #Banks the value and assigns value True
        self.listBank[index] = True

    def is_banked(self, index: int) -> bool:
        #Checks for the dice is banked or not
        return self.listBank[index]

    def release(self, index: int) -> None:
        #Release the dice value and assigns False value
        self.listBank[index] = False

    def release_all(self) -> None:
        #Releases all the dice
        for value in range(5):
            self.listBank[value] = False

    def roll(self) -> None:
        #rolls the dice
        for value in range(5):
            if not self.listBank[value]:
                self.__diceValues[value].roll()


class ShipOfFoolsGame:
    #calculate score in every round
    def __init__(self) -> None:
        self._cup = DiceCup()
        self._winning_score = 21

    def round(self) -> int:
        #rollin the dice 3 times
        has_ship = False
        has_captain = False
        has_crew = False
        max_total = 0
        for round in range(3):
            self._cup.roll()
            scores = []

            for value in range(5):
                scores.append(self._cup.value(value))
            print(scores)
	    #check for ship
            if not has_ship:
                for value in range(5):
                    if self._cup.value(value) == 6:
                        has_ship = True
                        self._cup.bank(value)
                        break
	    #check for presence of ship and no captain
            if has_ship and not has_captain:
                for value in range(5):
                    if not self._cup.is_banked(value):
                        if self._cup.value(value) == 5:
                            has_captain = True
                            self._cup.bank(i)
                            break
	    #check if crew is not present
            if has_ship and has_captain and not has_crew:
                for value in range(5):
                    if not self._cup.is_banked(value):
                        if self._cup.value(value) == 4:
                            has_crew = True
                            self._cup.bank(value)
                            break
	    #check all are banked
            if has_ship and has_captain and has_crew:
                if round+1 == 3:
                    for value in range(5):
                        if not self._cup.is_banked(value):
                            max_total += self._cup.value(value)
                else:
                    for value in range(5):
                        if not self._cup.is_banked(value):
                            if self._cup.value(value) > 3:
                                max_total += self._cup.value(value)
                                self._cup.bank(value)

        self._cup.release_all()
        return max_total


class PlayRoom:
    #used to add players in the game
    #player plays the game,this function prints the value
    def __init__(self) -> None:
        self._game = None
        self._players = []

    def set_game(self, game: ShipOfFoolsGame) -> None:
      	#start the game
        self._game = game

    def add_player(self, player: str) -> None:
        #add player
        self._players.append(player)

    def reset_scores(self) -> None:
        #reset score
        for player in self._players:
            player.reset_score()

    def play_round(self) -> None:
        #player plays all rounds
        for player in self._players:
            if not self.game_finished():
                player.play_round(self._game)

    def game_finished(self) -> bool:
        #print score if reached maximum
        for player in self._players:
            if player.current_score() > 21:
                return True
        return False

    def print_scores(self) -> None:
        #print the scores of all players
        print("players total are")
        for player in self._players:
            print(f"{player.name} current score: {player.current_score()}")

    def print_winner(self) -> None:

        #print winner name
        for player in self._players:
            if player.current_score() > 21:
                print(f"{player.name} is the winner of the game")
                break


class Player:
    #display name and score and reset the values

    def __init__(self, name: str) -> None:
        #set name and scores of players
        self._name = name
        self._score = 0

    def set_name(self, namestring: str) -> None:
        #nname of player
        self._name = namestring

    def current_score(self) -> None:
        #return score pf player
        return self._score

    def reset_score(self) -> None:
        #reset score
        self._score = 0

    def play_round(self, game: ShipOfFoolsGame) -> None:
        print(self._name, "match is started...!!")
        start = game.round()
        print(self._name, "'s score in this round is", start)
        self._score += start

    @property
    def name(self):
        return self._name


if __name__ == "__main__":
    game_p = PlayRoom()
    game_p.set_game(ShipOfFoolsGame())
    game_p.add_player(Player("sri"))
    game_p.add_player(Player("royal"))
    game_p.add_player(Player("abhi"))

    while not game_p.game_finished():
        game_p.play_round()
        game_p.print_scores()
    game_p.print_winner()
    game_p.reset_scores()
