"""QuizBrain"""
import html

class QuizBrain:
    """The logic for running a quiz"""

    def __init__(self, questions):
        self.question_number = 0
        self.questions_list = questions
        self.correct_answers = 0

    def question_total(self):
        """returns an integer of the total questions"""
        return len(self.questions_list)

    def increment_question_number(self):
        """increases the question number"""
        self.question_number += 1

    def increment_correct_answers(self):
        """increases the correct answers"""
        self.correct_answers += 1

    def human_question_number(self):
        """Humanizes the number by starting at 1"""
        return int(self.question_number) + 1

    def still_has_questions(self):
        """returns a boolean of if there are more questions"""
        return self.question_number < len(self.questions_list)

    def current_question(self):
        """returns the current question object"""
        return self.questions_list[self.question_number]

    def score(self):
        """a string of the score"""
        return f"{self.correct_answers}/{self.question_total()}"

    def current_question_text(self):
        """returns unescaped question string"""
        return html.unescape(self.current_question().text)

    def next_question(self):
        """asks for the answer and checks it"""
        return f"Q.{self.human_question_number()} {self.current_question_text()} (True/False): "
        # self.check_answer(answer)
        # self.increment_question_number()

    def check_answer(self, answer):
        """checks the answer and prints details"""
        question = self.current_question()
        if answer.lower() == question.answer.lower():
            self.increment_correct_answers()
            print("That's correct!")
        else:
            print("That's wrong.")
        print(f"The correct answer is: {question.answer}")
        print(f"Your current score is {self.score()}\n")

