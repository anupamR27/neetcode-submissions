class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top = 0
        bottom = ROWS - 1

        while (top <= bottom):
            row = (top + bottom) // 2

            if (target > matrix[row][-1]):
                top = row + 1
            elif (target < matrix[row][0]):
                bottom = row - 1
            else: 
                break

        low = 0
        high = len(matrix[row]) - 1

        while(low<=high):
            mid = (low+high)//2

            if(matrix[row][mid] == target):
                return True
            elif (matrix[row][mid] > target):
                high = mid - 1
            elif (matrix[row][mid] < target):
                low = mid + 1
        
        return False