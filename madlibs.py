from textblob import TextBlob
class Poems:
  def __init__(self):
    self.madlibs_type_mapping = {1: "Computer", 2:"Generated", 3:"New"}
    self.madlibs_type_list = [f"{key}:{self.madlibs_type_mapping[key]}" for key in self.madlibs_type_mapping]
    self.preferences(input("Two player? (Y/N/ Enter to default single)"), input(f"Madlibs type? (Press 'Enter' to default Computer given madlibs or enter corresponding number: {self.madlibs_type_list}"))
    self.multiplayer = False
    self.madlibs_type = 1

  def preferences(self, multiplayer_yesno, lib_type_num):
      self.multiplayer = True if multiplayer_yesno == "Y" else False
      self.madlibs_type = lib_type_num if lib_type_num else 1
      print(self.multiplayer)
      print(self.madlibs_type)




z = Poems()
