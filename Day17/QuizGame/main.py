from question_model import Question
from data import question_data

question_bank = list()

for line in question_data:
    question_bank.append(Question(line["text"], line["answer"]))

# print (question_bank)
#
# for question in question_bank:
#     print (question.text, ":", question.answer)