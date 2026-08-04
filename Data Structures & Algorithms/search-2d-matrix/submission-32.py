class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix[0]) - 1
        row = []
        for cur_row in matrix:
            if cur_row[0] <= target <= cur_row[-1]:
                row = cur_row
                break
        if not row:
            return False

        while left <= right:
            middle = (left + right) // 2
            # print(left, right, row, middle)

            if target == row[middle]:
                return True
            elif target < row[middle]:
                row = row[left:middle]
                right = len(row) -1
                # print(right)
            elif target > row[middle]:
                row = row[middle+1:right +1]
                right = len(row) -1


        return False



        