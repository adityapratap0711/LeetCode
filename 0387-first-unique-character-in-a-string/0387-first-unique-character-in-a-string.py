class Solution:
    def firstUniqChar(self, s: str) -> int: 
        frq={}

        for i in s:
            if i not in frq:
                frq[i]=1
            else:
                frq[i]+=1

        for i in range(len(s)):
            if frq[s[i]]==1:
                return i


        return -1