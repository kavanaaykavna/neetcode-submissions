class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:

        original = [row[:] for row in matrix]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if original[i][j] == 0:

                    # Make entire row zero
                    for x in range(len(matrix[0])):
                        matrix[i][x] = 0

                    # Make entire column zero
                    for y in range(len(matrix)):
                        matrix[y][j] = 0