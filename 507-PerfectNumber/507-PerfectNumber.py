# Last updated: 9/2/2025, 1:41:46 PM
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<=1:
            return False
        total=1
        i=2
        while i*i <=num:
            if num%i==0:
                total+=i
                if i!=num//i:
                    total+=num//i
            i+=1
        return True if total == num else False
        