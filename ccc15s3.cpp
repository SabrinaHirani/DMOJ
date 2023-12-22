#include <iostream>
#include <set>

using namespace std;

int main() {
    int G;
    cin >> G;

    int P;
    cin >> P;

    int count = 0;
    set<int> available;

    for (int i = 1; i <= G; i++) {
        available.insert(i);
    }

    for (int i = 0; i < P; i++) {
        int N;
        cin >> N;
        auto it  = available.upper_bound(N);
        if (it == available.begin()) {
            break;
        } else {
            available.erase(--it);
            count++;
        }
    }

    cout << count << endl;
    return 0;

}