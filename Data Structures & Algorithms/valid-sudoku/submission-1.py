class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create hash tables
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        # row
        for r in range(9):
            # col
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                elif (num in rows[r]
                or num in cols[c]
                or num in squares[(r//3, c//3)]):
                    return False

                rows[r].add(num)
                cols[c].add(num)
                # floor division to group numbers in 3 x 3
                squares[(r//3, c//3)].add(num)

        return True