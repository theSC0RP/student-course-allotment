class Department:
  def __init__(self, department_data):
    self.code = department_data['code']
    self.name = department_data['Name']
    self.courses = department_data['Courses']
    self.students = department_data['students']