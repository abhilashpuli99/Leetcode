# Last updated: 9/2/2025, 1:41:35 PM
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #---# use stack for opt sol-----
        stack = []
        for asteroid in asteroids:
            while stack and asteroid<0 and stack[-1]>0:
                if stack[-1] < abs(asteroid):
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        return stack
            
            
                        
            
        

        