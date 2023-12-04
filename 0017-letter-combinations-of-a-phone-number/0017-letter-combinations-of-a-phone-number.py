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
        
        def backtracking():
            length = len(digits)
            total = list(product(['a','b','c','d','e','f','g',
                                       'h','i','j','k','l','m','n',
                                       'o','p','q','r','s','t','u',
                                       'v','w','x','y','z'], repeat=length))
            for string in total:
                if contain(string):
                    result.append(''.join(string))
            
        def contain(string):
            for idx, val in enumerate(list(string)):
                if val not in info[int(digits[idx])]:
                    return False
            return True
        
        backtracking()
        return result