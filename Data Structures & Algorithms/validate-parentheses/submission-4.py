class Solution:
    def isValid(self, s: str) -> bool:
        valid = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char not in valid:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != valid[char]:
                        return False
        return not stack