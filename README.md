This application is created for VPKBIET (Vidya Pratishthan's Kamal Nayan Bajaj College of Engineering & Technology, Baramati) for course allotment process for multi-disciplinary minors, honors, double minors and open electives.
This repository can be used by any autonomous college for their allotment process.

### Specifications
Python: 3.12.1

### Setup
1. Create a virtual environment using `pipenv`
2. Install the dependencies from the requirements.txt file using `pip install -r requirements.txt`
3. Make necessary changes in the `consts.py` file
4. Run the driver using `python3 driver.py`
  a) Provide the csv file that contains the student data including their course preferences
  b) Select the course for which you want to do the allotment.
  c) Provide a filename to save the geneerated allotment csv files.
  d) The allotment file will be generated in the output directory

### Documentation
The detailed documentation for each file is in the documentation directory