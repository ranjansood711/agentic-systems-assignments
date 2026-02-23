class StudentMarks:
    def __init__(self, marks):
        self.marks = marks

    def last_three_avg(self):
        try:
            avg = (self.marks[-1] + self.marks[-2] + self.marks[-3]) / 3
            print("Average of last 3 marks is: ", avg)
        except IndexError:
            print("Not enough marks to calculate average")

try:
    user_input = input("Enter marks separated by spaces: ")
    marks_list = list(map(int, user_input.split()))

    student = StudentMarks(marks_list)
    student.last_three_avg()

except ValueError:
    print("Invalid input")