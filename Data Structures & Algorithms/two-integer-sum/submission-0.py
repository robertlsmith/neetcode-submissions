class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force Approach (O(n^2))
        # =============================
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j and nums[i] + nums[j] == target:
        #             return [i,j]

        # HashMap/Dictionary Approach (O(n))
        # =============================
        seen = {}

        for i, num in enumerate(nums):
            # print(i, num) --> i, nums[i]
            complement = target - num   # the number we need to have already seen because it's the value that would complete the pair
            
            if complement in seen:  # dict lookup = O(1), or instantaneous
                return [seen[complement], i]

            seen[num] = i   # store the value as key and index as value

            