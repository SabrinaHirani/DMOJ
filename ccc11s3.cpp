#include <iostream>
#include <cmath>

using namespace std;

string isCrystal(int m, int x, int y, int pattern[5][5]) {
    if (m <= 1) {
        if (pattern[y][x]) {
            return "crystal";
        } else {
            return "empty";
        }
    } else {
        int d = pow(5, (m-1));
        if (pattern[(y/d)][(x/d)]) {
            return "crystal";
        } else if (!pattern[((y/d)-1)][(x/d)]) {
            return "empty";
        } else {
            return isCrystal(m-1, x%d, y%d, pattern);
        }
    }
}

int main() {
    int T;
    cin >> T;

    for (int t = 0; t < T; t++) {
        int m, x, y;
        cin >> m >> x >> y;

        int pattern[5][5] = {
            {0, 1, 1, 1, 0},
            {0, 0, 1, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0}
        };

        cout << isCrystal(m, x, y, pattern) << endl;
    }

    return 0;
}
