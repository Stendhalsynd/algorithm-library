# ~ 09:30
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []
        info = {1: '(', 2: ')'}
        nums = [1, 2]
        combination = []
        
        def back(combination):
            
            if combination.count(1) == n and combination.count(2) == n:     # 충족 조건 : 여는 괄호와 닫는 괄호의 수가 모두 n
                parenthesis = ''.join([info[key] for key in combination])   # combination = [1, 1, 1, 2, 2, 2] 처럼 키만 갖고 있다.
                ans.append(parenthesis)
                
            else:
                for idx, num in enumerate(nums):
                    if not combination and num == 1:                        # combination 이 존재하지 않을때는 여는 괄호만 가능
                        back([num])
                    elif combination:                                       # combination 이 존재할때 
                        if num == 1 and combination.count(1) < n:           # 다음 괄호가 여는 괄호이고 여는 괄호가 아직 n 개가 아닐때
                            back(combination + [num])                       # 여는 괄호는 기존 조합에 그대로 추가하면 된다.
                        elif num == 2 and combination.count(2) < n:         # 다음 괄호가 닫는 괄호이고 닫는 괄호가 아직 n 개가 아닐때
                            if combination.count(1) > combination.count(2): # 닫는 괄호의 경우 기존 조합에 여는 괄호의 수가 닫는 괄호의 수보다 많아야 한다.
                                back(combination + [num])                   # 위의 조건을 만족할때 닫는 괄호를 조합에 추가한다.
                             
        back(combination)
        return ans
                