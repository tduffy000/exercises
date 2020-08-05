# include<string>

class Solution {
    
private:
    string formatEmail(string addr) {
        int splitIdx = addr.find("@");
        string localName = addr.substr(0, splitIdx);
        string domain = addr.substr(splitIdx);
        int periodIdx = localName.find(".");
        while (periodIdx != std::string::npos) {
            localName.erase(periodIdx, 1);
            periodIdx = localName.find(".");
        }
        int plusIdx = localName.find("+");
        if (plusIdx != std::string::npos) {
            localName = localName.substr(0,plusIdx);
        }
        return localName+domain;
    }
    
    std::unordered_set<string> filterUnique(vector<string>& emails) {
        std::unordered_set<string> unique;
        for (const string addr : emails) {
            string formatted = formatEmail(addr);
            unique.insert(formatted);
        }
        return unique;
    }
    
    
public:
    int numUniqueEmails(vector<string>& emails) {
        std::unordered_set<string> uniqueAddresses = filterUnique(emails);
        return uniqueAddresses.size();
    }
};
