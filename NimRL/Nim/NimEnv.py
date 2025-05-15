import numpy as np

class Nim:

    def __init__(self, piles, stones, limit):
        self.piles = piles
        self.stones = stones
        self.limit = limit
        self.winner = None
        self.turns = 0
        self.cur_player = 1
        self.board = [stones] * piles

        self.history = []
        self.history.append(self.get_state())

    def display(self):
        if self.history:
            print(f"\nTurn {self.turns}, Current Player: {self.cur_player}, Piles: {self.board}")
        else:
            print(f"Initial Board: {self.board}")

    def copy(self):
        new_state = Nim(self.piles, self.stones, self.limit)
        new_state.winner = self.winner
        new_state.turns = self.turns
        new_state.cur_player = self.cur_player
        new_state.board = self.board.copy()
        new_state.history = self.history.copy()
        return new_state

    def check_for_win(self):
        if all(stones == 0 for stones in self.board):
            self.game_over = True
            self.winner = self.cur_player
        else:
            self.game_over = False
            self.winner = None

    def get_actions(self):
        actions = []
        for i in range(self.piles):
            for j in range(1, min(self.board[i], self.limit) + 1):
                actions.append((i, j))
        return actions

    def take_action(self, a):
        new_state = self.copy()
        pile_index, stones_removed = a
        new_state.board[pile_index] -= stones_removed
        new_state.turns += 1
        new_state.cur_player = 3 - self.cur_player
        new_state.check_for_win()

        return new_state

    def reset(self):
        # Reinitialize the state of the game
        self.board = [self.stones] * self.piles
        self.winner = None
        self.turns = 0
        self.cur_player = 1
        self.history = []
        self.history.append(self.get_state())
        return self.get_state()  # Return the initial state as required

    def get_state(self):
        s = 0
        for i in range(self.piles):
            s += self.board[i] * (self.stones + 1) ** i
        return s

    def heuristic(self, agent, mode=None):
        return 0

#Code written by Kelby Craft