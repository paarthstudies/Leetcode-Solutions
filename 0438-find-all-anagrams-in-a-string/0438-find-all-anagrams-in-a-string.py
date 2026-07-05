class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        count = {}
        for char in p:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1
        l = len(p)
        freq = {}
        for char in range(l):
            x = s[char]
            if x not in freq:
                freq[x] = 1
            else:
                freq[x] += 1
        mylist = []
        if freq == count:
            mylist.append(0)
        after = l 
        temp = 0
        while after < len(s):
            freq[s[temp]] -= 1
            if freq[s[temp]] == 0:
                freq.pop(s[temp])
            temp += 1
            if s[after] not in freq :
                freq[s[after]] = 1
            elif s[after] in freq:
                freq[s[after]] += 1
            
            if count == freq:
                mylist.append(temp)
            after += 1
        return mylist