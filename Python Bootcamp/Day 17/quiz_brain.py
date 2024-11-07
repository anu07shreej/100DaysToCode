class QuizBrain:
    def __init__(self, q_list):
        self.qnum = 0
        self.que_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.qnum < len(self.que_list)


    def next_question(self):
        current_que = self.que_list[self.qnum]
        self.qnum += 1
        user_ans = input(f"Q.{self.qnum}: {current_que.text} (True/False):")
        self.check_answer(user_ans,current_que.ans)

        #if ans == self.que_list[self.qnum]

    def check_answer(self, user_ans,correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("That's correct")
            self.score += 1
        else:
            print("Wrong answer.")
        print(f"The correct answer is {correct_ans}")
        print(f"Your current score is: {self.score}/{self.qnum}")
        print("\n")
