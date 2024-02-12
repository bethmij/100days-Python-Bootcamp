class QuizBrain:
    def __init__(self, question, index, score):
        self.question = question
        self.total_questions = index
        self.score = score

    def display_question(self):
        is_successful = False
        msg = f"Q.{self.total_questions}: {self.question.text} (True/False)? : "
        user_answer = input(msg).capitalize()
        is_answer_correct = self.check_answer(user_answer)

        if is_answer_correct:
            print("You got it right!")
            is_successful = True
        else:
            print("That's wrong")

        print(f"The correct answer was: {self.question.answer}")
        print(f"Your current score is: {self.score}/{self.total_questions}\n\n")
        return self.score, is_successful

    def check_answer(self, user_answer):
        if user_answer == self.question.answer:
            self.score += 1
            print("check answer ", self.score)
            return True
        return False
h