class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ch_balance = {}
        for ch in s:
            if ch in ch_balance:
                ch_balance[ch] += 1
            else:
                ch_balance[ch] = 1
        
        ch_actual = {}
        for ch in t:
            if ch in ch_actual:
                ch_actual[ch] += 1
            else:
                ch_actual[ch] = 1
            
        return ch_balance == ch_actual