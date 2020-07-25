// idea here is to keep the lowest value allowed by max condition
// floating around as a constant (floor) and testing if something
// needs to be brought up only when it's updated (as opposed to all at once)
vector<int> solution(int N, vector<int> &A) {
    // write your code in C++14 (g++ 6.2.0)
    vector<int> counters (N, 0);
    int ceiling = 0;
    int floor = 0;

    for( vector<int>::const_iterator it = A.begin(); it != A.end(); ++it ) {

      int idx = *it - 1;
      if( *it <= N && *it != 0 ) {
        counters[idx] = std::max( counters[idx], floor ) + 1;
        ceiling = std::max( counters[idx], ceiling);
      } else {
        floor = std::max( ceiling, floor );
      }
    }

    // ensure all at least at floor
    for( int i = 0; i < counters.size(); ++i )
      counters[i] = std::max( counters[i], floor );

    return counters;

}
