from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question = Question(text=item['text'], answer=item['answer'])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_have_questions():
    quiz.next_question()

quiz.final_score()




