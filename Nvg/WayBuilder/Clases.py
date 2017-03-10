class Graph:
    connections=[]

    def __init__(self,connections):
        super().__init__()
        self.connections=connections

    def reque_path(self,start_point,stop_point,detalization_level):

        return None

class GraphConnection:
    point1 = -1
    point2 = -1

    connection_weight = -1

    connection_comment = None

    picture_path = None

    floor_index = -1

    def __init__(self, point1, point2, connection_weight, connection_comment, picture_path, floor_index):
        super().__init__()
        self.point1 = point1
        self.point2 = point2
        self.connection_weight = connection_weight
        self.connection_comment = connection_comment
        self.picture_path = picture_path
        self.floor_index = floor_index
