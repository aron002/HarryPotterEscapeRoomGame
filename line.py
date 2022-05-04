class Line:
    def __init__(self, start, end, color):
        self.start = start
        self.end = end
        self.color = color

    def __repr__(self):
        return f'{self.start}, {self.end}, {self.color}'

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end and self.color == other.color