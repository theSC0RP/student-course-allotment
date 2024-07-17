# Documentation for `allot_mdms.py`

## Overview
The `allot_mdms.py` script is designed to allocate students to various multidisciplinary minor (MDM) courses based on their preferences and the department-specific rules. The script ensures that students are assigned to courses while respecting seat limitations and departmental regulations.

---

## Functions

### 1. `allot_mdms(students: list[Student], computing_mdms: list)`
This function manages the entire allocation process for MDM courses. It interacts with helper functions to ensure courses are allotted according to student preferences and departmental rules.

**Parameters:**
- `students` (list[Student]): List of `Student` objects representing all students to be considered for MDM allocation.
- `computing_mdms` (list[str]): List of MDM course codes offered by computing departments.

**Returns:**
- `mdm_allotments` (dict): Mapping of MDM course codes to the list of student roll numbers allotted to each MDM course.

**Process:**
- Initializes MDM course allotments.
- Allocates courses to students based on their preferences.
- Identifies courses with fewer students than the minimum required and prompts the user to decide whether to reallocate seats.
- Handles reallocation by unassigning students from underpopulated courses and reassigning them.
- Converts the student indices to roll numbers in the final allotments.

---

### 2. `make_mdm_allotments(students: list[Student], mdm_allotments: dict, computing_mdms: list[str], mdms_with_less_seats = [])`
This helper function performs the actual allocation of MDMs to students based on their choices.

**Parameters:**
- `students` (list[Student]): List of students to be allotted MDMs.
- `mdm_allotments` (dict): Dictionary to store MDM course allotments.
- `computing_mdms` (list[str]): List of MDM course codes offered by computing departments.
- `mdms_with_less_seats` (list[str], optional): List of MDMs that should be excluded from consideration due to having fewer students.

**Process:**
- Iterates through students, checking their MDM preferences against seat availability and departmental rules.
- Allocates students to the first available MDM that matches their preferences and follows branch rules.

---

### 3. `get_does_mdm_follow_branch_rules(student: Student, mdm: str, computing_mdms: list[str])`
This helper function checks if a given MDM follows the branch-specific rules for a student.

**Parameters:**
- `student` (Student): The student object being considered for MDM allocation.
- `mdm` (str): The MDM course code being checked.
- `computing_mdms` (list[str]): List of MDM course codes offered by computing departments.

**Returns:**
- `bool`: True if the MDM follows the branch-specific rules for the student, otherwise False.

**Process:**
- Checks if the student is from a computing or non-computing department.
- Verifies if the MDM follows the allowed number of same-branch and total MDMs for the student based on their department.

---

### 4. `are_course_prereqs_satisfied(student: Student, mdm_prereqs: list[str])`
This helper function checks if the pre-requisite courses are completed by the student.

**Parameters:**
- `student` (Student): The student object being considered for MDM allocation.
- `mdm_prereqs` (list[str]): List of MDM course codes that are pre-requisites for a course.

**Returns:**
- `bool`: True if the student has completed the pre-requisite courses, otherwise False.

**Process:**
- Returns True if the length of intersection between the student's previous mdm list (prev_mdms) and the mdm_prereqs is equal to the mdm_prereqs, otherwise False.

---

