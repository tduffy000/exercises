
int solution(vector<int> &A) {

    int eastBoundPassed = 0;
    int pairOfPassingCars = 0;

    for(int carDirection : A) {
        if (carDirection == 0) {
            eastBoundPassed++;
        } else {
            pairOfPassingCars += eastBoundPassed;
        }
        if (pairOfPassingCars > 1000000000) return -1;
    }
    return pairOfPassingCars;
}
