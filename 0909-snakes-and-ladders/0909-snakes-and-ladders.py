# array, breadth-first search, matrix
from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # board = [[-1,-1,-1,-1,-1,-1],
        #          [-1,-1,-1,-1,-1,-1],
        #          [-1,-1,-1,-1,-1,-1],
        #          [-1,35,-1,-1,13,-1],
        #          [-1,-1,-1,-1,-1,-1],
        #          [-1,15,-1,-1,-1,-1]]
        
        def reverse_rows(board):
            reversed_rows = board[::-1]
            for idx, row in enumerate(reversed_rows):
                if idx % 2 == 1:
                    reversed_rows[idx] = row[::-1]
            return reversed_rows
            
        board = reverse_rows(board)
        array = [-1] + sum(board, [])
        # print(one_demension_board)
        destination = len(array) - 1
        
        start = 1
        que = deque([1])
        visited = set()
        count = 0
        
        while que:
            for _ in range(len(que)):
                curr = que.popleft()

                if array[curr] != -1:
                    curr = array[curr]
                if curr == destination:
                    return count
                for i in range(1, 7):
                    next = curr + i
                    if next <= destination and next not in visited:
                        que.append(next)
                        visited.add(next)
            count += 1
        
        return -1