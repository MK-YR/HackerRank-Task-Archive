def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib <= c_road:
        return n * c_lib
    connections = {i:[] for i in range(1, n + 1)}
    for first, second in cities:
        connections[first].append(second)
        connections[second].append(first)
    visited = set()
    def graph_size(node):
        size = 0
        cities = [node]
        while cities:
            city = cities.pop()
            if city in visited:
                continue
            visited.add(city)
            size += 1
            for connected in connections[city]:
                if connected not in visited:
                    cities.append(connected)
        return size
    total = 0
    for node in range(1, n + 1):
        if node not in visited:
            graph = graph_size(node)
            total += c_lib + (graph - 1) * c_road
    return total
q = int(input().strip())
for q_itr in range(q):
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    c_lib = int(first_multiple_input[2])
    c_road = int(first_multiple_input[3])
    cities = []
    for _ in range(m):
        cities.append(list(map(int, input().rstrip().split())))
    result = roadsAndLibraries(n, c_lib, c_road, cities)
    print(str(result) + '\n')