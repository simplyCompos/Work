print("Enter number of subjects")
NumSubjects = int(input())
class Student:
    def __init__(self, name, surname, grades):
        self.name = name
        self.surname = surname
        self.grades = grades
    def average(self):
        return sum(self.grades) / len(self.grades) 
students = []
print("Enter the number of students")
n = int(input())
for i in range(n):
    print(f"\nStudent {i + 1}")
    print("Enter name")
    name = input()
    print("Enter surname")
    surname = input()
    grades =[]
    for j in range(NumSubjects):
        print(f"Grade from {j + 1}: ")
        grade = int(input())
        grades.append(grade)
    students.append(Student(name, surname, grades))
print("\nSrudents Table")
print("Surname Name and average grade")
print("-" *30)
for s in students:
    print(f"{s.surname} {s.name} {s.average():.2f}")
print("\nAverage gradeof group from every subject: ")
for subj in range(NumSubjects):
    total = 0
    for s in students:
        total += s.grades[subj]
    avg = total / len(students)
    print(f"Subject {subj + 1}: {avg:.2f}")
