from textblob import TextBlob
import random
from collections import defaultdict
class Poems:
  def __init__(self):
    self.madlibs_type_mapping = {1: "Computer", 2:"Generated", 3:"New"}
    self.madlibs_tenses = {1: [(5, "noun"), (11, "adjective"), (15,"verb"), (18, "verb"), (26, "noun")]}
    self.madlibs_library = {1:"I ate a ton of sugar. \n It made me very sweet. \n It also made me very round -- \n now I can't find my feet."}
    self.madlibs_type_list = [f"{key}:{self.madlibs_type_mapping[key]}" for key in self.madlibs_type_mapping]
    self.madlibs_answers = defaultdict(list)
    self.multiplayer = False
    self.madlibs_type = 1
    self.player1 = ""
    self.player2 = ""

  def preferences(self, multiplayer_yesno, lib_type_num):
      self.multiplayer = True if multiplayer_yesno == "Y" else False
      self.madlibs_type = lib_type_num if lib_type_num else 1

      if self.madlibs_type == 1:
          random_lib = random.choice(list(self.madlibs_library.keys()))
          self.computer_generated_plays(random_lib)

  def single_play():
      self.player1 = input("Give yourself a name: ")

  def multi_play():
      self.player1 = input("Give yourself a name player 1: ")
      self.player2 = input("Give yourself a name player 2: ")

  def computer_generated_plays(self, rand_lib):
      lib = self.madlibs_library[rand_lib]

      lib_to_list = lib.split(" ")
      origin = []
      for ind, part_of_speech in self.madlibs_tenses[rand_lib]:
          origin.append((ind, lib_to_list[ind].replace('.', '')))
          ans = input(f"Provide a {part_of_speech}: ")
          self.madlibs_answers[rand_lib].append((ind, ans))
          lib_to_list[ind] = ans
      print("Original: " + str(origin))
      print("New: " + str(self.madlibs_answers[rand_lib]))
      print(' '.join(lib_to_list))
      return ' '.join(lib_to_list)

poem_inst = Poems()
poem_inst.preferences(input("Two player? (Y/N/ Enter to default single)"), input(f"Madlibs type? (Press 'Enter' to default Computer given madlibs or enter corresponding number: {poem_inst.madlibs_type_list}"))
