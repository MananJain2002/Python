from question_model import Question
from data import Data
from quiz_brain import QuizBrain
import html

data = Data()
data.create_api()
question_data = data.generate_data()

question_bank = [Question(html.unescape(quiz['question']), quiz['correct_answer']) for quiz in question_data]

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")