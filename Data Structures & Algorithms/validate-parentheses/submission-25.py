class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        if s == "":
            return True

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
                continue
            if c == ']' and (stack == [] or stack[-1] != '['):
                return False
            if c == ')' and (stack == [] or stack[-1] != '('):
                return False
            if c == '}' and (stack == [] or stack[-1] != '{'):
                return False
            
            stack.pop()
            

        if stack == []:
            return True
        else:
            return False

