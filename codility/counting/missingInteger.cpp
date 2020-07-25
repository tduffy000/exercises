// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;
#include <set>
#include <numeric>

int solution(vector<int> &A) {
    // write your code in C++14 (g++ 6.2.0)
    std::set<int> positiveInts;
    for( int el : A ) {
        if( el > 0 ) positiveInts.insert(el);
    }
    int x = 1;
    if( positiveInts.empty() ) return x;
    else {
        x = *positiveInts.rbegin();
        int ans = x + 1;
        int sum = std::accumulate(positiveInts.begin(), positiveInts.end(), 0);
        if( (x * (x + 1))/2 == sum ) return ans;

        while( x > 1 ) {
            if( positiveInts.find(x - 1) == positiveInts.end() )
                ans = x - 1;
            --x;
        }
        return ans;
    }

}
