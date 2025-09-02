# Last updated: 9/2/2025, 1:43:48 PM
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        re=len(matrix)
        ce=len(matrix[0])
        rb=0
        cb=0
        res=[]
        """if len(matrix)==1:
            return matrix[0]
        elif len(matrix[0])==1:
            return [item for row in matrix for item in row]"""
        total=re*ce
        while(len(res)<total):
            
            """if len(res)==(len(matrix)*len(matrix[0])):
                break"""
            for i in range(cb,ce):
                if len(res)<total:
                    res.append(matrix[rb][i])
            rb+=1
            #if rb<re:
            for i in range(rb,re):
                if len(res)<total:
                    res.append(matrix[i][ce-1])
            ce-=1
            #if rb<re:
            for i in range(ce-1,cb-1,-1):
                if len(res)<total:
                    res.append(matrix[re-1][i])
            re-=1
            #if cb<ce:
            for i in range(re-1,rb-1,-1):
                if len(res)<total:
                    res.append(matrix[i][cb])
            cb+=1
        return res

            

        