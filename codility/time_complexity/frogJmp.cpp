int solution(int X, int Y, int D) {
    long double float_jumps = (Y - X) / (D * 1.0);
    long int jumps = static_cast<int>( float_jumps );

    if( float_jumps - jumps == 0.0 ) {
        return jumps;
    } else {
        return ++jumps;
    }
}
