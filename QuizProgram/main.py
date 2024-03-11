quiz = {
  "question1": {
    "question": "What is the capital of France?",
    "answer": "Paris"
  },
  "question2": {
  "question": "Who painted the Mona Lisa?",
    "answer": "Leonardo da Vinci"
  },
  "question3": {
    "question": "What is the largest planet in our solar system?",
    "answer": "Jupiter"
  },
  "question4": {
    "question": "What is the chemical symbol for gold?",
    "answer": "Au"
  },
  "question5": {
    "question": "Who wrote the play Romeo and Juliet?",
    "answer": "William Shakespeare"
  }
}

score = 0

for key, value in quiz.items():
  print(value['question'])
  answer = input("Answer? ")

  if answer.lower() == value['answer'].lower():
    print("Correct")
    score+=1
    print(f"score: {score}")

  else:
    print(f"Wrong answer\nThe answer is {value['answer']}\nscore: {score}")