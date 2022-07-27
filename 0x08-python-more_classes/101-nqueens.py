#!/usr/bin/python3
"""This module solves the Nqueens problem"""


class Solution:
    """
    example : [[0, 1], [1, 3], [2, 0], [3, 2]]
    """
    def solveNQueens(self, n: int):
        solutions = []
        state = []
        self.search(state, solutions, n)
        self.output(solutions)
        return solutions

    def output(self, solutions):
        for i in solutions:
            print(i)
        return

    def is_valid_state(self, state, n):
        # check if it is a valid solution
        return len(state) == n

    def get_candidates(self, state, n):
        if not state:
            return range(n)

        # find the next position in the state to populate
        position = len(state)
        candidates = set(range(n))

        for row, col in enumerate(state):
            candidates.discard(col)
            dist = position - row
            candidates.discard(col + dist)
            candidates.discard(col - dist)
        return candidates

    def search(self, state, solutions, n):
        if self.is_valid_state(state, n):
            state_2d = self.state_to_2d(state, n)
            solutions.append(state_2d)
            return

        for candidate in self.get_candidates(state, n):
            state.append(candidate)
            self.search(state, solutions, n)
            state.pop()

    def state_to_2d(self, state, n):
        ret = []
        for i in range(len(state)):
            ret.append([i, state[i]])

        return ret


if __name__ == '__main__':

    import sys

    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except Exeception as e:
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    queen = Solution()
    queen.solveNQueens(size)
