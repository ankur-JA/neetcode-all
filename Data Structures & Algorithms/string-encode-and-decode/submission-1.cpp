class Solution {
public:

    string encode(vector<string>& strs) {
        string s = "";
        for(string str : strs){
            s += str + "\xC0";
        }
        return s;
    }

    vector<string> decode(string s) {
        int n = s.size();
        vector<string> res;

        string temp = "";
        for(char c : s){
            
            if(c == '\xC0'){
                res.push_back(temp);
                temp = "";
            }else{
                temp = temp + c;
            }
        }

        return res;
    }
};
