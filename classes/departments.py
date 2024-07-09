from department import Department

class Departments:
  def __init__(self, departments: list[Department]):
    self.departments = {d.code:d for d in departments}

  def get_department(self, code: str) -> Department:
    return self.departments.get(code)
  
  def get_departments(self, codes:list[str]) -> list[Department]:
    return [self.get_department(code) for code in codes]