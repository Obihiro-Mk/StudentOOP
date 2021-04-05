class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    grades = []



class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'



class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if 0 < grade < 11:
                lecturer.grades += [grade]
            else:
                print("Неправильная оценка")
        else:
            return 'Ошибка'



student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Java']

# print(student_1.courses_in_progress)

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']

reviewer_1 = Reviewer('Ronnie', 'Kirk')
reviewer_1.courses_attached += ['Java']

# print(cool_lecturer.courses_attached)

student_1.rate_lw(cool_lecturer, 'Python', 9)
student_1.rate_lw(cool_lecturer, 'Python', 5)
# student_1.rate_lw(cool_lecturer, 'Python', 15)
#
# print(cool_lecturer.grades)

reviewer_1.rate_hw(student_1, 'Java', 9)

print(student_1.grades)


# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.finished_courses += ['Git']
# best_student.courses_in_progress += ['Python']
# best_student.grades['Git'] = [10, 10, 10, 10, 10]
# best_student.grades['Python'] = [10, 10]
#
# print(best_student.finished_courses)
# print(best_student.courses_in_progress)
# print(best_student.grades)
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
# print(cool_mentor.courses_attached)

