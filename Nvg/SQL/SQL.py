from peewee import *
from Nvg.Clases import *




class Point(Model):
    id = IntegerField()
    name = CharField()
    floor_index = IntegerField()
    path_for_point_pic = CharField()
    x = IntegerField()
    y = IntegerField()




class Floor(Model):
    picture_path = CharField()
    floor_index = IntegerField()



class GraphConnection(Model):
    id=IntegerField()
    point1 = IntegerField()
    point2 = IntegerField()
    connection_weight = IntegerField()
    connection_comment = CharField()
    picture_path = CharField()
    floor_index = IntegerField()
    trans_floor_marker = BooleanField()


class Dialogs(Model):
    id=IntegerField()
    style1=CharField()
    style2=CharField()
    style3=CharField()


class SQL:
    def get_building(self)->Building:
        building = Building()
        building.graph=self.get_graph()
        building.floors=Floor.select()
        return None

    def get_graph(self)->Graph:
        graph=Graph()
        graph.connections=GraphConnection.select()
        graph.points=Point.select()
        graph.points_dict={}
        for point in graph.points:
            graph.points_dict[point.id]=point
        return graph


Floor.create_table(True)
Point.create_table(True)
GraphConnection.create_table(True)
Dialogs.create_table(True)

#grandma = Person.select().where(Person.name == 'Grandma L.').get()