#include <unordered_set>

int solution(vector<int> &A) {
    // write your code in C++14 (g++ 6.2.0)

    std::unordered_set<int> in_range;
    for( int i = 1; i <= A.size() ; ++i ) {
        in_range.insert( i );
    }

    std::unordered_set<int>::iterator it;
    for( int j : A ) {
        it = in_range.find( j );
        if( it != in_range.end() ) {
            in_range.erase( j );
        } else {
            return 0;
        }
    }
    return 1;
}
