
from collections import deque
import random
from Design_patterns.snakeAndLadder.board import Board
from Design_patterns.snakeAndLadder.dice import Dice
from Design_patterns.snakeAndLadder.player import Player


class Game:
    def __init__(self):
        self.board = Board(10, 5, 4)
        self.dice = Dice(1)
        self.playersList = deque([Player("Alice", 0), Player("Bob", 0)])
        self.winner = None

    def startGame(self):
        # while len(self.playersList)>1:
        #     player_turn = self.find_player_turn()
        #     print("player turn is:" + player_turn.id + " current position is: " + str(player_turn.current_position))
        #
        #     dice_numbers = self.dice.roll_dice()
        #     print("dice no is ", dice_numbers)
        #
        #     player_new_position = player_turn.current_position + dice_numbers
        #     if player_new_position >= len(self.board.cells) * len(self.board.cells[0]) - 1:
        #         print(f"{player_turn.id} won the game")
        #         self.playersList.pop()
        #     player_new_position = self.jump_check(player_new_position)
        #     player_turn.current_position = player_new_position
        #     print("player turn is:" + player_turn.id + " new Position is: " + str(player_new_position))
        #
        #     if player_new_position == len(self.board.cells) * len(self.board.cells[0]) - 1:
        #         print(f"{player_turn.id} won the game")
        #
        # print(f"{self.playersList[0].id } lost the game")


        while self.winner is None:
            # check whose turn now
            player_turn = self.find_player_turn()
            print("player turn is:" + player_turn.id + " current position is: " + str(player_turn.current_position))

            # roll the dice
            dice_numbers = self.dice.roll_dice()
            print("dice no is ", dice_numbers)

            # get the new position
            player_new_position = player_turn.current_position + dice_numbers
            player_new_position = self.jump_check(player_new_position)
            player_turn.current_position = player_new_position

            print("player turn is:" + player_turn.id + " new Position is: " + str(player_new_position))

            # check for winning condition
            if player_new_position >= len(self.board.cells) * len(self.board.cells[0]) - 1:
                self.winner = player_turn

        print("WINNER IS:" + self.winner.id)



    def find_player_turn(self):
        player_turns = self.playersList.popleft()
        self.playersList.append(player_turns)
        return player_turns

    def jump_check(self, player_new_position):
        if player_new_position > len(self.board.cells) * len(self.board.cells[0]) - 1:
            return player_new_position

        cell = self.board.get_cell(player_new_position)
        if cell.jump is not None and cell.jump.start == player_new_position:
            jumpBy = "ladder" if cell.jump.start < cell.jump.end else "snake"
            print("jump done by: " + jumpBy)
            return cell.jump.end
        return player_new_position


