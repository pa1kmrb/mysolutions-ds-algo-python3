#724. find pivot index 
##such that the sum on either side of the index (excluding the index) is equal

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        #Initialize left and right sum values
        left, right = 0, sum(nums)

        #start from left, loop through the list incrementing left sum and decrementing right sum
        for num in nums:
            right -= num
            if left == right:
                return nums.index(num)
            left += num
        
        #return -1 if no index exists such that the sum of elements on either side of the index is equal
        return -1
