departments = {
  "D1":"AIDS", 
  "D2":"COMP", 
  "D3":"IT", 
  "D4":"ENTC", 
  "D5":"CIVIL", 
  "D6":"MECH", 
  "D7":"ELECT",
  "D8":"FY"
}

mdms = {
  'MDM1': {'name': 'Artificial Intelligence and Machine Learning', 'prereqs': ['MDM19'], 'sem': 3, 'clashes': ['H1']},
  'MDM2': {'name': 'Data Science', 'prereqs': ['MDM19'], 'sem': 3, 'clashes': []}, 
  'MDM3': {'name': 'Generative AI','prereqs': ['MDM19'], 'sem': 5, 'clashes': []},
  'MDM4': {'name': 'Cloud Computing', 'prereqs': [], 'sem': 3, 'clashes': []}, 
  'MDM5': {'name': 'High Performance Computing', 'prereqs': [], 'sem': 5, 'clashes': []}, 
  'MDM6': {'name': 'Computer Graphics and Gaming', 'prereqs': [], 'sem': 3, 'clashes': []}, 
  'MDM7': {'name': 'Cyber Security', 'prereqs': [], 'sem': 3, 'clashes': ['R13', 'R32']}, 
  'MDM8': {'name': 'Full Stack Development', 'prereqs': [], 'sem': 3, 'clashes': []}, 
  'MDM9': {'name': 'Embedded Systems', 'prereqs': [], 'sem': 3, 'clashes': []}, 
  'MDM10': {'name': 'Drone Technology', 'prereqs': [], 'sem': 3, 'clashes': []}, 
  'MDM11': {'name': 'Internet of Things', 'prereqs': [], 'sem': 3, 'clashes': []}, 
  'MDM12': {'name': 'Waste Management', 'prereqs': [], 'sem': 3, 'clashes': []}, 
  'MDM13': {'name': 'Green building and smart cities', 'prereqs': [], 'sem': 3, 'clashes': []}, 
  'MDM14': {'name': '3-D Printing', 'prereqs': [], 'sem': 3, 'clashes': []}, 
  'MDM15': {'name': 'Robotics and Automation', 'prereqs': [], 'sem': 3, 'clashes': []}, 
  'MDM16': {'name': 'Solar Technology', 'prereqs': [], 'sem': 3, 'clashes': []}, 
  'MDM17': {'name': 'Industrial Automation', 'prereqs': [], 'sem': 3, 'clashes': []}, 
  'MDM18': {'name': 'Nano Technology', 'prereqs': [], 'sem': 3, 'clashes': []}, 
  'MDM19': {'name': 'Linear Algebra and Statistics', 'prereqs': [], 'sem': 3, 'clashes': []}
}

honors = {
  'H1': {'name': 'Computational Intelligence', 'prereqs': [], 'sem': 3},
  'H2': {'name': 'Data Science', 'prereqs': [], 'sem': 3}, 
  'H3': {'name': 'Generative AI','prereqs': [], 'sem': 3},
  'H4': {'name': '', 'prereqs': [], 'sem': 3}, 
  'H5': {'name': '', 'prereqs': [], 'sem': 5}, 
  'H6': {'name': '', 'prereqs': [], 'sem': 3}, 
  'H7': {'name': '', 'prereqs': [], 'sem': 3}, 
  'H8': {'name': '', 'prereqs': [], 'sem': 3}, 
  'H9': {'name': '', 'prereqs': [], 'sem': 3}, 
  'H10': {'name': '', 'prereqs': [], 'sem': 3}, 
  'H11': {'name': '', 'prereqs': [], 'sem': 3}, 
  'H12': {'name': '', 'prereqs': [], 'sem': 3}, 
  'H13': {'name': '', 'prereqs': [], 'sem': 3}, 
}

double_minors = {
  'DM1': {'name': 'Artificial Intelligence and Data Science', 'prereqs': [], 'sem': 3},
  'DM2': {'name': 'Cloud Computing and Virtulization', 'prereqs': [], 'sem': 3}, 
  'DM3': {'name': 'Full Stack Development','prereqs': [], 'sem': 3},
  'DM4': {'name': 'Embedded Systems and Real-Time OS', 'prereqs': [], 'sem': 3}, 
  'DM5': {'name': 'Municipal or Urabn Engineering', 'prereqs': [], 'sem': 3}, 
  'DM6': {'name': 'Ent Resource Planning', 'prereqs': [], 'sem': 3}, 
  'DM7': {'name': 'Digital Mfg and Robotics', 'prereqs': [], 'sem': 3}, 
  'DM8': {'name': 'Renewable Energy', 'prereqs': [], 'sem': 3}
}

open_electives_disribution = {
  "MGMT": ["E1","E2","E3","E4","E5","E6","E7"],
  "BIOTECH": ["E8, E9"],
  "LAW": ["E10","E11"],
  "SOCIAL-SC": ["E12", "E13"],
  "EDUCATION": ["E14", "E15"],
  "FINANCE": ["E16"],
  "OTHERS": ["E17", "E18", "E19"]
}


open_electives = {
  'E1': {'name': 'Digital Marketing', 'prereqs': [], 'sem': 3, 'clashes': []}, 
  'E2': {'name': 'Professional Leadership', 'prereqs': [], 'sem': 3, 'clashes': []}, 
  'E3': {'name': 'Organizational Behavior', 'prereqs': [], 'sem': 3, 'clashes': []}, 
  'E4': {'name': 'Industrial Management', 'prereqs': [], 'sem': 3, 'clashes': []}, 
  'E5': {'name': 'Disaster Management', 'prereqs': [], 'sem': 3, 'clashes': []}, 
  'E6': {'name': 'Energy Economics and Management', 'prereqs': [], 'sem': 3, 'clashes': []}, 
  'E7': {'name': 'Operations Research', 'prereqs': [], 'sem': 3, 'clashes': []}, 
  'E8': {'name': 'Bioinformatics', 'prereqs': [], 'sem': 3, 'clashes': []}, 
  'E9': {'name': 'Bitechnology', 'prereqs': [], 'sem': 3, 'clashes': []}, 
  'E10': {'name': 'Intellectual Property Rights', 'prereqs': [], 'sem': 3, 'clashes': []}, 
  'E11': {'name': 'Cyber Laws', 'prereqs': [], 'sem': 3, 'clashes': []}, 
  'E12': {'name': 'International Relations', 'prereqs': [], 'sem': 3, 'clashes': []}, 
  'E13': {'name': 'Universal Human Values', 'prereqs': [], 'sem': 3, 'clashes': []}, 
  'E14': {'name': 'Education Technology', 'prereqs': [], 'sem': 3, 'clashes': []}, 
  'E15': {'name': 'Design Thinking', 'prereqs': [], 'sem': 3, 'clashes': []}, 
  'E16': {'name': 'Accounting and Finance', 'prereqs': [], 'sem': 3, 'clashes': []}, 
  'E17': {'name': 'Sustainability and Climate Change', 'prereqs': [], 'sem': 3, 'clashes': []}, 
  'E18': {'name': 'Agriculture Tech', 'prereqs': [], 'sem': 3, 'clashes': []}, 
  'E19': {'name': 'Architectural Tech', 'prereqs': [], 'sem': 3, 'clashes': []}
}

departments_courses = {
  "D1": {
    "MDM": ['MDM1', 'MDM2', 'MDM3'],
    "HONORS": ['H1'],
    "DM": ['DM1']
  }, 
  "D2": {
    "MDM": ['MDM4', 'MDM5', 'MDM6'],
    "HONORS": ['H2', 'H3'],
    "DM": ['DM2']
  }, 
  "D3": {
    "MDM": ['MDM7', 'MDM8'],
    "HONORS": ['H4', 'H5'],
    "DM": ['DM3']
  }, 
  "D4": {
    "MDM": ['MDM9', 'MDM0', 'MDM11'],
    "HONORS": ['H6', 'H7'],
    "DM": ['DM4']
  }, 
  "D5": {
    "MDM": ['MDM12', 'MDM13'],
    "HONORS": ['H8', 'H9'],
    "DM": ['DM5']
  }, 
  "D6": {
    "MDM": ['MDM14', 'MDM15'],
    "HONORS": ['H10', 'H11'],
    "DM": ['DM6']
  },
  "D7": {
    "MDM": ['MDM16', 'MDM17'],
    "HONORS": ['H12', 'H13'],
    "DM": ['DM7', 'DM8'],
  }, 
  "D8": {
    "MDM": ['MDM18', 'MDM19'],
    "HONORS": [],
    "DM": []
  },  
}


rules = {
  "core_departments": ["D1", "D2", "D3"],
  "same_dept_mdms_allowed": {
    "core": 2,
    "others": 3
  },
  "sem_wise_max_credits": {
    1:22, 
    2:22,
    3:22,
    4:22,
    5:22,
    6:22,
    7:22
  },
  "number_of_allotment_semesters": 1,
  "max_students_in_class": 75,
  "min_students_in_class": 5
}


basic_fieldnames = ['name', 'department', 'email', 'roll_no', 'semester', 'is_all_clear', 'credits_earned', 'cgpa', 'interested_in_honors', 'interested_in_dm']
bool_fieldnames = ['is_all_clear', 'interested_in_honors', 'interested_in_dm']

mdm_fieldnames = []
for i in range(0,len(mdms)):
  mdm_fieldnames.append(f'mdm_choice_{i+1}')

honor_fieldnames = []
for i in range(0,len(honors)):
  honor_fieldnames.append(f'honor_choice_{i+1}')

dm_filednames = []
for i in range(0,len(double_minors)):
  dm_filednames.append(f'dm_choice_{i+1}')

oe_fieldnames = []
for i in range(0,len(open_electives)):
  oe_fieldnames.append(f'oe_choice_{i+1}')

fieldnames = basic_fieldnames + mdm_fieldnames + honor_fieldnames + dm_filednames + oe_fieldnames

