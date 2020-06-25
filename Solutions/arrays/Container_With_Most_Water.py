'''
Given n non-negative integers a1, a2, ..., an, 
where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
'''

### Nature: The area between ANY two lines is decided by the SHORTER line.
### Central logic: two pointers approach(sliding window): we only move the shorter
### line to see if there is any longer line to increase the area

## Time: O(n), Space: O(1) --> we need fixed number of variables

def maxArea(height):
    maxArea, i, j = 0, 0, len(height) - 1
    while i < j:
        # Update max
        maxArea = max((j - i) * min(height[i], height[j]), maxArea)

        # Only move the shorter line
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return maxArea