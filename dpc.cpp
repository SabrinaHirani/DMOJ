#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<vector<int>> vacation(N, vector<int>(3));
    for (int i = 0; i < N; i++) {
        cin >> vacation[i][0] >> vacation[i][1] >> vacation[i][2];
    }

    vector<vector<int>> happiness(N, vector<int>(3, 0));
    happiness[0][0] = vacation[0][0];
    happiness[0][1] = vacation[0][1];
    happiness[0][2] = vacation[0][2];

    for (int i = 1; i < N; i++) {
        for (int j = 0; j < 3; j++) {
            for (int k = 0; k < 3; k++) {
                if (j != k) {
                    happiness[i][j] = max(happiness[i][j], vacation[i][j]+happiness[i-1][k]);
                }
            }
        }
    }

    int maximum = 0;
    for (int i = 0; i < 3; i++) {
        if (maximum < happiness[N-1][i]) {
            maximum = happiness[N-1][i];
        }
    }

    cout << maximum << endl;

    return 0;

}