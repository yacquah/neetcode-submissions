class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS-1
        
        
        while top <= bot:
            trow = (top + bot)// 2
            if target < matrix[trow][0]:
                bot = trow -1
            elif target > matrix[trow][-1]:
                top = trow + 1
            else:
                break
        
        if top > bot:
            return False

        l, r = 0, COLS-1

        while l <= r:
            mid = (r + l)// 2
            if target == matrix[trow][mid]:
                return True
            elif target < matrix[trow][mid]:
                r = mid - 1
            else:
                l = mid + 1
        return False
