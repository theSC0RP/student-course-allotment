from consts import basic_fieldnames, mdm_fieldnames, honor_fieldnames, dm_filednames, oe_fieldnames
from random import shuffle

def get_choices_sorted_list(chocies_dict, id_str):
  return list(dict(sorted(chocies_dict.items(), key=(lambda x:int(x[0].split(id_str)[1])))).values())

class Student:
  def __init__(self, student_data: dict):
    mdm_choices_dict = {}
    honor_choices_dict = {}
    dm_choices_dict = {}
    oe_choices_dict = {}

    self.mdm_choices = []
    self.dm_choices = []
    self.oe_choices = []
    self.honor_choices = []


    for key, value in student_data.items():
      if key in basic_fieldnames:
        setattr(self, key, value)
      
      elif key in mdm_fieldnames:
        mdm_choices_dict[key] = value

      elif key in honor_fieldnames:
        honor_choices_dict[key] = value

      elif key in dm_filednames:
        dm_choices_dict[key] = value

      elif key in oe_fieldnames:
        oe_choices_dict[key] = value


    self.mdm_choices = get_choices_sorted_list(mdm_choices_dict, "mdm_choice_")
    self.dm_choices = get_choices_sorted_list(dm_choices_dict, "dm_choice_")
    self.oe_choices = get_choices_sorted_list(oe_choices_dict, "oe_choice_")
    self.honor_choices = get_choices_sorted_list(honor_choices_dict, "honor_choice_")

    # TODO: Change this
    self.hdm_choices = self.dm_choices + self.honor_choices
    shuffle(self.hdm_choices)

      

    self.assigned_honor = None
    self.assigned_oes = None
    self.assigned_dm = None
    self.assigned_mdms = None



