from consts import rules

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

