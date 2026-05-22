class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}

        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            if tuple(count) not in grouped:
                grouped[tuple(count)] = [s]
            else:
                grouped[tuple(count)].append(s)
        
        return list(grouped.values())