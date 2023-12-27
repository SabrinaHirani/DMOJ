#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

int main() {
    int dist;
    cin >> dist;

    int n;
    cin >> n;
    vector<int> stroke;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        stroke.push_back(x);
    }
    sort(stroke.rbegin(), stroke.rend());

    vector<int> distance(dist+1, -1);
    distance[0] = 0;

    queue<int> q;
    q.push(0);

    while (!q.empty()) {
        int next = q.front();
        q.pop();

        for (int i = 0; i < stroke.size(); i++) {
            if (next + stroke[i] <= dist && (distance[next + stroke[i]] == -1 || distance[next] + 1 < distance[next + stroke[i]])) {
                distance[next + stroke[i]] = distance[next] + 1;
                q.push(next + stroke[i]);
            }
        }
    }

    if (distance[dist] == -1) {
        cout << "Roberta acknowledges defeat." << endl;
    } else {
        cout << "Roberta wins in " << distance[dist] << " strokes." << endl;
    }

    return 0;
}
