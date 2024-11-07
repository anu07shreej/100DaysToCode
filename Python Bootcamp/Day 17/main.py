from question_model import Question
from data import question_data, question_data1
from quiz_brain import QuizBrain
question_bank = []
for que in question_data1:
    tex = que["question"]
    anw = que["correct_answer"]
    q_obj = Question(tex,anw)
    question_bank.append(q_obj)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.qnum}")