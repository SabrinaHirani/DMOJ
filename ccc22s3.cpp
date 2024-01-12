#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    int N, M;
    long long int K;
    cin >> N >> M >> K;

    K = K-N;

    int x = 1;
    vector<int> result;

    while (result.size() < N) {

        if (K < 0) {
            break;
        } else if (result.size() >= M || result.size() >= K+1) {

            if (K <= M-1) {
                result.push_back(result[result.size()-1-K]);
                K = 0;
            } else {
                result.push_back(result[result.size()-1-(M-1)]);
                K -= M-1;
            }

        } else {

            if (K-(x-1) >= 0) {
                result.push_back(x);
                K -= x-1;
                x += 1;
            } else {
                break;
            }
        }

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