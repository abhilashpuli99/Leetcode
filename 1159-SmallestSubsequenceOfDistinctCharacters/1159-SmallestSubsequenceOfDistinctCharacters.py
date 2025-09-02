# Last updated: 9/2/2025, 1:41:22 PM
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack=[]
        seen=dict()
        freq=dict()
        for char in s:
            freq[char]=freq.get(char,0)+1
        for char in s:
            freq[char]-=1
            if seen.get(char,False):
                continue
            while stack and stack[-1]>char and freq[stack[-1]]>0:
                seen[stack[-1]]=False
                stack.pop()
            stack.append(char)
            seen[char]=True
        return ''.join(stack)