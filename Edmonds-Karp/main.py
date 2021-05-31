
def opening_file(name_of_file):
    with open(name_of_file, "r") as file:
        nodes = [line.strip() for line in file]
    list1 = []
    for node in nodes:
        list1.append(node.split(", "))
    list_of_nodes = []
    for nodes in list1:
        list3 = []
        for single in nodes:
            element = single.replace(",", " ")
            element = element.replace("[", "")
            element = element.replace("]", "")
            list4 = []
            for ele in element.split(" "):
                list4.append(int(ele))
            list3.append(list4)
        list_of_nodes.append(list3)
    print("LIST")
    for x in list_of_nodes:
        print(x)
    return list_of_nodes


def bfs(r, start, end):
    queue = []
    visited = []
    predecessor = []
    flag = 0
    for x in range(len(r)):
        predecessor.append(-1)
    queue.append(start)
    visited.append(start)
    predecessor[start] = None

    while queue:
        actual = queue.pop(0)
        i = 0
        for neighbour in r[actual]:
            if neighbour[0] not in visited and neighbour[1] > 0:
                queue.append(neighbour[0])
                visited.append(neighbour[0])
                predecessor[neighbour[0]] = (actual, i)
                if neighbour[0] == end:
                    flag = 1
                    break
            i += 1

    path = []
    x = (end, 2137)
    if flag == 0:
        return -1
    else:
        while x[0] != start:
            path.append(x)
            x = predecessor[x[0]]
        path.append(x)
        path.reverse()
        return path


def residual(list_of_nodes, flow_):
    r = []
    for i in range(len(list_of_nodes)):
        list_1 = []
        for j in range(len(list_of_nodes[i])):
            list_1.append([list_of_nodes[i][j][0], list_of_nodes[i][j][1] - flow_[i][j][1]])
        r.append(list_1)

    return r


def flow(list_of_nodes):
    f = []
    for node in list_of_nodes:
        list1 = []
        for each in node:
            list1.append([each[0], 0])
        f.append(list1)
    return f


def max_flow(f, start):
    m_f = 0
    for each in f[start]:
        m_f += each[1]
    return m_f


def edmonds_karp(list_of_nodes, start, end):
    path = True
    f = flow(list_of_nodes)
    r = residual(list_of_nodes, f)
    while path:
        r = residual(list_of_nodes, f)
        p = bfs(r, start, end)
        if p == -1:
            path = False
        else:
            mini = float("Inf")
            for i in range(len(p) - 1):
                if r[p[i][0]][p[i][1]][1] < mini:
                    mini = r[p[i][0]][p[i][1]][1]
            for i in range(len(p) - 1):
                f[p[i][0]][p[i][1]][1] += mini
                for j, y in enumerate(f[p[i+1][0]]):
                    if y[0] == p[i][0]:
                        f[p[i+1][0]][j][1] -= mini

    return max_flow(f, start)

if __name__ == '__main__':
    start = 8
    end = 0
    list_of_notes = opening_file("graph.txt")
    max_f = edmonds_karp(list_of_notes, 8, 0)
    print("MAX FLOW when start =", start,",end =", end,"is equal", max_f)
