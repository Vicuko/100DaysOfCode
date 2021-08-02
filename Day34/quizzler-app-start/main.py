from question_model import Question
# from data import question_data
from quiz_brain import QuizBrain
import requests

def retrieve_questions():
    parameters = {
        "amount": "10",
        "type": "boolean"
    }
    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    data = response.json()
    questions = data["results"]
    return questions

question_bank = []
question_data = retrieve_questions()

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
