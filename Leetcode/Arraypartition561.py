class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        counter = 0
        for i in range(int(len(nums)/2)):
            counter+=min(nums[2*i],nums[2*i+1])
        return counter
        