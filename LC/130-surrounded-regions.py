class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def flip_board():
            print(board)
            for r in range(len(board)):
                for c in range(len(board[0])):
                    if board[r][c] == "X":
                        continue

                    if board[r][c] == "O":
                        board[r][c] = "X"
                        continue
                    # M
                    board[r][c] = "O"


        def mark_as_m(r, c):
            if board[r][c] in ["X", "M"]:
                return

            # is O
            board[r][c] = "M"

            if r > 0:
                mark_as_m(r - 1, c)

            if r < len(board) - 1:
                mark_as_m(r + 1, c)

            if c > 0:
                mark_as_m(r, c - 1)

            if c < len(board[0]) - 1:
                mark_as_m(r, c + 1)


        if not board:
            return board

        # first-row
        for c in range(len(board[0])):
            mark_as_m(0, c)

        # last-row
        for c in range(len(board[0])):
            last_row = len(board) - 1
            mark_as_m(last_row, c)

        # first-column
        for r in range(len(board)):
            mark_as_m(r, 0)

        # last-column
        for r in range(len(board)):
            last_column = len(board[0]) - 1
            mark_as_m(r, last_column)

        flip_board()

        return board

