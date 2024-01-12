#include <iostream>
#include <algorithm>
#include <limits>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> heights(N + 1, 0);

    for (int i = 1; i < N + 1; i++) {
        cin >> heights[i];
    }

    cout << "Heights: ";
    for (int i = 1; i < N + 1; i++) {
        cout << heights[i] << " ";
    }
    cout << endl;

    vector<vector<long long int>> scores(N + 1, vector<long long int>(N + 1, LLONG_MAX));

    for (int i = 1; i < N + 2; i++) {
        for (int j = 1; j < N + 2 - i; j++) {
            if (i == 1 || i == 2) {
                scores[i][j] = abs(heights[j + i / 2] - heights[j - (i - 1) / 2]);
            } else {
                scores[i][j] = scores[i - 2][j] + abs(heights[j + i / 2] - heights[j - (i - 1) / 2]);
            }
        }
    }

    cout << "Scores matrix:" << endl;
    for (int i = 1; i < N + 1; i++) {
        for (int j = 1; j < N + 1; j++) {
            cout << scores[i][j] << " ";
        }
        cout << endl;
    }

    cout << "Minimum symmetric values: ";
    for (int i = 1; i < N + 1; i++) {
        cout << *min_element(scores[i].begin(), scores[i].end()) << " ";
    }

    return 0;
}
