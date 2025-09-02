# Last updated: 9/2/2025, 1:40:42 PM
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        len_fruits=len(fruits)
        for i in fruits:
            for j in range(len(baskets)):
                if i<=baskets[j]:
                    len_fruits-=1
                    baskets[j]=float('-inf')
                    break
        return len_fruits