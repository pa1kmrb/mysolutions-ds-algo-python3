#724. find pivot index 
##such that the sum on either side of the index (excluding the index) is equal

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        #Initialize left and right sum values
        left, right = 0, sum(nums)

        #start from left, loop through the list incrementing left sum and decrementing right sum
        #enumerate list to have incremental index in case of duplicate values
        for idx, num in enumerate(nums):
            right -= num
            if left == right:
                return idx
                #below returns the first occurrence of element if the list has repeating elements - not correct
                #[-1,-1,-1,-1,-1,0] expected value 2, but below statement returns 0 (first occurrance)
                ##return nums.index(num)##
            left += num
        
        #return -1 if no index exists such that the sum of elements on either side of the index is equal
        return -1
