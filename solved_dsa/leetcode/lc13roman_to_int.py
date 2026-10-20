# class Solution:
#     def romanToInt(self, s: str) -> int:
#         roman_mapping = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000
#         }
#         complement = {
#             "V": "I",
#             "X": "I",
#             "L": "X",
#             "C": "X",
#             "D": "C",
#             "M": "C"
#         }
#         complement_reduce = {
#             "V": 2,
#             "X": 2,
#             "C": 20,
#             "L": 20,
#             "D": 200,
#             "M": 200
#         }
#         converted_int = 0
#         prev = None
#         for c in s:
#             reduce = 0
#             if prev and complement.get(c, None) == prev:
#                 reduce = complement_reduce.get(c, 0)
                            
#             converted_int += roman_mapping.get(c, 0) - reduce
#             prev = c
            
#         return converted_int


class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total = 0
        for i in range(len(s)): 
            # if this numeral is smaller than the next, it's subtractive
            if i + 1 < len(s) and values[s[i]] < values[s[i+1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        return total

         
sol = Solution()
s = "IL"
print(sol.romanToInt(s))