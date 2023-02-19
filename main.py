#krok 11 zadania z 19.02.2023
import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Point({self.x},{self.y}"

    def translate(self, x, y):
        self.x+=x
        self.y+=y

class Segment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self) -> str:
        return f"Segment({self.p1},{self.p2}"

    def distance(self):
        return math.hypot(self.p1.x-self.p2.x, self.p1.y-self.p2.y)

    def svg(self):
        return f'<line x1="{self.p1.x}" y1="{self.p1.y}" x2="{self.p2.x}" y2="{self.p2.y}" style="stroke:black" />'


class Polygon:
    def __init__(self, style):
        self.vertices=[]
        self.style=style

    def add(self, vertex):
        self.vertices.append(vertex)

    def __str__(self) -> str:
        vertices_str=""
        for vertex in self.vertices:
            vertices_str+=str(vertex) + ", "
        return f"Polygon({vertices_str[:-2]})"

    def svg(self):
        vertices_str = ""
        for vertex in self.vertices:
            vertices_str += f'{vertex.x},{vertex.y} '
        return f'<polygon points = "{vertices_str[:-1]}" {self.style.svg()} />'

    def area(self):
        result = 0
        for i in range(len(self.vertices)):
            pa = self.vertices[i]
            pn = self.vertices[(i+1)%len(self.vertices)]
            det = (pa.x*pn.y)-(pa.y*pn.x)
            result += det
        return abs(result/2)

    @staticmethod
    def regular_pentagon(radius):
        polygon = Polygon()
        for i in range(5):
            x = radius * math.cos(math.radians(72*i))
            y = radius * math.sin(math.radians(72*i))
            polygon.add(Point(x, y))
        return polygon

    def translate(self, x, y):
        for vertex in self.vertices:
            vertex.translate(x, y)

class Style:
    def __init__(self, file_color="transparent", stroke_color="black", stroke_width=1):
        self.file_color=file_color
        self.stroke_color=stroke_color
        self.stroke_width=stroke_width

    def svg(self):
        return f'style="fill:{self.fill_color};stroke{self.stroke_color};stroke_width{slef.stroke_width}'


def main():
    p = Point(300, 0)
    q = Point(0, 400)
    polygon=Polygon(Style(file_color="red"))
    polygon.add(p)
    polygon.add(q)
    polygon.add(Point(300, 400))

    #print(polygon.svg())
    #print(polygon.area())

    pentagon = Polygon.regular_pentagon(150)
    pentagon.translate(300, 400)
    print(pentagon.svg())

main()
