class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = 0
        for q in xrange(len(nums)):
            if nums[p] != nums[q]:
                nums[p+1] = nums[q]
                p = p + 1
        return p + 1

