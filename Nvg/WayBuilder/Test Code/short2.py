for i in range(0,10):
    print(i)

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

w=[]
w.append([])     #0
w.append([2])    #1
w.append([1,3])  #2
w.append([2,4,6])  #3
w.append([3,5])    #4
w.append([4,8])  #5
w.append([3,7])  #6
w.append([6,9])  #7
w.append([5,9])
w.append([8,7])
print(w)
w=[]
for i in range(0,len(g)):
    w.append([])
    for j in range(0,len(g[i])):
        if(g[i][j]<10000):
            w[i].append(j)
print (w)





start=5
n=10
INF = 10 ** 10

dist = [INF] * n
dist[start] = 0
prev = [None] * n
used = [False] * n
min_dist = 0
min_vertex = start
while min_dist < INF:
    i = min_vertex
    used[i] = True
    for j in w[i]:
        if dist[i] + g[i][j] < dist[j]:
            dist[j] = dist[i] + g[i][j]
            prev[j] = i
    min_dist = INF
    for i in range(n):
        if not used[i] and dist[i] < min_dist:
            min_dist = dist[i]
            min_vertex = i

print('wdwdwdwdwd')
print(dist)
print('eddd')
j=7
path = []
while j is not None:
    path.append(j)
    j = prev[j]
path = path[::-1]
print(path)
sum=0
for i in range(0,len(path)-1):
    sum+=g[path[i]][path[i+1]]
    print(sum)