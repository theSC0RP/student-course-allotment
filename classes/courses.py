from course import Course

class Courses:
  def __init__(self, courses:list[Course]):
    self.courses = {c.code:c for c in courses}

  def get_course(self, code: str) -> Course:
    return self.courses.get(code)
  
  def get_courses(self, codes: list[str]) -> list[Course]:
    return [self.get_course(code) for code in codes]