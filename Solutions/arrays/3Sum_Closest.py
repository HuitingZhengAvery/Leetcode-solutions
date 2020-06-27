'''
Given an array nums of n integers and an integer target, 
find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. 
You may assume that each input would have exactly one solution.
'''

### Nature: Find the combination of three, whose sum is closest to the
### target. Naively, there are O(n^3) possible combinations, but if
### we fix one number and do two pointers for the rest, it will be decreased to O(n^2)

## Time: O(n^2), Space: from O(logn) to O(n), depending on the implementation of 
# the sorting algorithm.

def threeSumClosest(nums, target):
    nums.sort()
    diff = float('inf')
    res = None
    # To slightly improve the performance by excluding special cases
    if sum(nums[:3]) >= target:
        return sum(nums[:3])
    # fix one number first
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        comp = target - nums[i]
        j, k = i+1, len(nums)-1
        while j < k:
            # perfect case
            if nums[j] + nums[k] == comp:
                return target
            # current difference
            temp = abs(nums[j] + nums[k] - comp)
            # Update difference if necessary
            if temp < diff:
                diff = temp
                res = nums[i] + nums[j] + nums[k]
            # Move the two pointers
            if nums[j] + nums[k] < comp:
                j += 1
            else:
                k -= 1                
    return res