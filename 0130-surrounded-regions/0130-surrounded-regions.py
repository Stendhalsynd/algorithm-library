from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """ 
        m, n = len(board), len(board[0])
        
        def convertMarginRegionInto(target, char):
            for i in range(m):
                for j in range(n):
                    if i in [0, m - 1] and board[i][j] == target:
                        board[i][j] = char # 경계 margin
                    elif j in [0, n - 1] and board[i][j] == target:
                        board[i][j] = char
                        
        def bfs():
            for i in range(m):
                for j in range(n):
                    if board[i][j] == 'O':
                        que = deque([(i, j)])
                        check = deque([(i, j)])
                        board[i][j] = 'X'
                        isSurrounded = True
                        while que:
                            y, x = que.popleft()
                            for dy, dx in (0, 1), (1, 0), (0, -1), (-1, 0):
                                ny, nx = y + dy, x + dx
                                if board[ny][nx] == 'M':
                                    isSurrounded = False
                                    que.clear()
                                    break
                                if 1 <= ny < m - 1 and 1 <= nx < n - 1 and board[ny][nx] == 'O':
                                    que.append((ny, nx))
                                    check.append((ny, nx))
                                    board[ny][nx] = 'X'
                        if not isSurrounded:
                            while check:
                                y, x = check.pop()
                                board[y][x] = 'O'
                        
                        for dy, dx in (0, 1), (1, 0), (0, -1), (-1, 0):
                            ny, nx = i + dy, j + dx
                            if board[ny][nx] == 'M':
                                board[i][j] = 'O'
                        
        convertMarginRegionInto('O', 'M')
        
        bfs()
        
        convertMarginRegionInto('M', 'O')
        
        
                