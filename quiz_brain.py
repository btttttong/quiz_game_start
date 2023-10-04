from typing import List
from question_model import Question

# :List[Question] = tell type of input to do this we need to import in before use
# 1. import from typing import List
# 2. from question_model import Question > go to class of Question object which is contain text and answer

class quiz_Brain:
    def __init__(self, list_question: List[Question]):
        self.list_question = list_question
        self.q_no = 0
        self.score = 0

    def has_more_question(self):
        return self.q_no < len(self.list_question)

    def check_answer(self, user_choice, answer):
        if user_choice == answer:
            print('You are correct ^_^')
            return True
        else:
            print('You are wrong T_T')

    def ask_quiz(self):
        while self.has_more_question():
            print(f'Q.{self.q_no+1}: {self.list_question[self.q_no].text} (True/False)')

            user_choice = input('Enter your answer here: ') or 'True'
            if user_choice != 'True' and user_choice != 'False':
                print('invalid input')
            else:
                if self.check_answer(user_choice, self.list_question[self.q_no].answer):
                    self.score += 1
                self.q_no += 1
                print(f'your current score is {self.score}/{self.q_no}')

        print('-----------------------------------')
        print(f'summary answer: \n{self.score} correct  \n{self.q_no - self.score} wrong')


        # for i in self.list_question:
        #     q_no += 1
        #     print(f'Q.{q_no}: {i.text} (True/False)')
        #     user_choice = input('Enter your answer here: ') or 'True'
        #     # if user_choice not in 'True' or 'False':
        #
        #     if self.check_answer(user_choice, i.answer):
        #         score += 1
        #     print(f'your current score is {score}/{q_no}')
        # print('-----------------------------------')
        # print(f'summary answer: \n{score} correct  \n{q_no - score} wrong')
