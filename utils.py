from consts import rules, departments_courses, mdms, open_electives, honors, double_minors
from classes.student import Student

def get_courses_with_less_seats(allotments):
  return [k for k, v in allotments.items() if len(v) < rules['min_students_in_class'] and len(v) > 0]

def remove_students_till_the_first_assigned_to_courses_with_less_seats(courses_with_less_seats, allotments):
  min_student_num = 999999
  for course in courses_with_less_seats:
    if min_student_num > allotments[course][0]:
      min_student_num = allotments[course][0]

  for course, stud_nums in allotments.items():
    if course in courses_with_less_seats:
      allotments[course] = []
    else:
      for i in range(len(stud_nums)):
        if stud_nums[i] >= min_student_num:
          allotments[course] = stud_nums[:i]
          break

  return min_student_num

def get_computing_mdms():
  computing_mdms = []
  for d in rules['computing_departments']:
    computing_mdms.extend(departments_courses[d]['MDM'])

  return computing_mdms


def get_hdm_studnets(students: list[Student]) -> list[Student]:
  return list(filter(lambda student: float(student.cgpa) >= 7.5 and (student.interested_in_honors or student.interested_in_dm), students))

def get_choices_list(students: list[Student], course_type: str):
  course_total_dict = {}

  
  if course_type == "mdm":
    choices_dict = {k:0 for k in range(len(mdms.keys()))}
    course_total_dict = {k:choices_dict.copy() for k in mdms.keys()}
  
  elif course_type == "oe":
    choices_dict = {k:0 for k in range(len(open_electives.keys()))}
    course_total_dict = {k:choices_dict.copy() for k in open_electives.keys()}

  elif course_type == "hdm":
    students = get_hdm_studnets(students)
    total_hdms = len(honors.keys()) + len(double_minors.keys())

    choices_dict = {k:0 for k in range(total_hdms)}

    course_total_dict = {k:choices_dict.copy() for k in honors.keys()}
    course_total_dict.update({k:choices_dict.copy() for k in double_minors.keys()})



  for student in students:    
    choices = getattr(student, f"{course_type}_choices")

    for i, c in enumerate(choices):
      course_total_dict[c][i] += 1


  return course_total_dict


