class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        self.val = val
        self.nums = nums
        for num in nums:
            if num == self.val:
                self.nums.remove(self.val)
                print(nums)
