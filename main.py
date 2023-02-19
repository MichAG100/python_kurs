#krok 3 zadania z 19.02.2023
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Point({self.x},{self.y}"


def main():
    p = Point(5, 10)
    p.x= 100
    print(p.x, p.y)

main()
