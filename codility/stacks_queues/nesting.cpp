#include <string>
#include <stack>

int solution(string &S) {
    // empty string check
    if( S.empty() )
        return 1;

    // check for matches using a stack
    std::stack<char> stack;
    for( std::string::iterator it = S.begin(); it != S.end(); ++it ) {
        if( *it == '(' )
            stack.push( *it );
        else if( *it == ')' ) {
            char c = stack.top();
            stack.pop();
            if( c != '(' )
                return 0;
        }
    }

    // is Stack empty? i.e. no leftovers
    if( !stack.empty() )
        return 0;
    else return 1;
}
