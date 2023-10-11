class Student:

  def __init__(self, name, r_no, cgpa):
    self.name = name
    self.r_no = r_no
    self.cgpa = cgpa


def sort_students(student_list):
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students


students = [
    Student("shaha", "Emuc112", 6.5),
    Student("shahama", "Emuc103", 8.9),
    Student("safrin", "Emuc104", 8.5),
]
sorted_students = sort_students(students)
for student in sorted_students:
  print("Name: {}, Roll_no: {}, CGPA: {}".format(student.name, student.r_no,
                                                 student.cgpa))
