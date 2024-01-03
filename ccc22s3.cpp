// TODO subtask #3 + #4

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    int N, M, K;
    cin >> N >> M >> K;

    K = K-N;

    vector<int> result;

    int value = 1;
    while (result.size() < N) {

        if (K != 0) {

            if (K < 0) {
                break;
            }

            if (result.size() >= K+1) {

                int temp = min(K, M-1);

                value = result[result.size()-temp-1];
                K -= temp;

            } else {

                value++;
                if (value > M) {
                    value -= M;
                }

                if (result.size() < M) {
                    K -= result.size();
                } else {
                    K -= (M-1);
                }

            }

        }
        
        result.push_back(value);

    }

    if (K != 0) {

        cout << -1 << endl;

    } else {

        for (int value : result) {
            cout << value << " ";
        }
        cout << endl;

    }

    return 0;

}