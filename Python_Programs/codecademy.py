class realStudent:
    def __init__(self, name = "", age = 0, grades = []):
        self.name = name
        self.age = age
        self.grades = []
    
    def addG (self, grade: int):
        self.grades.append(grade)
        print(self.grades)


def createStudent(name, age, grades=[]):
    return {
        'name': name,
        'age': age,
        'grades': grades
    }
chrisley = createStudent('Chrisley', 15)
dallas = createStudent('Dallas', 16)
c2 = realStudent("c2", 1)
d2 = realStudent("d2",2)
def addGrade(student, grade):
    student['grades'].append(grade)
    # To help visualize the grades we have added a print statement
    print(student['grades'])
addGrade(chrisley, 90)
addGrade(dallas, 100)
c2.addG(90)
d2.addG(100)