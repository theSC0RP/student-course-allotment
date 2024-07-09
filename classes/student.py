from consts import basic_fieldnames, mdm_fieldnames, hdm_fieldnames, oe_fieldnames, rules
from random import shuffle

def get_choices_sorted_list(chocies_dict, id_str):
  return list(dict(sorted(chocies_dict.items(), key=(lambda x:int(x[0].split(id_str)[1])))).values())

class Student:
  def __init__(self, student_data: dict, computing_mdms: list):
    mdm_choices_dict = {}
    hdm_choices_dict = {}
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

      elif key in hdm_fieldnames:
        hdm_choices_dict[key] = value

      elif key in oe_fieldnames:
        oe_choices_dict[key] = value


    self.mdm_choices = get_choices_sorted_list(mdm_choices_dict, "mdm_choice_")
    self.hdm_choices = get_choices_sorted_list(hdm_choices_dict, "hdm_choice_")
    self.oe_choices = get_choices_sorted_list(oe_choices_dict, "oe_choice_")
      

    self.assigned_honor = None
    self.assigned_oes = None
    self.assigned_dm = None
    self.assigned_mdms = None
    self.prev_oes = []
    self.prev_mdms = []

    self.total_prev_same_branch_mdms = 0
    self.total_prev_different_branch_mdms = 0
    self.is_computing_department = True if self.department in rules['computing_departments'] else False
    

    for pmdm in self.prev_mdms:
      if self.is_computing_department:
        if pmdm in computing_mdms:  
          self.total_prev_same_branch_mdms += 1
        else: self.total_prev_different_branch_mdms += 1

      else:
        if pmdm not in computing_mdms:
          self.total_prev_same_branch_mdms += 1
        else: self.total_prev_different_branch_mdms += 1

  # def assign_mdms(self, mdm):
  #   pass

  # def assign_oe(self, oe):
  #   pass

  # def assign_hdms(self, hdm):
  #   pass
    
      
    



