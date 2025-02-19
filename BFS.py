# Logic
# Make two queue one for the visited elements and one for the graph nodes
# we will pop the nodes from the visted queue and print and we will push the adjacent nodes in the queue from the initial queue
# In short push the nodes breadth wise, pop then and print them

from collections import deque
def bsf(graph,root):
    visited = set()
    queue = deque([root])

    while queue:
        vertex = queue.popleft()
        visited.add(vertex)
        for i in graph[vertex]:
            if i not in visited:
                queue.append(i)
    print(visited)
if __name__ == "__main__":
    # Dictionary
    graph = {0:[1,2,3],1:[0,2],2:[0,1,4],4:[2],3:[0]}
    bsf(graph,0)