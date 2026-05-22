class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valid_pair = []
        index_array = {}

        for i in range(len(nums)):
            index_array[nums[i]] = i

        for j in range(len(nums)):
            difference = target - nums[j]
            if difference in index_array and j != index_array[difference]:
                valid_pair.append(j)
                valid_pair.append(index_array[difference])
                break

        return valid_pair