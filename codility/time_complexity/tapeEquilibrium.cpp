#include <cmath>

// Complexity: O(n)

int solution(vector<int> &A) {

    int right_sum = 0;
    for( int i = 1; i < A.size(); ++i ) {
        right_sum += A[i];
    }
    int left_sum = A[0];

    int min_diff = 100001;
    for( int j = 1; j < A.size(); ++j ) {
        if( abs(right_sum - left_sum) < min_diff )
            min_diff = abs(right_sum - left_sum);

        left_sum += A[j];
        right_sum -= A[j];
    }

    return min_diff;
}
