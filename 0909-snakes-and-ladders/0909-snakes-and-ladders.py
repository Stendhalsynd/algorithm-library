# array, breadth-first search, matrix
from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:        
        def reverse_rows(board): # 반전된 행 뒤집기
            reversed_rows = board[::-1]
            for idx, row in enumerate(reversed_rows):
                if idx % 2 == 1:
                    reversed_rows[idx] = row[::-1]
            return reversed_rows
            
        board = reverse_rows(board)
        array = [-1] + sum(board, []) # 인덱스와 숫자를 일치시켜주기 위해 앞에 의미없는 -1 추가하고 2차원 배열을 1차원으로 돌리기 위해 sum 함수 사용
        destination = len(array) - 1 # 목적지
        
        start = 1
        que = deque([1])
        visited = set()
        count = 0
        
        # bfs
        while que:
            for _ in range(len(que)): # 현재 큐에 있는 숫자들은 이전 단계에서 방문할 수 있었던 모든 위치
                curr = que.popleft() # bfs 순회

                if array[curr] != -1: # 사다리나 뱀이었으면 현재 위치를 해당 목표지점으로 이동
                    curr = array[curr]
                if curr == destination: # 목적지에 도착했으면 그때까지 count 를 바노한
                    return count
                for i in range(1, 7): # 주사위는 1 ~ 6
                    next = curr + i
                    if next <= destination and next not in visited: # 다음 지점이 목적지 이내이고 방문한적 없으면 큐에 추가하고 방문했음을 기록
                        que.append(next)
                        visited.add(next)
            count += 1
        
        # 만약 남은게 모두 방문했던 곳인데 return 조건문에 들어가지 못했다면 while 을 탈출하게 되어 -1 을 반환
        return -1