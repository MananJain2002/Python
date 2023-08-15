ANSWERS = ["true", "false", "t", "f"]

class QuizBrain:

    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        user_answer = ""
        self.question_number += 1
        while user_answer not in ANSWERS:
            user_answer = input(f"Q.{self.question_number}: {question.text} ({'/'.join(ANSWERS[:2]).capitalize()})?: ").lower()
        self.check_answer(user_answer, question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer[0] == correct_answer[0].lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: ({self.score}/{self.question_number})\n\n")