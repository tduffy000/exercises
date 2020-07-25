#include <unordered_set>

int solution(vector<int> &A) {

    std::unordered_set<int> seen;

    for( int i : A ) {
        std::unordered_set<int>::iterator it = seen.find( i );
        if( it != seen.end() ) {
            seen.erase( i );
        } else {
            seen.insert( i );
        }

    }

    return *seen.begin();
}
