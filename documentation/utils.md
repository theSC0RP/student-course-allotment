## Documentation for `utils.py`

### Overview
The `utils.py` file contains utility functions to support the process of course allotment for students. It includes functions for determining courses with fewer students, removing students from courses to balance class sizes, retrieving computing MDMs, filtering students eligible for Honors and Double Minors, and generating lists of course choices.

---

### Functions

#### 1. `get_courses_with_less_seats(allotments)`
Identifies courses that have fewer students than the minimum required seats.

**Parameters:**
- `allotments`: Dictionary where keys are course codes and values are lists of student numbers assigned to those courses.

**Returns:**
- List of course codes: Courses with fewer students than the minimum required seats.

---

#### 2. `remove_students_till_the_first_assigned_to_courses_with_less_seats(courses_with_less_seats, allotments)`
Removes students from courses until the first student assigned to any of the courses with fewer seats is reached.

**Parameters:**
- `courses_with_less_seats`: List of courses identified as having fewer seats.
- `allotments`: Dictionary where keys are course codes and values are lists of student numbers assigned to those courses.

**Returns:**
- `min_student_num`: The minimum student number among those removed.

---

#### 3. `get_computing_mdms()`
Retrieves a list of all MDMs offered by computing departments.

**Parameters:**
- None

**Returns:**
- List of computing MDMs: MDMs offered by computing departments.

---

#### 4. `get_hdm_studnets(students)`
Filters and returns students eligible for Honors and Double Minors based on their CGPA and interest.

**Parameters:**
- `students`: List of Student objects.

**Returns:**
- List of eligible students: Students with CGPA >= 7.5 who are interested in Honors or Double Minors.

---

#### 5. `get_choices_list(students, course_type)`
Generates a dictionary representing the total number of choices each course received, broken down by choice preference.

**Parameters:**
- `students`: List of Student objects.
- `course_type`: Type of course (e.g., "mdm", "oe", "hdm").

**Returns:**
- `course_total_dict`: Dictionary with course codes as keys and another dictionary as values. The inner dictionary contains choice preference (e.g., 1st choice, 2nd choice) as keys and the number of students who made that choice as values.

---