#include <math.h>

int solution(int A, int B, int K) {

    int upperBoundDivided = floor(B / K);
    int lowerBoundDivided = floor(A / K);
    int inRangeMultiples = upperBoundDivided - lowerBoundDivided;
    if(A % K == 0) inRangeMultiples++;
    return inRangeMultiples;
}
