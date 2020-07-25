// you can use includes, for example:
// #include <algorithm>

void rotate( vector<int> &A ) {
    int last = A[A.size() - 1];
    int tmp = A[0];
    for(int i = 1; i < A.size(); ++i) {
        int localTmp = A[i];
        A[i] = tmp;
        tmp = localTmp;
    }
    A[0] = last;
}

vector<int> solution(vector<int> &A, int K) {
    // write your code in C++14 (g++ 6.2.0)
    int len = A.size();
    if( len == 0 || len == 1 || K % len == 0 )
        return A;

    int rotations_remaining = K % len;
    while(rotations_remaining > 0) {
        rotate(A);
        --rotations_remaining;
    }
    return A;
}
