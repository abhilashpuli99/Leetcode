# Last updated: 9/2/2025, 1:44:08 PM
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        curr_set=[]
        def backtrack(open,close):
            if len(curr_set)==2*n:
                result.append(''.join(curr_set))
                return
            if open<n:
                curr_set.append('(')
                backtrack(open+1,close)
                curr_set.pop()
            if close<open:
                curr_set.append(')')
                backtrack(open,close+1)
                curr_set.pop()
        backtrack(0,0)
        return result