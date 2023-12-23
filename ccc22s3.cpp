// TODO fix

#include <iostream>
#include <string>

using namespace std;

int main() {
    int N, M, K;
    cin >> N >> M >> K;

    K = K-N;

    int size = 0;

    string result;

    while (size < N) {

        int x = 1;
        int z = -1;
        while (true) {
            result += to_string(x)+' ';
            size++;
            x++;
            z += x;

            if (x > M || z >= K || size >= N) {
                cout << (x > M) << endl;
                cout << (z >= K) << endl;
                cout << (size >= N) << endl;
                break;
            }

        }

        K = max(0, K-x-1);

    }

    if (K != 0 || size != N) {
        cout << -1 << endl;
        cout << result << endl;
    } else {
        cout << result << endl;
    }

}