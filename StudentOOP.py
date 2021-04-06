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
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {round((sum(self.grades)) / len(self.grades), 1)}'

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

        # ошибка
        # print("Имя: ", self.name,
        #     "\nФамилия: ", self.surname,
        #     "\nСредняя оценка за домашнее задание: ", average_grade,
        #     "\nКурсы в процессе изучения: ", ", ".join(self.courses_in_progress),
        #     "\nЗавершенные курсы: ", ", ".join(self.finished_courses))

student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Java']

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']

reviewer_1 = Reviewer('Ronnie', 'Kirk')
reviewer_1.courses_attached += ['Java']
print(reviewer_1)


student_1.rate_lw(cool_lecturer, 'Python', 9)
student_1.rate_lw(cool_lecturer, 'Python', 10)
student_1.rate_lw(cool_lecturer, 'Python', 5)
student_1.rate_lw(cool_lecturer, 'Python', 10)
print(cool_lecturer)

reviewer_1.rate_hw(student_1, 'Java', 9)
reviewer_1.rate_hw(student_1, 'Java', 10)
reviewer_1.rate_hw(student_1, 'Java', 5)
reviewer_1.rate_hw(student_1, 'Java', 3)
print(student_1)

best_student = Student('Petya', 'Ivanov', 'your_gender')
best_student.finished_courses += ['Git']
best_student.finished_courses += ['Java']
best_student.finished_courses += ['Введение в программирование']
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Что-то']
best_student.grades['Git'] = [10, 10, 3, 10, 5]
best_student.grades['Python'] = [10, 7, 5, 6, 7]
print(best_student)

