class Solution:

    def exist(self, board: list[list[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])

        def search(i, j, k):

            if k == len(word):
                return True

            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False

            if board[i][j] != word[k]:
                return False

            temp = board[i][j]
            board[i][j] = "#"

            if (search(i - 1, j, k + 1) or
                search(i + 1, j, k + 1) or
                search(i, j - 1, k + 1) or
                search(i, j + 1, k + 1)):

                return True

            board[i][j] = temp

            return False

        for i in range(rows):
            for j in range(cols):

                if search(i, j, 0):
                    return True

        return False