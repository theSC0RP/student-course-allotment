from faker import Faker
import numpy as np

import datetime
import csv
import os
import sys


from consts import departments, mdms, open_electives, honors, double_minors, fieldnames
from random import randint, shuffle, random

fake = Faker('en_IN')

def get_random_department():
  return list(departments.keys())[randint(0, len(departments) - 1)]

def get_random_semester():
  return randint(3, 7)


def get_course_choices(course_type: str):
  course = {}
  if course_type == 'mdm':
    course = mdms
  elif course_type == 'honors':
    course = honors
  elif course_type == 'dm':
    course = double_minors
  elif course_type == 'oe':
    course = open_electives

  choices = list(course.keys())
  shuffle(choices)

  return choices

def get_credits_earned(is_all_clear: bool):
  # max_credits = rules['sem_wise_max_credits'][current_sem]
  max_credits = 44
  if is_all_clear:
    return max_credits
  else:
    return randint(0, 43)  


def get_cgpa():
  min_cgpa = 4.0
  max_cgpa = 10.0

  # Mean and standard deviation for the normal distribution
  mean = (min_cgpa + max_cgpa) / 2
  std_dev = (max_cgpa - min_cgpa) / 6  # 99.7% data within 3 standard deviations

  # Generate a random decimal following the normal distribution
  random_decimal = np.random.normal(mean, std_dev)

  # Clip the value to ensure it falls within the range
  cgpa = round(np.clip(random_decimal, min_cgpa, max_cgpa), 2)

  return cgpa


# def get_random_mdm():
#   return list(mdms.keys())[randint(0, total_mdms - 1)]

# def get_random_honor(dept):
#   valid_honors = []
#   if dept in computing_depts:
#     valid_honors.extend(departments_courses[dept]['HONORS'])

#     invalid_honors = []
#     for d in departments:
#       if d not in computing_depts:
#         invalid_honors.extend(departments_courses[d]['HONORS'])
#   else:
#     valid_honors = departments_courses[dept]['HONORS']
#     invalid_honors = []
#     for d in departments:
#       if d != dept:
#         invalid_honors.extend(departments_courses[d]['HONORS'])
  
#   random_val = randint(0, 9)
#   if random_val > 0:
#     if len(valid_honors) > 1:
#       return valid_honors[randint(0, len(valid_honors) - 1)]
#     else:
#       return valid_honors[0]
  
#   else:
#     return invalid_honors[randint(0, len(invalid_honors) - 1)]

# def get_random_double_minor(dept):
#   valid_dms, invalid_dms = [], []
#   for d in departments:
#     if d != dept:
#       if dept not in computing_depts or dept in computing_depts and d not in computing_depts:
#         valid_dms.extend(departments_courses[d]['DM'])
#       else:
#         invalid_dms.extend(departments_courses[d]['DM'])
#     else:
#       invalid_dms.extend(departments_courses[d]['DM'])

#   random_val = randint(0, 9)
#   return invalid_dms[randint(0, len(invalid_dms) - 1)] if random_val == 0 else valid_dms[randint(0, len(valid_dms) - 1)]

# def get_random_open_elective():
#   return list(open_electives.keys())[randint(0, total_open_electives - 1)]
rolls = [0]*8

if __name__ == '__main__':
  os.remove("student_choices.csv")

  with open('student_choices.csv', 'a', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    num_students = 600 if len(sys.argv) != 2 else int(sys.argv[1])-1
    for i in range(num_students):
      name = fake.name()
      dept = get_random_department()
      dept_num = int(dept[-1])
      rolls[dept_num-1] += 1
      year = datetime.date.today().year
      stud_roll = "EN{}0{}{}".format(year, dept_num, str(rolls[dept_num-1]).zfill(3))
      email = "{}.{}.{}@vpkbiet.org".format(".".join(name.lower().split(" ")[::-1]), departments[dept].lower(), year)
      semester = 3 #get_random_semester()
      is_all_clear = random() < 0.95 # 5% students won't have all clear
      is_all_clear_str = "YES" if is_all_clear else "NO"
      credits_earned = get_credits_earned(is_all_clear)
      cgpa = 0 if not is_all_clear else get_cgpa()
      
      
      if cgpa > 7.5:
        interested_in_honors = "YES" if random() < 0.8 else "NO" 
      else:
        interested_in_honors = "YES" if random() < 0.6 else "NO" 
      


      if cgpa > 7.5: 
        interested_in_dm = "YES" if random() < 0.2 else "NO" 
      else:
        interested_in_dm = "YES" if random() < 0.6 else "NO" 
        


      mdm_choices = get_course_choices('mdm')
      hdm_choices  =  get_course_choices('honors') + get_course_choices('dm')
      shuffle(hdm_choices)
      open_elective_choices = get_course_choices('oe')

      student_data = [name, dept, email, stud_roll, semester, is_all_clear_str, credits_earned, cgpa, interested_in_honors, interested_in_dm]
      student_data.extend(mdm_choices)
      student_data.extend(open_elective_choices)
      student_data.extend(hdm_choices)
      writer.writerow({k:v for k,v in zip(fieldnames, student_data)})

  

  # print("\nName: ", f_name, "\n")
  # print("Email: ", email, "\n")
  # print("Department: ", dept, "\n")
  # print("MDM: ", mdm_choices, "\n")
  # print("Honor: ", honor_choices, "\n")
  # print("Double Minor: ", double_minor_choices, "\n")
  # print("Open Elective: ", open_elective_choices, "\n")


