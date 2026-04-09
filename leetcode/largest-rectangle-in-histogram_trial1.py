class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        result = 0
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                popped_idx = stack.pop()
                height = heights[popped_idx]
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
            
                result = max(result, height*width)

            stack.append(i)
        
        return result