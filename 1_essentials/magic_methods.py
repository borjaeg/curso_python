class intX(int):
  def __lt__(self, v):
    return True
  
  def __gt__(self,v):
    return True

# from magic_methods import intX
# a = intX(10)
# a > 5
# a < 5
