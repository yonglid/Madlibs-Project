from textblob import TextBlob
import random
from collections import defaultdict
import nltk
nltk.download('punkt')
# seems to be using a simple perceptron algorithm
nltk.download('averaged_perceptron_tagger')
class Poems:
  def __init__(self):
    self.madlibs_type_mapping = {1: "Computer", 2:"Generated", 3:"New"}
    self.madlibs_tenses = {1: [(5, "noun"), (10, "adjective"), (13,"verb"), (16, "verb"), (23, "noun")]}
    self.madlibs_library = {1:"I ate a ton of sugar. It made me very sweet. It also made me very round -- now I can't find my feet."}
    self.madlibs_type_list = [f"{key}:{self.madlibs_type_mapping[key]}" for key in self.madlibs_type_mapping]
    self.madlibs_answers = defaultdict(list)
    self.multiplayer = False
    self.madlibs_type = 1
    self.player1 = ""
    self.player2 = ""
    self.blob_map = {"noun": ["NN", "NNS", "NNP", "NNPS"], "verb": ["VBD", "VB", "VBG", "VBN", "VBP", "VBZ"], "coordinating conjunction": ["CC"], "cardinal digit": ["CD"], "determiner": ["DT"], "existential there": ["EX"], "foreign word": ["FW"], "preposition/subordinating conjunction": ["IN"],
        "adjective": ["JJ", "JJR", "JJS"],
        "adjective, comparative": ["JJR"],
        "adjective, superlative": ["JJS"],
        "list marker": ["LS"],
        "modal": ["MD"],
        "noun, singular": ["NN"],
        "noun, plural":["NNS"],
        "proper noun, singular": ["NNP"],
        "proper noun, plural": ["NNPS"],
        "predeterminer": ["PDT"],
        "possessive ending": ["POS"],
        "possessive pronoun": ["PRP$"],
        "adverb": ["RB", "RBR", "RBS"],
        "adverb, comparative": ["RBR"],
        "adverb, superlative": ["RBS"],
        "particle": ["RP"],
        "to go": ["TO"],
        "interjection": ["UH"],
        "wh-determiner": ["WDT"],
        "wh-pronoun": ["WP"],
        "possessive wh-pronoun": ["WP$"],
        "wh-adverb where": ["WRB"]}

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
      blob = TextBlob(' '.join(lib_to_list))
      response = f""
      for ind in range(0, len(self.madlibs_tenses[rand_lib])-1):
          word_ind = self.madlibs_tenses[rand_lib][ind][0]
          pos = self.madlibs_tenses[rand_lib][ind][1]
          if blob.tags[word_ind][1] not in self.blob_map[pos]:
              response += f"{blob.tags[word_ind]} is not {pos}. "
      print(response)
      return ' '.join(lib_to_list)

poem_inst = Poems()
poem_inst.preferences(input("Two player? (Y/N/ Enter to default single)"), input(f"Madlibs type? (Press 'Enter' to default Computer given madlibs or enter corresponding number: {poem_inst.madlibs_type_list}"))
