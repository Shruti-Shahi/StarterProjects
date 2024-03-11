import random

def get_choices():
  option = ["rock","paper","scissors"]
  player_choice = input("Enter a choice(rock, paper or scissors): ")
  computer_choice = random.choice(option)
  choice = {"player": player_choice, "computer": computer_choice}
  return choice


def check_win(player, computer, p_score, c_score):
  print(f"Player: {player}, Computer: {computer}")
  if player==computer:
    print("Draw!")
  elif player=="rock":
    if computer=="scissors":
      p_score += 1
      print("You Win!!")
    else:
      c_score+=1
      print("You Lose")
  elif player=="scissors":
    if computer=="rock":
      c_score+=1
      print("You Lose")
    else:
      p_score += 1
      print("You Win!!")
  elif player=="paper":
    if computer=="rock":
      p_score += 1
      print("You Win!!")
    else:
      c_score+=1
      print("You Lose")
  return p_score, c_score

print("Welcome to the Game")
p_score = 0
c_score = 0
answer = 1
while(answer):
  choices = get_choices()
  p_score, c_score = check_win(choices["player"], choices["computer"], p_score, c_score)
  print(f"Scores:\nPlayer: {p_score}, Computer: {c_score}")
  answer = int(input("Enter 1 to play and 0 to exit: "))

print("Thanks for playing!!!")
  
  