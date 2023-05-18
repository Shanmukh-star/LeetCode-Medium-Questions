class Solution:
    def longestPalindrome(self, s: str) -> str:
        l=len(s)
        li=[]
        maxi=0
        req=''
        for j in range(l):
            for k in range(j,l):
                if(s[j]==s[k]):
                    if(s[j:k+1]==s[j:k+1][::-1]):
                        if(maxi<k-j+1):
                            maxi=k-j+1
                            req=s[j:k+1]
        return req
