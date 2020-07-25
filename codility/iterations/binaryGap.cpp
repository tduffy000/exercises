#include <math.h>
#include <vector>
#include <stack>
#include <deque>

vector<int> to_binary( int x ) {
    long int twoRaised = 0;
    int power = 31;
    vector<int> in_binary;

    while( power >= 0 ) {
        twoRaised = pow( 2, power );
        if( x - twoRaised >= 0 ) {
            in_binary.push_back( 1 );
            x -= twoRaised;
        } else {
            in_binary.push_back( 0 );
        }
        --power;
    }
    return in_binary;
}

int solution(int N) {

    std::stack<int> counter;
    vector<int> in_binary = to_binary( N );
    for( int i : in_binary ) {
        counter.push( i );
    }

    int maxCount = 0;
    int tmpCount = 0;
    bool headZero = true;
    while( !counter.empty() ) {
        int tmp = counter.top();
        counter.pop();
        if( tmp == 1 && !headZero) {
            if( tmpCount > maxCount )
                maxCount = tmpCount;
            tmpCount = 0;
        } else if ( tmp == 1 && headZero ) {
            tmpCount = 0;
            headZero = false;
        } else {
            ++tmpCount;
        }
    }
    return maxCount;
}
