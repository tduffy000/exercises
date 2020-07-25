#include <unordered_set>

int solution(vector<int> &A) {

    std::unordered_set<int> unique;
    for( int i : A ) {
        unique.insert(i);
    }

    return unique.size();
}
