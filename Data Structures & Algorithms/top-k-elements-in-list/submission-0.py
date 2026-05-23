class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        ch_array = []

        for num in nums:
            num_freq[num] = 1 + num_freq.get(num, 0)

        for num, freq in num_freq.items():
            ch_array.append([freq, num])
        ch_array.sort()
        print(ch_array)

        return_list = []
        while len(return_list) < k:
            return_list.append(ch_array.pop()[1])

        return return_list
