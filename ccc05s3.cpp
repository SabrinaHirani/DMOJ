// TODO complete

#include <iostream>
#include <vector>

int main() {
    int N;
    cin >> N;

    vector<vector<vector<int>>> operations;

    for (int i = 0; i < N; i++) {

        int r,c;
        cin >> r >> c;

        vector<vector<int>> operation(r,c);
        for (int j = 0; j < r; j++) {
            for (int k = 0; k < c; k++) {
                cin >> operation[r][c];
            }
        }

        operations.insert(operation);

    }

    vector<vector<int>> result = operations[0];

    for (int i = 0; i < operations.size(); i++) {

    }

    return 0;

}