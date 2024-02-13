import sys

from data import question_data
from question_model import QuestionModel
from quiz_brain import QuizBrain

score = 0

for index, data in enumerate(question_data):

    question_text = data['text']
    question_answer = data['answer']

    question = QuestionModel(question_text, question_answer)
    quiz_brain = QuizBrain(question, index+1, score)
    score, is_successful = quiz_brain.display_question()

    if not is_successful:
        sys.exit()


print("You've completed the quiz")
print(f"Your final score was: {score}/{len(question_data)}")
