#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int dfs(int current, int destination, int distance, vector<bool>& visited, vector<vector<pair<int,int>>>& graph) {
    if (current == destination) {
        return distance;
    }

    visited[current] = true;
    int dist = -1;

    for (auto next : graph[current]) {
        if (!visited[next.first]) {
            dist = max(dist, dfs(next.first, destination, distance + next.second, visited, graph));
        }
    }

    visited[current] = false;
    return dist;
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);

    vector<vector<pair<int,int>>> graph(n);

    for (int i = 0; i < m; i++) {
        int s, d, l;
        scanf("%d %d %d", &s, &d, &l);
        graph[s].push_back(make_pair(d, l));
    }

    vector<bool> visited(n, false);

    int dist = dfs(0, n - 1, 0, visited, graph);

    printf("%d", dist);

    return 0;
}
