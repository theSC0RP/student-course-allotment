# Documentation for `consts.py`

## Overview
This document provides an overview of the data structures and rules used in the course allotment system for a university. The system manages departments, courses, students' choices, and allotment rules.


## Data Structures

### Departments
- **departments**: Dictionary mapping department codes to their names.

---

### Courses
- **course_types**: Dictionary mapping numeric identifiers to course types.
- **mdms**: Dictionary containing details of multidisciplinary minor courses, including prerequisites, semester, and clashes.
- **honors**: Dictionary containing details of honors courses, including prerequisites and semester.
- **double_minors**: Dictionary containing details of double minor courses, including prerequisites and semester.
- **open_electives**: Dictionary containing details of open electives, including prerequisites, semester, and clashes.
- **open_electives_distribution**: Dictionary mapping categories to the open elective codes.

---


### Departments & Courses Relationship
- **departments_courses**: Dictionary mapping departments to their respective mdms, honors, and double minor courses.

---

### Rules
- **rules**: Dictionary defining various rules for course allotment, including allowed courses, maximum credits, class size limits, etc.

---

### Field Names
- **basic_fieldnames, mdm_fieldnames, oe_fieldnames, hdm_fieldnames**: Lists of field names for various student data. These must match the headings from the CSV data file.

---
