graph = {'A':['B','C','D'],
        'B':['E','A'],
        'E':['B','C'],
        'C':['A','D','E'],
        'D':['A','C'],
        }
visited =set()

def dfs(visited,graph,root):
    if root not in visited:
        print(root)
        visited.add(root)
        for neighbour in graph[root]:
            dfs(visited,graph,neighbour)
dfs(visited,graph,'A')