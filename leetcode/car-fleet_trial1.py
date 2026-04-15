class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort()
        print(pairs)
        # 0 3 5 8 10
        # 1 1 1 4 2 
        sol = 0
        last_time = float('inf')
        while pairs and p < positions[stack[-1]]:
            p, s =pairs.pop()
            
            time = (target - p)//speed
            
            stack.append(i)
            
            
