class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        std::vector<int> ans(A.size());
        int evenIdx = 0;
        int oddIdx = A.size() - 1;
        for (int n : A) {
            if (n % 2 == 0) {
                ans[evenIdx++] = n;
            } else {
                ans[oddIdx--] = n;
            }
        }
        return ans;
    }
};
