import os
from datetime import datetime

from read_data import read_student_data
from allot_oes import allot_oes
from allot_hdms import allot_hdms
from allot_mdms import allot_mdms
from utils import get_computing_mdms, get_choices_list
from write_data import create_allotment_csv, create_choices_csv
from consts import course_types


if __name__ == "__main__":
  datafile_path = "student_choices.csv"
  datafile_path = input("Enter the data file name (path): ")
  if not os.path.exists(datafile_path):
    print(f"Data file not found at '{datafile_path}'")
    exit(1)


  computing_mdms = get_computing_mdms()
  students = read_student_data(datafile_path, computing_mdms)
  students = sorted(
    students, 
    key=lambda student: (
        not student.is_all_clear,  # Primary: All clear students first
        -float(student.cgpa) if student.is_all_clear else -int(student.credits_earned)  # Secondary: Sort by CGPA or credits earned
    ))

  course_number_choice = 0
  is_course_type_choice_valid = False

  while not is_course_type_choice_valid:
    print("\n\nPress 1 - Open Electives (OE)")
    print("Press 2 - Honors and Double Majors (HDM)")
    print("Press 3 - Multidisciplinary Minor (MDM)")
    course_number_choice = int(input("Select course type: "))
    print()
    if course_number_choice < 1 or course_number_choice > 3:
      print("Invalid choice!")
      print("Please select a valid course type number [1, 2, 3]")
      is_course_type_choice_valid = False
    else:
      is_course_type_choice_valid = True

  course_type = course_types[course_number_choice]

  filename = input("\nEnter the filename for saving the allotments: ") 
  while os.path.exists("{}_{}_allotments.csv".format(filename, course_type)):
    print(f"File {filename} already exists!")
    request_new_filename = input("Press Y to to enter a new filename (otherwise a random unique identifier will be added in the end): ")
    
    if request_new_filename == 'y' or request_new_filename == 'Y':
      filename = input("Enter new filename: ")
    else: filename += "_" + str(datetime.now().timestamp()).replace(".", "")

  allotments = {}
  if course_number_choice == 1:
    allotments = allot_oes(students)
  elif course_number_choice == 2:
    honor_allotments, dm_allotments = allot_hdms(students)
    honor_allotments.update(dm_allotments)
    allotments = honor_allotments
  elif course_number_choice == 3:
    allotments = allot_mdms(students,computing_mdms)

  create_allotment_csv(allotments, filename + f"_{course_type}_allotments")
  create_choices_csv(get_choices_list(students, course_type), filename + f"_{course_type}_choices")



  