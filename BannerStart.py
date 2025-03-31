import pyfiglet 
from pyfiglet import figlet_format
def Banner():
  banner = figlet_format("CodingLab Hangman",font = 'standard',width = 200)
  print("歡迎來到Hangman，請猜出對的字，你有7次機會")
  print("------------------GameStart------------------")
