# Documentation for `allot_oes.py`

## Overview
The `allot_oes.py` script is designed to allocate students to various Open Elective (OE) courses based on their preferences and the departmental rules. The script ensures that students are assigned to courses while respecting seat limitations and departmental regulations.

---

## Functions

### 1. `allot_oes(students: list[Student])`
This function manages the entire allocation process for Open Elective (OE) courses. It interacts with helper functions to ensure courses are allotted according to student preferences and departmental rules.

**Parameters:**
- `students` (list[Student]): List of `Student` objects representing all students to be considered for OE allocation.

**Returns:**
- `oe_allotments` (dict): Mapping of OE course codes to the list of student roll numbers allotted to each OE course.

**Process:**
- Initializes OE course allotments.
- Allocates courses to students based on their preferences.
- Identifies courses with fewer students than the minimum required and prompts the user to decide whether to reallocate seats.
- Handles reallocation by unassigning students from underpopulated courses and reassigning them.
- Converts the student indices to roll numbers in the final allotments.

---

### 2. `make_oe_allotments(students: list[Student], oe_allotments: dict, disallowed_oes: list[str] = [])`
This helper function performs the actual allocation of OEs to students based on their choices.

**Parameters:**
- `students` (list[Student]): List of students to be allotted OEs.
- `oe_allotments` (dict): Dictionary to store OE course allotments.
- `disallowed_oes` (list[str], optional): List of OE courses that should be excluded from consideration due to having fewer students or being previously allotted.

**Process:**
- Iterates through students, checking their OE preferences against seat availability and previously allotted courses.
- Allocates students to the first available OE that matches their preferences and is not disallowed.

---

