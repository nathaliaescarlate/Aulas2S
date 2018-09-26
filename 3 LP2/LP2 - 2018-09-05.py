class Televisao:  
  def __init__(self, mini=None, maxi=None):
    self.canal = 2
    if mini != None:
        self.__cmini = mini
    if maxi != None:
        self.__cmaxi = maxi

  def get_cmini(self):
    return self.__cmini

tv = Televisao(2,50)
print(tv.canal)

tv.__cmini = 20

