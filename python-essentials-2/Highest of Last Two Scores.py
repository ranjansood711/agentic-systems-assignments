class StudentScores:
    def __init__(self, scores):
        self.scores = scores

    def highest_last_two(self):
        try:
            highest_score = max(self.scores[-1], self.scores[-2])          
            print("Highest score among last two is: ", highest_score)
            
        except IndexError:
            print("Not enough scores to find highest value")

try:
    user_input = input("Enter scores separated by spaces: ")
    score_list = list(map(int, user_input.split()))

    student = StudentScores(score_list)
    student.highest_last_two()

except ValueError:
    print("Invalid input")