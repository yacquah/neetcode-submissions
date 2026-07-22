class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       # create a dict to store key, val pairs
       # for str in strs:
       #    if soted(str) not dict:     
       #        add to the dict
       #        if str is same as the key, then add it as a value too
       #    add the actual str as a value, using the sorted as the key
        anagrams = {}

        for word in strs:
            sorted_str = "".join(sorted(word))
            if not sorted_str in anagrams:
                anagrams[sorted_str] = [word]
            else:
                anagrams[sorted_str] += [(word)]
        return list(anagrams.values())
