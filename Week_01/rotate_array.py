# timeout
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in xrange(k):
            temp = nums[-1]
            for m in range(len(nums), 0, -1):
                m = m - 1
                if m == 0:
                    nums[m] = temp
                else:
                    nums[m] = nums[m-1]


