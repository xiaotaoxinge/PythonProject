class Circle:
    def __init__(self, point_x, point_y, center_x, center_y, radius):
        self.point_x = point_x
        self.point_y = point_y
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def judge(self):
        if (self.point_x - self.center_x) ** 2 + (self.point_y - self.center_y) ** 2 <= self.radius ** 2:
            return 1
        else:
            return -1


s = [int(x) for x in input().split(' ')]
a = Circle(s[0], s[1], s[2], s[3], s[4])
print(a.judge())
