#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, M, K;
    cin >> N >> M >> K;

    vector<vector<long long int>> cake(N, vector<long long int>(M));
    for (int i = 0; i < K; i++) {
        int A, B, C, D;
        cin >> A >> B >> C >> D;

        cake[A-1][B-1]++;
        if (C < N) {
            cake[C][B-1]--;
        }
        if (D < M) {
            cake[A-1][D]--;
        }
        if (C < N && D < M) {
            cake[C][D]++;
        }

    }

    for (int i = 0; i < N; i++) {
        for (int j = 1; j < M; j++) {
            cake[i][j] += cake[i][j-1];
        }
    }

    for (int i = 1; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cake[i][j] += cake[i-1][j];
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 1; j < M; j++) {
            cake[i][j] += cake[i][j-1];
        }
    }

    for (int i = 1; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cake[i][j] += cake[i-1][j];
        }
    }

    int Q;
    cin >> Q;

    for (int i = 0; i < Q; i++) {
        int A, B, C, D;
        cin >> A >> B >> C >> D;

        long long int total = cake[C-1][D-1];
        if (A > 1) {
            total -= cake[A-2][D-1];
        }
        if (B > 1) {
            total -= cake[C-1][B-2];
        }
        if (A > 1 && B > 1) {
            total += cake[A-2][B-2];
        }
        cout << total << endl;

    }

    return 0;
}
