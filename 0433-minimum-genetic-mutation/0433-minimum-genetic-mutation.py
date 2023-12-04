# Hash Table, String, Breath-First Search
from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        que = deque([startGene])
        info = deque(bank)
        count = 0
        gene = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
        visited = set()
        
        while que:
            for _ in range(len(que)):
                curr = que.popleft()
                
                if curr == endGene: # endGene 까지 변형이 완료
                    return count
                
                for idx, char in enumerate(curr):
                    for mutate_gene in gene.values():
                        compare = list(curr)
                        if mutate_gene != char:
                            compare[idx] = mutate_gene
                            next = ''.join(compare)
                            if next in info and next not in visited:
                                que.append(next)
                                visited.add(next)
            count += 1
        return -1
                    