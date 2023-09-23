import random
from Design_patterns.snakeAndLadder.cell import Cell
from Design_patterns.snakeAndLadder.jump import Jump


class Board:
    def __init__(self, board_size, number_of_snakes, number_of_ladders):
        self.board_size = board_size
        self.number_of_snakes = number_of_snakes
        self.number_of_ladders = number_of_ladders
        self.snake_tail = None
        self.snake_head = None
        self.ladder_tail = None
        self.ladder_head = None
        self.cells = None
        self.initialise_board()

    def initialise_board(self):
        self.initialise_cells()
        self.add_snakes_ladders()

    def initialise_cells(self):
        self.cells = [[Cell() for _ in range(self.board_size)] for _ in range(self.board_size)]


    def add_snakes_ladders(self):
        while self.number_of_snakes > 0:
            self.snake_head = random.randint(1, self.board_size * self.board_size - 1)
            self.snake_tail = random.randint(1, self.board_size * self.board_size - 1)

            if self.snake_tail >= self.snake_head:
                continue

            snake_obj = Jump(self.snake_head, self.snake_tail)
            cell = self.get_cell(self.snake_head)
            cell.jump = snake_obj
            self.number_of_snakes -= 1

        while self.number_of_ladders > 0:
            self.ladder_head = random.randint(1, self.board_size * self.board_size - 1)
            self.ladder_tail = random.randint(1, self.board_size * self.board_size - 1)

            if self.ladder_head >= self.ladder_tail:
                continue

            ladder_obj = Jump(self.ladder_head, self.ladder_tail)
            cell = self.get_cell(self.ladder_head)
            cell.jump = ladder_obj
            self.number_of_ladders -= 1

    def get_cell(self, player_position):
        boardRow = int(player_position / len(self.cells))
        boardColumn = int(player_position % len(self.cells[0]))
        return self.cells[boardRow][boardColumn]
