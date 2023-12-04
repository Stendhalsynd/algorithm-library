# hash table, string, backtracking
# ~ 08: 45
from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if not digits:
            return result
        
        info = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'],
                5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'],
                8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
        
        # expected : 22 -> ["aa","ab","ac","ba","bb","bc","ca","cb","cc"]
        # combinations : iterable 객체에서 r 개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우 (조합)
          # 22 -> ["ab","ac","bc"]
        # combinations_with_replacement : combinations 와 같으나 원소를 중복해서 뽑는다.
          # 22 -> ["aa","ab","ac","bb","bc","cc"]
        # product : permutations 와 같이 리스트와 같은 iterable 객체에서 r 개의 데이터를 뽑아 일렬로 나열하는 모든 경우 (순열)를 계산한다. 단, 중복해서 뽑는다.
        def backtracking():
            length = len(digits)
            total = list(product(['a','b','c','d','e','f','g',
                                  'h','i','j','k','l','m','n',
                                  'o','p','q','r','s','t','u',
                                  'v','w','x','y','z'], repeat=length))
            for string in total:
                if contain(string): # 유망하면 결과 배열에 append
                    result.append(''.join(string)) 
            
        def contain(string): # 유망조건
            for idx, val in enumerate(list(string)):
                if val not in info[int(digits[idx])]:
                    return False
            return True
        
        backtracking()
        return result