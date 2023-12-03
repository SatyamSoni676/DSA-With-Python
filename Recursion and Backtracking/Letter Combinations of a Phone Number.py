#https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digit_mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        def backtrack(index, digit):
            if len(digit) == len(digits):
                res.append(digit)
                return
            for char in digit_mapping[digits[index]]:
                backtrack(index+1, digit+char)
            
        if digits:
            backtrack(0, "")
        
        return res
