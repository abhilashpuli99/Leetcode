# Last updated: 9/2/2025, 1:41:58 PM
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq={}
        for i in range(len(t)):
            freq[t[i]]=freq.get(t[i],0)+1
        for c in s:
            freq[c]-=1
            if freq[c]==0:
                del freq[c]

        return list(freq.keys())[0]