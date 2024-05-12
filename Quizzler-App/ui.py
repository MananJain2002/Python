from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
THEME_FONT = ("Arial", 20, "italic")

class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 15, "bold"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=400, height=300, bg="white")
        self.question_text = self.canvas.create_text(
            200, 
            155, 
            width= 380, 
            font=THEME_FONT, 
            fill=THEME_COLOR, 
            text="Some Question Text"
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_button = Button(command=self.true_pressed)
        true_image = PhotoImage(file="./images/true.png")
        self.true_button.config(image=true_image, bd=0 ,bg=THEME_COLOR, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(command=self.false_pressed)
        false_image = PhotoImage(file="./images/false.png")
        self.false_button.config(image=false_image, bd=0, bg=THEME_COLOR, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.true_button.config(state="active")
            self.false_button.config(state="active")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_pressed(self):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.false_button.config(state="disabled")
        self.true_button.config(state="disabled")
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        