class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: "
              f"{current_question.text}(True/False)?: ")#['text']はオブジェクトにするため使えない
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False
        # 上をする代わりに↓でいい。
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("正解です！")
            self.score += 1
        else:
            print("間違っています")
        print(f"実際の答え: {correct_answer}")
        print(f"あなたの現在のスコア: {self.score}/{self.question_number}")
        print("")








