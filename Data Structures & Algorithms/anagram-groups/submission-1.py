class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}

        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            # use defaultdict(list) to simplify this block into:
            # grouped[tuple(count)].append(s)
            if tuple(count) not in grouped:
                grouped[tuple(count)] = [s]
            else:
                grouped[tuple(count)].append(s)
        
        return list(grouped.values())