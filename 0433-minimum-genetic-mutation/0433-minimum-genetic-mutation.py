# Hash Table, String, Breath-First Search
from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        que = deque([startGene])
        info = deque(bank)
        count = 0
        gene = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
        visited = set()
        
        # bfs
        while que:
            for _ in range(len(que)):
                curr = que.popleft()
                
                if curr == endGene: # endGene 까지 변형이 완료
                    return count
                
                for idx, char in enumerate(curr):                    # 현재 유전자 문자열을 idx, char 로 순회
                    for mutate_gene in gene.values():                # 유전자 리스트 gene 의 값들 (A, C, G, T) 중에서 현재 char 과 다른 유전자로 변형 
                        compare = list(curr)                         # mutation 을 위해 문자열에서 리스트로 변환
                        if mutate_gene != char:                      # 현재 유전자중 해당 idx 에서의 char 을 다른 유전자로 변형한다면
                            compare[idx] = mutate_gene               # 해당 idx 의 유전자만 변형한 compare
                            next = ''.join(compare)                  # 다시 비교를 위해 리스트에서 문자열로 join
                            if next in info and next not in visited: # 만약 변형한 next 가 bank 에 존재하고 변형된 이력이 없는 유전자라면
                                que.append(next)                     # bfs 순회. 큐에 다음 변형된 유전자 next 를 append 
                                visited.add(next)                    # 변형된 해당 유전자 방문처리
            count += 1
        return -1
                    