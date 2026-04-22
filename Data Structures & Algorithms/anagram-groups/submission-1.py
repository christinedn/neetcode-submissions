class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        # go through each string
        for s in strs:
        # create count with index 0 ... 25. each index represents a letter in the alphabet
            count = [0] * 26
        # iterate through each char of current string and increment the count 
            for c in s:
                i = ord(c) - ord('a')
                count[i] += 1
        # add count as key to res, and append the s. must convert to tuple so it can be used as a key
            d[tuple(count)].append(s)
        # return d.values as a list 
        return list(d.values())
        