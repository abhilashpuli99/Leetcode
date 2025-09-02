# Last updated: 9/2/2025, 1:42:56 PM
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def helper(a,b,opr):
            if opr == '+':
                return int(a)+int(b)
            elif opr == '-':
                return int(b)-int(a)
            elif opr == '*':
                return int(a)*int(b)
            elif opr == '/':
                return int(int(b)/int(a))
        stack=[]
        oprs=['+','-','*','/']
        for val in tokens:
            if val in oprs and stack:
                first=stack.pop()
                second=stack.pop()
                stack.append(str(helper(first,second,val)))
            else:
                stack.append(val)
        return int(stack[0])
        