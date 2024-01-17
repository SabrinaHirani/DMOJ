#include <iostream>
#include <vector>

using namespace std;

int main() {

    cin.tie(0);
    cin.sync_with_stdio(0);

    int N;
    cin >> N;

    vector<int> number(N, 0);
    vector<int> weight(N, 0);
    int total = 0;

    for (int i = 0; i < N; i++) {
        int k, c;
        cin >> k >> c;
        number[i] = k;
        weight[i] = c;
        total += k*c;
    }

    vector<bool> dp(total, false);
    vector<int> amount(total, 0);
    dp[0] = true;

    for (int i = 0; i < N; i++) {
        for (int j = weight[i]; j <= total/2+1; j++) {
            if (!dp[j] && dp[j-weight[i]] && amount[j-weight[i]] < number[i]) {
                dp[j] = true;
                amount[j] = amount[j-weight[i]]+1;
            }
            amount[j-weight[i]] = 0;
        }
    }

    int minimum = total;
    for (int i = total/2; i >= 0; i--) {
        if (dp[i]) {
            minimum = abs(total-2*i);
            break;
        }
    }

    cout << minimum << endl;
    return 0;
}
