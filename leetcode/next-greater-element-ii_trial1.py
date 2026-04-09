class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        stack = []
        matchings = {}
        arr = nums
        nums = nums + nums
        for i in range(len(nums)):
            while stack and nums[i] > stack[-1]:
                num = stack.pop()
                matchings[num] = nums[i]


            stack.append(nums[i])

        return [matchings.get(n, -1) for n in arr]