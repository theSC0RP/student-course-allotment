from read_data import read_student_data
from allot_oes import allot_oes
from allot_hdms import allot_hdms
from allot_mdms import allot_mdms

if __name__ == "__main__":
  students = read_student_data()
  students = sorted(
    students, 
    key=lambda student: (
        not student.is_all_clear,  # Primary: All clear students first
        -float(student.cgpa) if student.is_all_clear else -int(student.credits_earned)  # Secondary: Sort by CGPA or credits earned
    ))

  honor_allotments, dm_allotments = allot_hdms(students)
  # print(honor_allotments, dm_allotments)
  print("\n\nFinal Allotments\n")
  print("Honors: ", {k:len(v) for k,v in honor_allotments.items()})
  print("Double Minors: ", {k:len(v) for k,v in dm_allotments.items()})

  total_students = 0
  for k,v in honor_allotments.items():
    total_students += len(v)
  for k,v in dm_allotments.items():
    total_students += len(v)
  print("Final Total Students: ", total_students)

  