"""import Question, question data and QuizBrain"""

from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
for item in question_data:
    question = Question(item["question"], item["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You scored {quiz.score()}")
