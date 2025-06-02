class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

class Line:
  def __init__(self, start, end):
    self.__start = start
    self.__end = end

  def draw(self, window, fill_color):
    window.create_line(self.__start.x, self.__start.y, self.__end.x, self.__end.y, fill=fill_color, width=2)
