class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0  
        right = len(nums) - 1
        counter = 0 
        while left < right:
            while nums[right] == val:
                right -= 1
            if nums[left] == val:
                counter += 1
                nums[right], nums[left] = nums[left], nums[right]
                right -=1
            left += 1
        
        return len(nums) - counter
        