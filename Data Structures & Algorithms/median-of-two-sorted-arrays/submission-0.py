class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        i = 0
        j = 0
        result = []

        while(i < len(nums1) and j < len(nums2)):
            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i = i + 1
            else:
                result.append(nums2[j])
                j = j + 1
        
        result.extend(nums1[i:])
        result.extend(nums2[j:])

        n = len(nums1) + len(nums2)

        if(n%2 == 1):
            return result[n//2]
        else:
            return ( ( result[n//2] + result[n//2 - 1] ) / 2)
