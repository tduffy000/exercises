#include <unordered_set>

int solution(vector<int> &A) {

    std::unordered_set<int> seen;

    for( int i = 1; i < A.size() + 2; ++i ) {
        seen.insert( i );
    }
    std::unordered_set<int>::iterator it;
    for( int j : A ) {
        it = seen.find( j );
        if( it != seen.end() )
            seen.erase( j );
    }
    return *seen.begin();
}
