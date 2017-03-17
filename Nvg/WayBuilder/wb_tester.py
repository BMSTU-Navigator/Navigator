from Nvg.WayBuilder.WayBuilderClass import *
from Nvg.SQL.SQL import *







building =get_building()
wb = WayBuilderClass(building)
wb.init_pre_count()

path=wb.request_path(1,4)


print('\n\n\n\n')

for i in range(len(path.points)):
    print(path.points[i].name)
    if(i<len(path.connections)):print('com '+str(path.connections[i].connection_comment))


#for i in path.connections:
#    print(i.)

print(path.connections)
print(path.floors)
print(path.weight)

