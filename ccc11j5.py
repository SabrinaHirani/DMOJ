# TODO revisit after doing more dp

def dfs(next, n, graph, count):
    sum = len(graph[next])
    for i in range(len(graph[next])):
        if graph[next][i] in graph:
            sum += dfs(graph[next][i], n, graph, count)
    if next != n:
        count[0] -= (2**(n-2-i)-2**(sum))
        print(count)
    return sum

n = int(input())

graph = {}

for i in range(1, n):
    x = int(input())
    if x not in graph:
        graph[x] = []
    graph[x].append(i)

count = [2**(n-1)]
print(count)
dfs(n, n, graph, count)
print(count[0])