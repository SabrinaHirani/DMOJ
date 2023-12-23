#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, W;
    cin >> N >> W;

    vector<long long int> weight(N);
    vector<long long int> value(N);

    for (int i = 0; i < N; i++) {
        cin >> weight[i] >> value[i];
    }

    vector<long long int> dp(W+1);
    for (int i = 0; i < N; i++) {
        for (int j = W; j > weight[i]-1; j--) {
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i]);
        }
    }

    cout << dp[W] << endl;


}