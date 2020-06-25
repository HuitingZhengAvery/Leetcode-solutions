'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
'''

### Nature: the meaning of MEDIAN, is that, the number of elements less than it, 
### is equal to that is more than it.
### len(left) == len(right)
### It is NOT important that if these two parts are sorted.

## Time: O(log(min(m, n))), Space: O(1) --> we need fixed number of variables

# Iterative approach
# Central logics: there exists i, j where i+j = (m+n+1) // 2 AND
# A[i-1] (leftmax of A) < B[j] (rightmin of B) AND B[j-1] < A[i]
# (in general, all left <= all right)
def findMedianSortedArrays(nums1, nums2):
    m, n = len(nums1), len(nums2)
    # To ensure j will not be negative
    if m > n:
        m, n = n, m
        nums1, nums2 = nums2, nums1

    # (m+n+1) plus 1 makes sure i & j are the minimums of the right part, AND
    # that j-1 (which is left max) will not be negative
    imin, imax, half = 0, m, (m+n+1) / 2
    while imin <= imax: # This will directly handle edge cases like len(A) == 0 etc
        i = (imin+imax) / 2
        j = half - i

        # case one: i hasn't exceeded array 1 and is too small
        if i < m and nums2[j-1] > nums1[i]:
            imin = i+1
        # case two: i-1 hasn't exceeded the smallest and i is too big
        elif i > 0 and nums1[i-1] > nums2[j]:
            imax = i-1
        # case three: i is perfect
        else:
            # edge case 1:
            # all nums in nums1 is bigger than nums2
            if i == 0:
                max_of_left = nums2[j-1] # j-1 >= 0 is ensured
            # edge case 2:
            # the opposite, AND m==n or m=n-1
            elif j == 0:
                max_of_left = nums1[m-1]
            # general case:
            else:
                max_of_left = max(nums1[i-1], nums2[j-1])
                
            if (m+n) % 2 == 1:
                return max_of_left
            # edge case: when A[i] would be out of index bound
            if i == m:
                min_of_right = nums2[j]
            # edge case: when B[j] would be out of index bound
            elif j == n:
                min_of_right = nums1[i]
            else:
                min_of_right = min(nums1[i], nums2[j])
            return (max_of_left + min_of_right) / 2.0 
