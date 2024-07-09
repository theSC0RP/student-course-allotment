# Documentation for `student.py`

## Overview
The `Student` class in `student.py` is designed to represent a student and manage their course choices, including Major Domain Minors (MDMs), Open Electives (OEs), Honors, and Double Minors (DMs). It initializes a student with their respective data, processes their choices, and provides methods for assigning courses.

---

## Class Attributes
- **basic_fieldnames**: List of basic student attributes (e.g., name, department, email, roll_no, semester, etc.).
- **mdm_fieldnames**: List of field names for MDM choices.
- **hdm_fieldnames**: List of field names for Honor and DM choices.
- **oe_fieldnames**: List of field names for OE choices.
- **mdm_choices**: List of MDM choices sorted by preference.
- **hdm_choices**: List of Honor and DM choices sorted by preference.
- **oe_choices**: List of OE choices sorted by preference.
- **honor_choices**: List of Honor choices sorted by preference.
- **assigned_honor**: Assigned Honor course (initially `None`).
- **assigned_oes**: Assigned OE courses (initially `None`).
- **assigned_dm**: Assigned DM courses (initially `None`).
- **assigned_mdms**: Assigned MDM courses (initially `None`).
- **prev_oes**: List of previously assigned OE courses.
- **prev_mdms**: List of previously assigned MDM courses.
- **total_prev_same_branch_mdms**: Count of previously assigned MDMs from the same branch.
- **total_prev_different_branch_mdms**: Count of previously assigned MDMs from different branches.
- **is_computing_department**: Boolean indicating if the student belongs to a computing department.

---

## Constructor
Initializes a `Student` object with the provided data.

**Parameters:**
- `student_data`: Dictionary containing student data.
- `computing_mdms`: List of computing MDMs for determining if a student's MDMs are from computing departments.

**Initialization Process:**
- **Basic Attributes**: Initializes basic student attributes from the `student_data` dictionary.
- **Course Choices**: Processes and sorts the MDM, DM, OE, and Honor choices.
- **Previous Courses**: Initializes lists for previously assigned courses and counts for same branch and different branch MDMs.
- **Department Check**: Sets a boolean flag to indicate if the student belongs to a computing department.

---