class Student:

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.grades = []
        self.fail = 0
        self.average = 0

    def avg(self):
        if len(self.grades) > 0:
            self.average = round(sum(self.grades)/len(self.grades), 1)

    def fcount(self, grade):
        if grade < 60:
            self.fail += 1

    def add(self, grade):
        self.grades.append(grade)
        self.avg()
        self.fcount(grade)

    def info(self):
        print('Name:', self.name)
        print('Gender:', self.gender)
        print('Grades:', self.grades)
        print('Avg: %.1f' % self.average)
        print('Fail Number:', self.fail)
        print()


def top(*students):
    top_student = students[0]
    for i in range(1, len(students)):
        if top_student.average < students[i].average:
            top_student = students[i]
    return top_student

s1 = Student("Tom", "M")
s2 = Student("Jane", "F")
s3 = Student("John", "M")
s4 = Student("Ann", "F")
s5 = Student("Peter", "M")
s1.add(80)
s1.add(90)
s1.add(55)
s1.add(77)
s1.add(40)
s2.add(58)
s2.add(87)
s3.add(100)
s3.add(80)
s4.add(40)
s4.add(55)
s5.add(60)
s5.add(60)

s1.info()
s2.info()
s3.info()
s4.info()
s5.info()
print('Top Student:')
top(s1, s2, s3, s4, s5).info()
# Name = input()
# Gender = input()
# student = Student(Name, Gender)
# student.add(eval(input()))
# student.add(eval(input()))
# student.add(eval(input()))
# # student.avg()
# student.info()
