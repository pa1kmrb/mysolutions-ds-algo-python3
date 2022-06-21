from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        #Initialization
        sum = 0
        outList = []

        for num in nums:
            sum = sum + num
            outList.append(sum)
        return outList