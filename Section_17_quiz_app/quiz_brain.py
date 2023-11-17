class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.questions_list = questions

    def increment_question_number(self):
        self.question_number += 1

    def human_question_number(self):
        return int(self.question_number) + 1

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        question = self.questions_list[self.question_number]
        input(f"Q.{self.human_question_number()} {question.text} (True/False): ")
        self.increment_question_number()
