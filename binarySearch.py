class BinarySearch:
    
    tests = [{
                'input':
                {
                    'nums':[0,1,3,5,6,9,10],
                    'target': 9
                },
                'output': 5
				
            },
            {
                'input':
                {
                    'nums':[1,2,4,6,8,12,13],
                    'target': 10
                },
                'output': -1
				
            }
            ]

    def searchnum(nums, target) -> int:
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
    
    for test in tests:
        result = searchnum(**test['input'])
        if (result == test['output']):
            print ('Success\n Input: {input}\n Expected Output: {output}\n Actual Output: {}'.format(result,**test))
        else:
            print ('Fail')
    
