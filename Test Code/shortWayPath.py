# прочитать g // g[0 ... n - 1][0 ... n - 1] - массив, в котором хранятся веса рёбер, g[i][j] = 2000000000, если ребра между i и j нет


def Dijkstra(N, S, matrix):
    valid = [True] * N
    weight = [1000000] * N
    weight[S] = 0
    for i in range(N):
        paths[i]=[]
        min_weight = 1000001
        ID_min_weight = -1
        for i in range(N):
            if valid[i] and weight[i] < min_weight:
                min_weight = weight[i]
                ID_min_weight = i

        for i in range(N):
            if weight[ID_min_weight] + matrix[ID_min_weight][i] < weight[i]:
                weight[i] = weight[ID_min_weight] + matrix[ID_min_weight][i]
        valid[ID_min_weight] = False
    return weight


#      -4-5-8-
# 1-2-3<        >-9
#


paths=[]

g = []
for i in range(10):
    g.append([10000] * 10)

# первая вершина-вторая вершина-вес перехода
# 1-2-5
# 2-1-5


g[1][2] = 5
g[2][1] = 5

g[2][3]=10
g[3][2]=10
g[3][4]=1
g[4][3]=1
g[4][5]=1
g[5][4]=1
g[5][8]=1
g[8][5]=1
g[8][9]=1
g[9][8]=1
g[3][6]=3
g[6][3]=3
g[6][7]=6
g[7][6]=6
g[7][9]=8
g[9][7]=8
for i in range(0, 10):
    print(g[i])

#                -(3)-4-(5)-5-(2)-8-(5)-
# 1-(5)-2-(10)-3<                         >-9
#                -(3)-6-(6)-7-(8)------

print(Dijkstra(10, 1, g))
