# Last updated: 9/2/2025, 1:40:56 PM
class Solution:
    def finalString(self, s: str) -> str:
        new_str=''
        for i in range(len(s)):
            if s[i]=='i':
                new_str=new_str[::-1]
            else:
                new_str+=s[i]
        return new_str