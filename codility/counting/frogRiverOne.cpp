#include <unordered_set>

int solution(int X, vector<int> &A) {
    // write your code in C++14 (g++ 6.2.0)

    std::unordered_set<int> leaves;
    int ans = -1;
    for( int i = 0; i < A.size(); ++i ) {
        if( A[i]  <= X ) leaves.insert(A[i]);
        if( leaves.size() == X ) {
            ans = i;
            break;
        }
    }
    return ans;
}
