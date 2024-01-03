#include <cstdio>
#include <vector>

using namespace std;

int main() {
    int R, C;
    scanf("%d %d", &R, &C);

    int K;
    scanf("%d", &K);

    vector<vector<bool>> illegal(R + 1, vector<bool>(C + 1, false));
    for (int i = 0; i < K; i++) {
        int r, c;
        scanf("%d %d", &r, &c);
        illegal[r][c] = true;
    }

    vector<vector<int>> dp(R + 1, vector<int>(C + 1, 0));
    dp[1][1] = 1;

    for (int i = 1; i <= R; i++) {
        for (int j = 1; j <= C; j++) {
            if (!illegal[i][j]) {
                dp[i][j] += dp[i - 1][j] + dp[i][j - 1];
            }
        }
    }

    printf("%d\n", dp[R][C]);

    return 0;
}
