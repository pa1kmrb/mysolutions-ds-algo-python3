class BinarySearch:

		test = {
						'input':
						{
							'nums' : [-1,0,3,5,9,12]
							'target' : 9
						}
						'output': 4
						}
    def searchnum(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        
        #iterative approach
        while lo <= hi:
            mid = lo + (hi-lo)//2
            
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                lo = mid + 1
            elif target < nums[mid]:
                hi = mid - 1
        
        return -1
      
      def locate_num -> None:
        result = searchnum(**test['input'])
        if (result == test['output']):
            print ('Success\n Input: {}\n Output: {}'.format(**test['input'],result))
        elif (result == -1):
            print ('Fail\n Input: {}\n Output: {}'.format(**test['input'],result))
        
