class Solution:
    def isValid(self, s: str) -> bool:
        ## "(,), {,}, [,]"
        if len(s) < 2:
            return False
        
        valid = "({["

        stack = []
        for c in s:
            if c in valid:
                stack.append(c)
            else:
                if not stack:
                    return False
                if c== ")" and stack[-1] == "(":
                    stack.pop()
                elif c== "]" and stack[-1] == "[" :
                    stack.pop()
                elif c== "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        return not stack
        
