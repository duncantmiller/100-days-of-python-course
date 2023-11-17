class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.questions_list = questions
        self.correct_answers = 0

    def question_total(self):
        return len(self.questions_list)

    def increment_question_number(self):
        self.question_number += 1

    def increment_correct_answers(self):
        self.correct_answers += 1

    def human_question_number(self):
        return int(self.question_number) + 1

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def current_question(self):
        return self.questions_list[self.question_number]

    def next_question(self):
        answer = input(
            f"Q.{self.human_question_number()} {self.current_question().text} (True/False): "
        )
        if self.check_answer(answer):
            self.increment_correct_answers()
        self.increment_question_number()

    def check_answer(self, answer):
        question = self.current_question()
        return answer == question.answer
