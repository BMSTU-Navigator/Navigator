from PIL import Image, ImageDraw
import random
class Drawer:
    path=None
    floor_points=[]

    def draw_path(self):
        cf=self.path.points[0].floor_index




    pass
im = Image.open("cat.jpg")
im.show()
draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=128)
draw.line((0, im.size[1], im.size[0], 0), fill=128)
del draw

# write to stdout
im.save('catout.jpg')