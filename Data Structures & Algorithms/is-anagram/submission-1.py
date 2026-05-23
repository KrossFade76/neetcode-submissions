class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ch_balance = {}
        ch_actual = {}

        for i in range(len(s)):
            if s[i] in ch_balance:
                ch_balance[s[i]] += 1
            else:
                ch_balance[s[i]] = 1
            ch_actual[t[i]] = 1 + ch_actual.get(t[i], 0)
            
        return ch_balance == ch_actual