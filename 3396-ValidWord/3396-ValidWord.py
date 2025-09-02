# Last updated: 9/2/2025, 1:40:52 PM
class Solution:
    def isValid(self, word: str) -> bool:
        vowels='aeiouAEIOU'
        v,c=0,0
        if len(word)<3:
            return False
        for char in word:
            if char.isalpha():
                if char in vowels:
                    v+=1
                else:
                    c+=1
            elif not char.isdigit():
                return False
        return v>0 and c>0
""""a3$e"
Output
true
Expected
false"""