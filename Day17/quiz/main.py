# from data import question_data

# score = 0

# for i in range(len(question_data)):
#     print(question_data[i]["text"])
#     ans = input("Enter your answer (True/False): ")

#     # input validation
#     if ans != "True" and ans != "False":
#         print("Invalid input, try again.")
#         continue

#     if ans == question_data[i]["answer"]:
#         score += 1
#         print("Correct!")
#     else:
#         print("Wrong!")

# print(f"Final score: {score}/{len(question_data)}")


from data import question_data

# Question class
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


# QuizBrain class
class QuizBrain:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.q_number = 0

    def still_has_questions(self):
        return self.q_number < len(self.questions)

    def next_question(self):
        current_q = self.questions[self.q_number]
        self.q_number += 1

        ans = input(f"Q{self.q_number}: {current_q.text} (True/False): ").capitalize()

        if ans != "True" and ans != "False":
            print("Invalid input, try again.")
            return self.next_question()   # ask again

        self.check_answer(ans, current_q.answer)

    def check_answer(self, user_ans, correct_ans):
        if user_ans == correct_ans:
            self.score += 1
            print("Correct! ✅")
        else:
            print("Wrong! ❌")

        print(f"Score: {self.score}/{self.q_number}\n")


# Convert data into Question objects
question_bank = []
for item in question_data:
    question = Question(item["text"], item["answer"])
    question_bank.append(question)


# Start quiz
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Quiz finished 🎉")
print(f"Final score: {quiz.score}/{len(question_bank)}")