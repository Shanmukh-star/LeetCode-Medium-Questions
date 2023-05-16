class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l =s.length();
        int j,k,p,maxi,init;
        set<char> se;
        maxi=0;
        for(j=0;j<l;j++)
        {
            for(k=j;k<l;k++)
            {
                init=se.size();
                se.insert(s[k]);
                if(se.size()==init)
                {
                    if(maxi<se.size())
                    {
                        maxi=se.size();
                    }
                    break;
                }
                else if (k==l-1)
                {
                    if(maxi<se.size())
                    {
                        maxi=se.size();
                    }
                }
            }
            se.clear();
        }
        return maxi;
    }
};
