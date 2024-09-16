from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print(nums)
        print(target)

        indexes = []
        index_dict = {}

        for index, num in enumerate(nums):
            difference = target - num
            if difference in index_dict:
                indexes.append(index)
                indexes.append(index_dict[difference])
                return indexes
            
            index_dict[num] = index 

        return indexes
