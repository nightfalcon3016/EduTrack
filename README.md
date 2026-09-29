# EduTrack

## Student Academic Performance & Eligibility Analyzer

EduTrack is a Python command-line application developed to analyze student academic performance and eligibility.

The application collects student information, subject marks, attendance, previous academic information, and backlog details. It then performs academic calculations and provides performance, attendance, risk, explanation, recommendation, and CGPA analysis.

## Features

- Student profile creation
- Subject-wise marks and grade calculation
- Grade point calculation
- SGPA calculation
- CGPA calculation
- Attendance percentage calculation
- Attendance eligibility analysis
- Attendance safe-zone analysis
- Subject performance ranking
- Strong subject identification
- Subjects requiring attention
- Academic risk analysis
- Academic performance explanation
- Academic recommendations
- CGPA target simulation
- Academic dashboard
- Academic history
- JSON-based record storage
- Input validation and error handling

## Subjects

| Subject | Credits |
| Physics | 4 |
| Chemistry | 4 |
| Mathematics | 4 |
| English | 3 |
| UHV | 1 |

Subject credits are predefined in the program and do not need to be entered by the user.

## Technology Used

- Python
- JSON
- Command Line Interface
- Git
- GitHub

No external Python packages are required.

## Project Structure


EduTrack/
├── main.py
├── student.py
├── academic.py
├── academic_analyzer.py
├── attendance_analyzer.py
├── cgpa_simulator.py
├── risk_analyzer.py
├── explanation_engine.py
├── recommendation_engine.py
├── dashboard.py
├── storage.py
└── data/
    └── students.json

## Module Description

| File | Purpose |
| main.py | Controls the main program and menu |
| student.py | Creates and validates the student profile |
| academic.py | Collects and validates academic information |
| academic_analyzer.py | Calculates grades, SGPA, and CGPA |
| attendance_analyzer.py | Calculates attendance and eligibility |
| cgpa_simulator.py | Simulates CGPA targets and future performance |
| risk_analyzer.py | Identifies academic risk factors |
| explanation_engine.py | Explains academic results |
| recommendation_engine.py | Generates academic recommendations |
| dashboard.py | Displays the academic dashboard |
| storage.py | Handles JSON storage and academic history |

## Application Workflow


Student Profile
      |
      v
Academic Information
      |
      v
Marks + Attendance + Backlogs
      |
      v
Academic Performance Analysis
      |
      v
Grades + SGPA + CGPA
      |
      v
Attendance Analysis
      |
      v
Academic Risk Analysis
      |
      v
Performance Explanation
      |
      v
Academic Recommendations
      |
      v
Academic Dashboard
      |
      v
JSON Storage
      |
      v
Academic History


## Running the Project

### Requirements

- Python 3
- Windows, Linux, or macOS
- Command-line terminal

### Check Python Installation


python --version


### Run the Application

Open a terminal in the project directory:


cd EduTrack

Run the application:

python main.py


### Main Menu


1. Create Student Profile
2. Enter Academic Information
3. Academic Performance Analysis
4. Attendance Compliance & Safe-Zone Analyzer
5. CGPA Goal & Performance Simulator
6. Academic Risk Analysis
7. Academic Performance Explanation
8. Academic Recommendations
9. Academic Dashboard
10. Academic History
0. Exit


## Input Details

The application asks for:

- Student Name
- Registration Number
- Semester
- Marks for each subject
- Classes attended
- Total classes
- Previous CGPA for later semesters
- Completed credits before the current semester
- Backlog information

Subject names and credits are already configured in the program.

## Data Storage

Academic records are stored locally in:


data/students.json


The application uses JSON to store and retrieve academic records.

## Input Validation

The application validates:

- Semester values
- Subject marks
- Attendance values
- Classes attended
- Total classes
- Previous CGPA
- Backlog input
- Menu selections

Invalid input is rejected and the user is asked to enter a valid value.

## Academic Analysis

### Academic Performance Analysis

The system calculates:

- Subject grades
- Grade points
- SGPA
- Current CGPA
- Subject ranking
- Strong subjects
- Subjects requiring attention

### Attendance Compliance & Safe-Zone Analysis

The system calculates:

- Attendance percentage
- Attendance eligibility status
- Classes required to reach the configured threshold
- Maximum additional absences within the safe zone

### Academic Risk Analysis

The system considers:

- Attendance status
- Academic backlogs
- Current SGPA
- Subjects requiring attention

The identified risk factors are classified as:

- Low
- Moderate
- High

### Academic Performance Explanation

The explanation engine explains the calculated academic results using attendance, SGPA, subject performance, and backlog information.

### Academic Recommendations

The recommendation engine provides academic priorities based on attendance, performance, backlogs, and identified risk factors.

### CGPA Goal & Performance Simulation

The simulator allows the student to enter a target CGPA and calculates the required future SGPA when possible. It also displays projected CGPA values for different future SGPA scenarios.

### Academic Dashboard

The dashboard provides a consolidated view of:

- Student information
- SGPA
- Current CGPA
- Attendance
- Attendance status
- Academic risk
- Subject performance
- Strong subjects
- Subjects requiring attention
- Backlogs
- Attendance safe zone

### Academic History

Academic records are saved in JSON format and can be retrieved using the student's registration number. Semester-wise academic information can be viewed from previously saved records.

## CSE1021 Concepts Used

The project applies concepts from Introduction to Problem Solving and Programming, including:

- Problem decomposition
- Algorithm design
- Functions
- Parameters and arguments
- Conditional statements
- Loops
- Lists
- Dictionaries
- Sorting
- Searching
- Numerical calculations
- Input validation
- File handling
- JSON data representation

## Testing

The application was tested using:

- Semester 1 student data
- Later-semester academic data
- High marks
- Low marks
- Full attendance
- Attendance below the configured threshold
- Backlog conditions
- Invalid marks
- Invalid CGPA values
- Invalid semester values
- Academic history retrieval
- CGPA simulation scenarios

## Future Improvements

- Semester performance trend analysis
- Configurable subject structures
- Academic report export
- Additional CGPA simulation scenarios
- More detailed historical analysis
- Additional academic performance metrics

## Project Type

EduTrack is a command-line student academic performance and eligibility analysis project developed using Python.



