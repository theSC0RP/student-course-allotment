class Course:
  def __init__(self, course_data) -> None:
    self.code = course_data['Code']
    self.name = course_data['Name']
    self.department = course_data['Department']
    