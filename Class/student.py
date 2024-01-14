class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def getGrade(self):
        return self.grade

class Course:
    def __init__(self, name, maxStudent):
        self.name = name
        self.maxStudent = maxStudent
        self.student = []

    def addStudent(self, student):
        if len(self.student) < self.maxStudent:
            self.student.append(student)
            return True
        return False
    
    def getAverage(self):
        value = 0
        for student in self.student:
            value = value + student.getGrade()

        return value / len(self.student)


s1 = Student("a", 19, 90)
s2 = Student("b", 18, 98)
s3 = Student("c", 20, 70)

course = Course("Science", 2)
course.addStudent(s1)
course.addStudent(s2)
