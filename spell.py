from line import Line

class Spell:
    def __init__(self, name, r_lines, color):
        self.name = name
        self.rough_lines = r_lines
        self.lines = []
        self.color = color
  
