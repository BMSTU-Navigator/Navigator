class WayBuilderClass:
    graph = None
    paths = None
    dijkstra_graph = None
    max_id = -1

    def init_pre_count(self):
        for tmp_point in self.graph:
            if tmp_point.id >= self.max_id: self.max_id = tmp_point.id
        self.paths=[self.max_id]
        self.dijkstra_graph = []
        for i in range(self.max_id):
            self.dijkstra_graph.append([10000] * self.max_id)
        for conection in self.graph.connections:
            self.dijkstra_graph[conection.point1.id][conection.point2.id]=conection.weight

    def dijkstra(self, start,stop):
        valid = [True] * self.max_id
        weight = [1000000] * self.max_id
        weight[start] = 0
        for i in range(self.max_id):
            self.paths[i] = []
            min_weight = 1000001
            ID_min_weight = -1
            for i in range(self.max_id):
                if valid[i] and weight[i] < min_weight:
                    min_weight = weight[i]
                    ID_min_weight = i

            for i in range(self.max_id):
                if weight[ID_min_weight] + self.dijkstra_graph[ID_min_weight][i] < weight[i]:
                    weight[i] = weight[ID_min_weight] + self.dijkstra_graph[ID_min_weight][i]
            valid[ID_min_weight] = False
        if weight[stop]==10000:raise Exception('no path to point')
        return weight



    def psi_init(self):
        self.dijkstra_graph = []
        self.max_id = 10
        self.paths = [0]*self.max_id

        for i in range(self.max_id):
            self.dijkstra_graph.append([10000] * self.max_id)

        self.dijkstra_graph[1][2] = 5
        self.dijkstra_graph[2][1] =5
        self.dijkstra_graph[2][3] = 10
        self.dijkstra_graph[3][2] = 10
        self.dijkstra_graph[3][4] = 1
        self.dijkstra_graph[4][3] = 1
        self.dijkstra_graph[4][5] = 1
        self.dijkstra_graph[5][4] = 1
        self.dijkstra_graph[5][8] = 1
        self.dijkstra_graph[8][5] = 1
        self.dijkstra_graph[8][9] = 1
        self.dijkstra_graph[9][8] = 1
        self.dijkstra_graph[3][6] = 3
        self.dijkstra_graph[6][3] = 3
        self.dijkstra_graph[6][7] = 6
        self.dijkstra_graph[7][6] = 6
        self.dijkstra_graph[7][9] = 8
        self.dijkstra_graph[9][7] = 8
        # прочитать g // g[0 ... n - 1][0 ... n - 1] - массив, в котором хранятся веса рёбер, g[i][j] = 2000000000, если ребра между i и j нет






        #      -4-5-8-
        # 1-2-3<        >-9
        #




        # первая вершина-вторая вершина-вес перехода
        # 1-2-5
        # 2-1-5





        # -(3)-4-(5)-5-(2)-8-(5)-
        # 1-(5)-2-(10)-3<                         >-9
        #                -(3)-6-(6)-7-(8)------
