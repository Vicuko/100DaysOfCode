from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = list()

for line in question_data:
    question_text = line["text"]
    question_answer = line["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

    # Another way of writing it down:
    # question_bank.append(Question(line["text"], line["answer"]))

# print (question_bank)
#
# for question in question_bank:
#     print (question.text, ":", question.answer)