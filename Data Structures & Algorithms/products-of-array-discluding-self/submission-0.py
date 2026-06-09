class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result_array = []
        curr_num = 0

        while curr_num < len(nums):
            result = 1
            for i in range(len(nums)):
                if i != curr_num:
                    result *= nums[i]
            result_array.append(result)
            curr_num += 1

        return result_array