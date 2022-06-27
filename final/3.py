# 3
class Player:
  team = "TIGERS"

  def __init__(self, avg, hr, age):
    self.avg = avg
    self.hr = hr
    self.age = age
  
  def sum_player(self, player):
    sum = self.hr + player.hr
    print(sum)

bh = Player(0.378, 15, 33)
sb = Player(0.359, 12, 25)
dh = Player(0.315, 17, 29)