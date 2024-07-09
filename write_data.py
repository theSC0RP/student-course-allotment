import csv
import os
from classes.student import Student

def create_allotment_csv(allotments: dict, filename: str):
  with open("output/{}.csv".format(filename), mode='w', newline='') as file:
    writer = csv.writer(file)
    for course_id, student_ids in allotments.items():
      writer.writerow([course_id] + student_ids)

def create_choices_csv(student_choices: list[list], filename: str):
  choice_fields = ["Course | Choice Totals"]
  student_choice_values = list(student_choices.values())

  choice_fields.extend([v for v in student_choice_values[0].keys()])

  choices = []
  for k, v in student_choices.items():
    l = [k]
    l.extend(list(v.values()))
    choices.append(l)

  with open("output/{}.csv".format(filename), mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=choice_fields)
    writer.writeheader()

    for c in choices:
      writer.writerow({k:v for k,v in zip(choice_fields, c)})
