# Display a title 
print(r"""
 ██████╗ ██╗   ██╗██╗███████╗    ████████╗██╗███╗   ███╗███████╗██╗
██╔═══██╗██║   ██║██║╚══███╔╝    ╚══██╔══╝██║████╗ ████║██╔════╝██║
██║   ██║██║   ██║██║  ███╔╝        ██║   ██║██╔████╔██║█████╗  ██║
██║▄▄ ██║██║   ██║██║ ███╔╝         ██║   ██║██║╚██╔╝██║██╔══╝  ╚═╝
╚██████╔╝╚██████╔╝██║███████╗       ██║   ██║██║ ╚═╝ ██║███████╗██╗
 ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝       ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝╚═╝
""")
# Define tuples for questions and correct answers
questions = ("Q1. Walt Disney holds the record for the most Oscars.", "Q2. Atari made the first game console.", "Q3. Sheep can climb walls up to almost 90 degrees steep.", "Q4. An octopus has three hearts.", "Q5. Hydrogen is the first element on the periodic table.")
answers = ("T", "F", "F", "T", "T")
# Create variables for correct answers and 
correct = 0
numberOfQuestions = len(questions)
# Lay out the rules of the game
print("Hello and welcome to Quiz Time! You will be asked a series of true or false questions. Please ONLY answer with 'T' or 'F'. Good luck!")
print()
# Create a loop that cycles through the questions
for index in range(numberOfQuestions):
  # Display question
  print(questions[index])
  # Prompt user for an answer, making sure it's either "T" or "F"
  guess = input("Please enter 'T' or 'F': ")
  while (guess != "T" and guess != "F"):
    guess = input("Please enter 'T' or 'F': ")
  if (guess == answers[index]):
      correct += 1
  print()
# Display how many they got correct out of the total
print()
print(f"You answered {correct} out of {(numberOfQuestions)} questions correctly.")
# Congratulate them if they got 100%
if (correct == (numberOfQuestions)):
  print("You got a full score, great job!")