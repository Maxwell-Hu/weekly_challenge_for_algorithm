class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not len(matrix): return []
        boarder = [0, len(matrix[0])-1, len(matrix)-1, 0]
        res = []
        while boarder[0] <= boarder[2] and boarder[1] >= boarder[3]:
            res += [matrix[boarder[0]][i] for i in range(boarder[3], boarder[1]+1)]
            boarder[0] += 1
            if boarder[0] > boarder[2]: break

            res += [matrix[i][boarder[1]] for i in range(boarder[0], boarder[2]+1)]
            boarder[1] -= 1
            if boarder[1] < boarder[3]: break

            res += [matrix[boarder[2]][i] for i in range(boarder[1], boarder[3]-1, -1)]
            boarder[2] -= 1
            if boarder[2] < boarder[0]: break

            res += [matrix[i][boarder[3]] for i in range(boarder[2], boarder[0]-1, -1)]
            boarder[3] += 1
            if boarder[3] > boarder[1]: break
        return res