import random

class RockBot:
  name = "RockBot"
  def play(self):
    return "rock"
  def handle_moves(self, own_move, opponent_move):
    pass

class PaperBot:
  name = "PaperBot"
  def play(self):
    return "paper"
  def handle_moves(self, own_move, opponent_move):
    pass

class ScissorsBot:
  name = "ScissorsBot"
  def play(self):
    return "scissors"
  def handle_moves(self, own_move, opponent_move):
    pass

class RandomBot:
  name = "Randombot"
  def play(self):
    return random.choice(["rock","paper","scissors"])
  def handle_moves(self, own_move, opponent_move):
    pass

class TwoCycler:
  name = "TwoCycler"
  counter=0
  def play(self):
    return ["rock","paper"][self.counter%2]
  def handle_moves(self, own_move, opponent_move):
    self.counter+=1

class FiveCycler:
  name = "FiveCycler"
  counter=0
  def play(self):
    return ["rock","paper","paper","scissors","paper"][self.counter%5]
  def handle_moves(self, own_move, opponent_move):
    self.counter+=1

class CounterBot:
  name = "CounterBot"
  history = "paper"
  def play(self):
    return self.counter_move(self.history)
  def handle_moves(self, own_move, opponent_move):
    self.history=opponent_move
  def counter_move(self, move):
    counter = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    return counter.get(move)
  
class DrawBot:
  name = "DrawBot"
  history = "paper"
  def play(self):
    return self.history
  def handle_moves(self, own_move, opponent_move):
    self.history=opponent_move

class DumbBot:
  name = "DumbBot"
  history = "paper"
  def play(self):
    return self.self_counter_move(self.history)
  def handle_moves(self, own_move, opponent_move):
    self.history=opponent_move
  def self_counter_move(self, move):
    counter = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    return counter.get(move)



strategy = ScissorsBot()