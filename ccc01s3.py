graph = {k: [] for k in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}

next = input()
while next != '**':
    graph[next[0]].append(next[1])
    graph[next[1]].append(next[0])
    next = input()

def dfs(graph):
    stack = ['A']
    visited = set()
    visited.add('A')

    while len(stack) > 0:
        next = stack.pop()
        if next == 'B':
            return True
        
        for x in graph[next]:
            if (x != None) and (x not in visited):
                stack.append(x)
                visited.add(x)
    return False

disconnecting = set()
checked = set()

for x in graph:
    for z in graph[x]:
        if x+z not in checked:
            graph[x].remove(z)
            graph[z].remove(x)

            if not dfs(graph):
                disconnecting.add(x+z)
            checked.add(x+z)
            checked.add(z+x)

            graph[x].append(z)
            graph[z].append(x)

for x in disconnecting:
    print(x)
print(f'There are {len(disconnecting)} disconnecting roads.')