"""imports"""
import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    """QuizInterface class"""

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.set_up_tk_configs()
        self.set_up_score_label()
        self.set_up_question_text()
        self.set_up_buttons()
        self.get_next_question()

        self.window.mainloop()

    def set_up_question_text(self):
        """question text config and creation"""
        self.ui_question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )

    def set_up_score_label(self):
        """score label config and creation"""
        self.score_label = tk.Label(text="Score 0/10", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

    def set_up_buttons(self):
        """buttons config and creation"""
        self.true_image = tk.PhotoImage(file="images/true.png")
        self.false_image = tk.PhotoImage(file="images/false.png")
        self.true_button = tk.Button(
            image=self.true_image, highlightthickness=0, command=self.mark_true
        )
        self.true_button.grid(row=2, column=0)
        self.false_button = tk.Button(
            image=self.false_image, highlightthickness=0, command=self.mark_false
        )
        self.false_button.grid(row=2, column=1)

    def set_up_tk_configs(self):
        """configs for tk and window"""
        self.window = tk.Tk()
        self.window.title = "Quizzler"
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

    def set_up_next_question(self):
        """sets up the screen for the next question"""
        self.canvas.config(bg="white")
        self.quiz.increment_question_number()
        self.get_next_question()
        self.update_score_display()

    def mark_true(self):
        """checks if true from the quiz brain"""
        self.give_feedback_and_set_up_next(self.quiz.is_answer_correct("true"))

    def give_feedback_and_set_up_next(self, is_correct):
        """send feedback to screen"""
        if is_correct:
            self.canvas.config(bg="green")
            self.quiz.increment_correct_answers()
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.set_up_next_question)

    def mark_false(self):
        """checks if false from the quiz brain"""
        self.give_feedback_and_set_up_next(self.quiz.is_answer_correct("false"))

    def update_score_display(self):
        """updates the score on screen"""
        self.score_label.config(text=self.quiz.score())

    def get_next_question(self):
        """gets the next question from the quiz brain"""
        if self.quiz.still_has_questions():
            self.update_question_text(self.quiz.next_question())
        else:
            self.end_quiz()

    def update_question_text(self, question_text):
        """updates the question text on the screen"""
        self.canvas.itemconfig(self.ui_question_text, text=question_text)

    def end_quiz(self):
        """ends the quiz"""
        self.update_question_text("You've reach the end!")
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
