class Solution:

    def encode(self, strs: List[str]) -> str:
        # initialize a string to store strings and their len
        res = ""
        # store in the form "len(str)#str"
        for s in strs:
            res += str(len(s)) + "#" + s
        # return the result
        return res
        

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j+1+length
        return res