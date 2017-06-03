import math

class Point:

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def distant(self, distan):
        x0 = self.x - distan.x
        y0 = self.y - distan.y
        dist = math.sqrt(x0 ** 2 +  y0 ** 2)
        return dist

    def halfway(self):
        mx = (p1.x + p2.x)/2
        my = (p1.y + p2.y)/2
        return mx, my
    def reflect_x(self):

        xm = self.x
        ym = self.y * (-1)
        return  xm, ym
    def reflect_y(self):

        xm = self.x * (-1)
        ym = self.y
        return  xm, ym
    def reflect_O(self):

        xm = self.x * (-1)
        ym = self.y * (-1)
        return  xm, ym
    def get_line_to(self, other_point):
        xn = self.x - other_point.x
        yn = self.y - other_point.y
        # return yn, xn * (-1)
        return ("x -", (yn * -1), "+ y -", xn, " = 0 ")

        # return yn, xn * (-1)


    def print(self):

        # print("Khoảng cách =",self.distant(p2), " Trung điểm của p1 và p2:", self.halfway(), "đôi xứng qua 0x:",self.reflect_x(),"đối xứng qua 0y:", self.reflect_y()
        #       ,"đối xứng qua O:", self.reflect_O(), "Phuong trinh:",self.get_line_to(p2))
        print("Khoảng cách= {0}. Trung điểm p1 và p2={1} . Đối xứng qua 0x= {2}. Đối xứng qua 0y={3}. Đối xứng qua 0= {3}".format(self.distant(p2), self.halfway(), self.reflect_x(), self.reflect_y(), self.reflect_O()))
        print()
p1 = Point(4,3)
p2 = Point(2,1)
p1.reflect_x()
p1.reflect_y()
p1.reflect_O()

Point.print(p1)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.height + 2 * self.width

    # def contain(self,points):
    #     self.points = points
    #     for point in points:
    #         if point.x <= hcn.x and point.y <= hcn.y:
    #             return True
    #
    #         return False

    def flip(self):
        [self.width, self.height] = [self.height, self.width]
        print("Width = {0}Height = {1}".format(self.width, self.height))

    def print(self):
        print("area= {0} . perimeter= {1}".format(self.area(), self.perimeter()))
        print(Rectangle.flip(hcn))


hcn = Rectangle(10,5)

hcn.print()



