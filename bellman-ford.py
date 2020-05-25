infinity = 2**31

graph = {
    'bellman-ford': [('baran', 39.82), ('lovelace', 55.78)],
    'knuth': [('cerf', 92.92), ('hopper', 86.93), ('lovelace', 45.77)],
    'lovelace': [('hopper', 45.87), ('knuth', 145.80), ('bellman-ford', 55.84)],
    'baran': [('bellman-ford', 39.90), ('cerf', 62.76)],
    'hopper': [('knuth', 86.83), ('cerf', 98.91), ('lovelace', 45.94)],
    'cerf': [('baran', 62.93), ('hopper', 98.90), ('knuth', 92.89)]
}

def dist(current, dest, maxlength, jumps = 0):
    if jumps > maxlength:
        return infinity     # Can't be reached
    if current == dest:
        return 0            # Destination reached
    # Calculate dist from neighbor nodes
    result = infinity
    for edge in graph[current]:
        newdist = dist(edge[0], dest, maxlength, jumps + 1) + edge[1]
        if newdist < result:
            result = newdist
    return result

def bellman_matrix(starting):
    # Make new matrix
    matrix = {}
    for key in graph:
        matrix[key] = []
        for i in range(len(graph)):
            matrix[key].append(infinity)
    matrix[starting][0] = 0    # Set starting
    # for each length
    for length in range(1, len(graph)):
        for dest in matrix:
            current = matrix[dest][length - 1]
            new = dist(starting, dest, length)
            matrix[dest][length] = min(current, new)
    return matrix

def clean(matrix):
    for key in matrix:
        for i in range(len(graph)):
            if matrix[key][i] == infinity:
                matrix[key][i] = 'inf'

matrix = bellman_matrix('bellman-ford')
clean(matrix)

for node in matrix:
    print(node)
    print(matrix[node])

node = input('Enter node: ').lower()

i = 0
if node in matrix:
    for num in matrix[node]:
        i += 1
        print(str(i) + ': ' + str(num))
else:
    print('Node name not found')