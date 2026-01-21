from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))
# print(question_bank[0].text)
# print(question_bank[0].answer)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()
print("クイズ終了!!")
print(f"最終的なスコア: {quiz.score}/{quiz.question_number}")