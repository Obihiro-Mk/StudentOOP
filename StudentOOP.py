class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []

    def __str__(self):
        average_grade = round((sum(self.grades)) / len(self.grades), 1)
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {average_grade}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return "Неверный лектор"
        else:
            average_grade = round((sum(self.grades)) / len(self.grades), 1)
            average_grade_other = round((sum(other.grades)) / len(other.grades), 1)
            return (average_grade < average_grade_other)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


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

    def __str__(self):
        total = []
        for course, value_grade in self.grades.items():
            total += value_grade
        average_grade = round((sum(total)) / len(total), 1)
        progress_ = ', '.join(self.courses_in_progress)
        finished_ = ', '.join(self.finished_courses)
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {average_grade}' \
               f'\nКурсы в процессе изучения: {progress_}\nЗавершенные курсы: {finished_}'

    def __lt__(self, other):
        total = []
        if not isinstance(other, Student):
            return "Неверный студент"
        else:
            for course, value_grade in self.grades.items():
                total += value_grade
            average_grade = round((sum(total)) / len(total), 1)
            total_other = []
            for course_other, value_grade_other in other.grades.items():
                total_other += value_grade_other
            average_grade_other = round((sum(total_other)) / len(total_other), 1)
            return (average_grade < average_grade_other)

student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.finished_courses += ['Git']
student_1.finished_courses += ['Введение в программирование']
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Java']
student_1.grades['Java'] = [10, 7]
student_1.grades['Python'] = [10, 9]
student_1.grades['Git'] = [10, 6 ]
student_1.grades['Введение в программирование'] = [8, 7]

student_2 = Student('Petya', 'Ivanov', 'your_gender')
student_2.finished_courses += ['Git']
student_2.finished_courses += ['Введение в программирование']
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Java']
student_2.grades['Java'] = [10, 5]
student_2.grades['Python'] = [10, 7]
student_2.grades['Git'] = [9, 7]
student_2.grades['Введение в программирование'] = [9, 7]

lecturer_1 = Lecturer('Some', 'Buddy')
lecturer_1.courses_attached += ['Python']
lecturer_1.grades += [6, 10]

lecturer_2 = Lecturer('Dima', 'Ivanov')
lecturer_2.courses_attached += ['Java']
lecturer_2.grades += [6, 8]

reviewer_1 = Reviewer('Ronnie', 'Kirk')
reviewer_1.courses_attached += ['Java']

reviewer_2 = Reviewer('Ben', 'West')
reviewer_2.courses_attached += ['Python']

student_1.rate_lw(lecturer_1, 'Python', 9)
student_2.rate_lw(lecturer_2, 'Java', 10)

reviewer_1.rate_hw(student_1, 'Java', 9)
reviewer_2.rate_hw(student_2, 'Python', 10)


all_lecturer = [lecturer_1, lecturer_2]
def average_grades_lecturers(lecturers_list, course_name): # не понял как "в рамках конкретного курса" если оценки общие в 1 списке
    all_grades =[]
    for lecturer in lecturers_list:
        for courses in lecturer.courses_attached:
            if course_name in courses:
                for grade in lecturer.grades:
                    all_grades += [grade]
            elif course_name not in courses:
                pass
    print(f'Средняя оценка {round((sum(all_grades)) / len(all_grades), 1)}')

average_grades_lecturers(all_lecturer, 'Python')

all_students = [student_1, student_2]
def average_grades_students(students_list, course_name):
    all_grades = []
    for student in students_list:
        for key, values in student.grades.items():
            if key in course_name:
                all_grades += values
            elif key not in course_name:
                pass
    print((f'Средняя оценка за {course_name}: {round((sum(all_grades)) / len(all_grades), 1)}'))

average_grades_students(all_students, 'Java')
print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)
print(student_2 > student_1)
print(lecturer_2 < lecturer_1)





