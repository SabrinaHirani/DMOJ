#include <iostream>
#include <algorithm>
#include <climits>
#include <cmath>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> heights(N, 0);

    for (int i = 0; i < N; i++) {
        cin >> heights[i];
    }

    vector<vector<long long int>> scores1(N, vector<long long int>(N, LLONG_MAX));
    vector<vector<long long int>> scores2(N, vector<long long int>(N, LLONG_MAX));

    for (int i = 0; i < N/2+1; i++) {
        for (int j = i; j < N-i; j++) {
            if (i <= 0) {
                scores1[i][j] = abs(heights[j+i] - heights[j-i]);
            } else {
                scores1[i][j] = scores1[i-1][j] + abs(heights[j+i] - heights[j-i]);
            }
        }
    }

    for (int i = 0; i < N/2+1; i++) {
        for (int j = i; j < N-i-1; j++) {
            if (i <= 0) {
                scores2[i][j] = abs(heights[j+i+1] - heights[j-i]);
            } else {
                scores2[i][j] = scores2[i-1][j] + abs(heights[j+i+1] - heights[j-i]);
            }
        }
    }

    for (int i = 0; i < N/2; i++) {
        cout << *min_element(scores1[i].begin(), scores1[i].end()) << " ";
        cout << *min_element(scores2[i].begin(), scores2[i].end()) << " ";
    }
    if (N%2 == 1) {
        cout << *min_element(scores1[N/2].begin(), scores1[N/2].end()) << endl;
    }

    return 0;
}
