'''
-Given an array of integers, return indices(=index) of the two numbers 
such that they add up to a specific target.
-Each input will have exactly ONE solution
-You may not use the same element twice
'''
### Nature: locate the index of the answer --> which leads to map

## Time: O(n), Space: O(n) --> the numMap's size equals to the input array

# Two-pass map solution
def twoSumTwoPass(nums, target):
    # The dictionary to store each number's index
    numMap = {}
    # O(1)
    N = len(nums)

    # O(n)
    for i in range(N):
        numMap[nums[i]] = i
    # O(n)
    for i in range(len(nums)):
        # comp = complement: 补充
        comp = target - nums[i]
        if comp in numMap.keys() and numMap[comp] != i:
            return [i, numMap[comp]]
    return [] # edge case
   

# One-pass map solution: there is no need to start the search
# after the map is built, we can do them in the same time.
# Once a match is found, we return it and stop the function
def twoSumOnePass(nums, target):
    numMap = {}
    N = len(nums)
    for i in range(N):
        comp = target - nums[i]
        if comp in numMap and numMap[comp] != i:
            return [comp, i]
        else:
            numMap[nums[i]] = i
    return [] # edge case

# Using 'enumerate'
def twoSumEnumerate(nums, target):
    numMap = {}
    for i, num in enumerate(nums):
        comp = target - num
        if comp not in numMap:
            numMap[num] = i
        else:
            return [numMap[comp], i]
