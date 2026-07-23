class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initialize a dictionary
        # since each anagram will have the same letter frequency
        # use letter frequency for each word
        #   to find the frequency
        #       first set a count = 26 zeros, each for each char 
        # for each char in each s, find count[ord(char)-ord(a)] += 1
        # then store each count list as the key and assign the word as the value
        # return a list of all the values
        anagrams = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord("a")] += 1
            
            anagrams[tuple(count)].append(s)    
        return list(anagrams.values())