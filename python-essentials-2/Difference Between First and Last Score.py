class StudentPerformance:
    def __init__(self, scores):
        self.scores = scores

    def score_difference(self):
        try:
            difference = self.scores[-1] - self.scores[0]      
            print("Difference between last and first score is: ", difference)
            
        except IndexError:
            print("No scores available to calculate difference")

try:
    user_input = input("Enter scores separated by spaces: ")
    score_list = list(map(int, user_input.split()))

    student = StudentPerformance(score_list)
    student.score_difference()

except ValueError:
    print("Invalid input")