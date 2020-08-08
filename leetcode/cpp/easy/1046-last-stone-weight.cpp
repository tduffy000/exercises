#include <queue>
#include <vector>

class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        std::priority_queue<int> q;
        for (int stone : stones) {
            q.push(stone); 
        }
        while (q.size() > 1) {
            int largest = q.top();
            q.pop();
            int secondLargest = q.top();
            q.pop();
            if (largest == secondLargest) {
                continue;
            } else {
                q.push(largest - secondLargest);
            }
        }
        return q.empty() ? 0 : q.top();
    }
};