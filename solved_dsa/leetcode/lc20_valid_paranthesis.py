
class Solution:
    def isValid(self, s: str) -> bool:
        openers = {"[", "{", "("}
        closers = {"]": "[", "}": "{", ")": "("}
        openers_recorded = {}
        openers_arr = []
        for paranthesis in s:
            if paranthesis in openers:
                openers_recorded[paranthesis] = openers_recorded.get(paranthesis, 0) + 1
                openers_arr.append(paranthesis)
            else:
                if closers[paranthesis] == openers_arr[len(openers_arr) - 1]:
                    openers_arr = openers_arr[:-1]
                else:
                    return False
                
        return True  
    
sol = Solution()
s = "{[({{{}{}()[({[()({)]})]}})]}"
print(sol.isValid(s))