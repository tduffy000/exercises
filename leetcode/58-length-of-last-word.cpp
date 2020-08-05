# include <string>

class Solution {
public:
    int lengthOfLastWord(std::string s) {
        int length = 0;
        bool haveStarted = false;
        for (auto it = s.crbegin(); it != s.crend(); ++it) {
            if (*it != ' ') {
                haveStarted = true;
                length++;
            }
            if (*it == ' ' && !haveStarted) continue;
            if (*it == ' ' && haveStarted) break;
        }
        return length;
    }
};