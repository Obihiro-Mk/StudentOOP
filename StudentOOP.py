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
        if not isinstance(other, Lecturer): # не понимаю как это тут работает, как обработать ошибки
            print("Неверный лектор")
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
        for course, value_grade in self.grades.items():
            total += value_grade
        average_grade = round((sum(total)) / len(total), 1)
        total_other = []
        for course_other, value_grade_other in other.grades.items():
            total_other += value_grade_other
        average_grade_other = round((sum(total_other)) / len(total_other), 1)
        if not isinstance(other, Student): # не понимаю как это тут работает, как обработать ошибки
            print("Неверный студент")
        return (average_grade < average_grade_other)

        # ошибка
        # print("Имя: ", self.name,
        #     "\nФамилия: ", self.surname,
        #     "\nСредняя оценка за домашнее задание: ", average_grade,
        #     "\nКурсы в процессе изучения: ", ", ".join(self.courses_in_progress),
        #     "\nЗавершенные курсы: ", ", ".join(self.finished_courses))

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

# print(student_1)
# print(student_2)
# print(lecturer_1)
# print(lecturer_2)
# print(reviewer_1)
# print(reviewer_2)
# print(student_1 > student_2)
# print(lecturer_1 < lecturer_2)





