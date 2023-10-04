from question_model import Question
from data import question_data
from quiz_brain import quiz_Brain

question_list = []
print(question_data)

for i in range(len(question_data)):
    question_list.append(Question(text=question_data[i]['text'], answer=question_data[i]['answer']))

quiz_brain = quiz_Brain(question_list)
quiz_brain.ask_quiz()