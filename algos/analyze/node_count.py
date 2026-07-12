from collections import deque

def countCompleteComponents(n: int, edges) -> int:
    adj_list = {i: [] for i in range(n)}
    visited = set()
    count = 0
    # Populate the adjacency list
    for n1, n2 in edges:
        adj_list[n1].append(n2)
        adj_list[n2].append(n1)

    # Check all nodes in range
    for start in range(n):
        # Check that node hasnt been visited
        if start in visited:
            continue

        # Create a queue
        queue = deque([start])

        # Mark the node as visited
        visited.add(start)

        # Create counters for nodes and edges
        nodes = 0
        edges = 0

        # Traverse all nodes connected to the start node
        while queue:
            node = queue.popleft()
            nodes += 1
            edges += len(adj_list[node])

            for neighbor in adj_list[node]:
                if neighbor in visited:
                    continue

                visited.add(neighbor)
                queue.append(neighbor)

        # Deduce edge count
        edge_cnt = edges // 2

        # Check if all vertices share an edge
        if edge_cnt == nodes * (nodes - 1) // 2:
            count += 1


    return count



print(countCompleteComponents(6, [[0,1],[0,2],[1,2],[3,4]]))
print(countCompleteComponents(6, [[0,1],[0,2],[1,2],[3,4],[3,5]]))



    # edge_cnt = dict.fromkeys(set(node_map.values()), 0)
    # print(node_map)
    # print(node_map.values())


    # for v in node_map.values():
    #     edge_cnt[v] += 1

    # print(edge_cnt)

    # for k, v in edge_cnt.items():
    #     if v*(v -1)/2 == k:
    #         print("k", k, "v", v, "=", int(v*(v -1)/2))
    #         completed += 1
    #         print("completed...", completed)

    # print(completed)

    # return completed
