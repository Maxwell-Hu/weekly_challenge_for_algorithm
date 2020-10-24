class Solution {
public:
    int findString(vector<string>& words, string s) {
        for(int i=0; i<words.size(); ++i) {
            if(words[i] == s) return i;
        }
        return -1;
    }
};
