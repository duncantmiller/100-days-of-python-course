class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.questions_list = questions

    def increment_question_number(self):
        self.question_number += 1

    def next_question(self):
        question = self.questions_list[self.question_number]
        input(f"Q.{self.question_number} {question.text} (True/False)")
