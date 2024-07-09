# Documentation for `allot_hdms.py`

## Overview
The `allot_hdms.py` script is designed to allocate students to various honors and double minor (HDM) courses based on their preferences and the department-specific rules. The script ensures that students are assigned to courses while respecting seat limitations and departmental regulations.

---

## Functions

### 1. `allot_hdms(students: list[Student])`
This function manages the entire allocation process for honors and double minor courses. It interacts with helper functions to ensure courses are allotted according to student preferences and departmental rules.

**Parameters:**
- `students` (list[Student]): List of `Student` objects representing all students to be considered for HDM allocation.

**Returns:**
- A tuple containing two dictionaries:
  - `honor_allotments`: Mapping of honor course codes to the list of student roll numbers allotted to each honor course.
  - `dm_allotments`: Mapping of double minor course codes to the list of student roll numbers allotted to each double minor course.

**Process:**
- Initializes department-wise allowed HDMs and collects eligible students.
- Allocates courses to students based on their preferences.
- Identifies courses with fewer students than the minimum required and prompts the user to decide whether to reallocate seats.
- Handles reallocation by unassigning students from underpopulated courses and reassigning them.
- Converts the student indices to roll numbers in the final allotments.

---

### 2. `make_hdm_allotments(students, department_wise_allowed_hdms, honor_allotments, dm_allotments, disallowed_hdms = [])`
This helper function performs the actual allocation of HDMs to students based on their choices.

**Parameters:**
- `students` (list): List of students to be allotted HDMs.
- `department_wise_allowed_hdms` (dict): Dictionary containing allowed HDMs for each department.
- `honor_allotments` (dict): Dictionary to store honor course allotments.
- `dm_allotments` (dict): Dictionary to store double minor course allotments.
- `disallowed_hdms` (list): List of HDMs that should be excluded from consideration.

**Process:**
- Updates allowed HDMs by removing disallowed ones.
- Iterates through students, checking their HDM preferences against the allowed HDMs and seat availability.
- Allocates students to the first available HDM that matches their preferences.

---

### 3. `get_department_wise_allowed_hdms()`
This helper function constructs a dictionary of allowed HDMs for each department, based on predefined rules and departmental courses.

**Returns:**
- `department_wise_allowed_hdms` (dict): A dictionary where keys are department names and values are lists of allowed HDMs (both honors and double minors) for that department.

**Process:**
- Compiles a list of all double minors and computing-specific honors and double minors.
- Constructs the list of allowed HDMs for each department by differentiating between computing and non-computing departments.
- Merges honors and double minor courses into a single list for each department.

---

### Additional Utilities
The script uses utility functions (imported but not defined within this file):
- `get_courses_with_less_seats`: Identifies courses with fewer than the minimum required students.
- `remove_students_till_the_first_assigned_to_courses_with_less_seats`: Unassigns students from courses that don't meet the minimum seat requirement.
- `get_hdm_studnets`: Retrieves the list of students eligible for HDM courses.


---