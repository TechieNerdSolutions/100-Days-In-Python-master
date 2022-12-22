from question_model import QuestionModel
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for new_q in question_data:
    new_q_text = new_q["question"]
    new_q_answer = new_q["correct_answer"]
    question = QuestionModel(new_q_text, new_q_answer)
    question_bank.append(question)


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/ {quiz.question_number} ")
