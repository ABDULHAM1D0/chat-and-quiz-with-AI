class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_question_remaining(self):
        return self.question_number < len(self.question_list)

    def next_question(self,):
        self.new_question = self.question_list[self.question_number]
        self.question_number += 1
        print(f"Q.{self.question_number}: {self.new_question.text}.")
        for option in self.new_question.options:
            print(f"{option}.{self.new_question.options[option]}")
        choice = int(input("Which is correct. choose: 1/2/3/4: "))
        self.check_answer(choice, self.new_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if self.new_question.options[user_answer].lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1

        else:
            print("That's wrong")

        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")