AI Resume Updater

A lightweight resume-tailoring application that analyzes a job description, extracts relevant skills, responsibilities, qualifications, projects, and languages, and uses them to update a text-based resume. The project includes a Python resume-processing module and a Streamlit web interface for uploading a resume and providing a job description.

Status: This is a local-development/demo project. It is intended to run on one machine and currently works with plain-text (.txt) resumes. Review the limitations and security notes before using it with real personal information.

Contents

Features

Technology stack

Architecture

Prerequisites

Installation

Run locally

Input and output

Resume updating workflow

Project structure

Troubleshooting

Limitations and security notes

Features

Upload a resume in .txt format through the Streamlit interface.

Accept a job description as pasted text.

Classify job-description content into:

Technical skills

Responsibilities

Qualifications

Projects

Languages

Remove duplicate extracted items.

Add relevant job-description skills to the resume.

Generate or update a resume summary based on extracted skills.

Merge relevant responsibilities, project information, qualifications, and languages into matching resume sections.

Add a project description when the Projects section does not already contain one.

Maintain a standard resume section order:
Summary → Technical Skills → Experience → Projects → Education → Languages

Download the updated resume as a .txt file from the Streamlit interface.

Also provide a standalone Python module for resume updating.

Technology stack

Language: Python

Web framework: Streamlit

Text processing: Python standard library (os, re)

Input format: Plain-text .txt

Output format: Plain-text .txt

Development environment: VS Code or any Python-compatible IDE

Architecture

The project contains two main Python components:

Component

Responsibility

RESUME_UPDATER.py

Contains the resume-processing and job-description analysis logic

resume_app.py

Provides the Streamlit web interface

The basic flow is:

Resume (.txt)
      |
      v
Streamlit Web Interface
      |
      +----------------------+
      |                      |
      v                      v
Resume Text          Job Description
      |                      |
      +----------+-----------+
                 |
                 v
        Resume Updater Logic
                 |
                 v
       JD Classification
                 |
        +--------+--------+
        |        |        |
      Skills  Duties  Qualifications
        |        |        |
        +--------+--------+
                 |
                 v
       Resume Section Update
                 |
                 v
        Updated Resume
                 |
                 v
       Download .txt File

Prerequisites

Install the following before running the project:

Python 3.9 or later

pip

Streamlit

VS Code or another Python IDE

Check the Python installation:

python --version

Check pip:

pip --version

Installation

1. Clone or extract the project

Place the project in a convenient local folder.

Example:

cd C:\path\to\project

2. Install Streamlit

Run:

pip install streamlit

If a requirements.txt file is added later, the recommended installation command is:

pip install -r requirements.txt

Run locally

Open PowerShell or the VS Code terminal in the project folder.

Start the Streamlit application

Run:

streamlit run resume_app.py

Streamlit will display a local URL in the terminal. Open that URL in a browser.

The application provides:

Resume upload

Job description input

Resume update button

Updated-resume download option

Typical workflow

1. Start Streamlit
        |
2. Upload resume.txt
        |
3. Paste job description
        |
4. Click "Update Resume"
        |
5. Resume is processed
        |
6. Download updated_resume.txt

Input and output

Resume input

The current application accepts:

.txt

Example:

John Doe

Summary
Software engineering student with programming experience.

Technical Skills
Python
Java
SQL

Projects
Resume Management System

Education
Bachelor of Engineering in Computer Science

Job description input

Paste the complete job description into the Job Description text area.

The updater searches the text for keywords related to skills, responsibilities, qualifications, projects, and languages.

Output

The generated file is:

updated_resume.txt

The Streamlit interface provides a download button after successful processing.

Resume updating workflow

The core processing is implemented in RESUME_UPDATER.py.

1. Load resume

The application reads the supplied resume text and prepares it for processing.

2. Analyze the job description

Each non-empty job-description line is examined and classified using keyword-based rules.

Examples of skill-related keywords include:

Python
Java
C++
SQL
React
JavaScript
Node.js
AWS
Azure
GCP
API
Testing
Cloud

Responsibility-related keywords include terms such as:

develop
implement
design
maintain
test
execute
collaborate
debug

Qualification-related terms include:

bachelor
degree
qualification
certification
graduate

3. Build job-description sections

The extracted information is grouped into:

skills
responsibilities
qualifications
projects
languages

Duplicate entries are removed.

4. Update the summary

A summary is generated using the extracted job-related skills. If an existing Summary or Career Objective section is detected, it is replaced with the generated summary.

5. Merge relevant information

Extracted information is added to matching resume sections such as:

Technical Skills
Experience
Projects
Education
Languages

Long job-description lines are skipped when they exceed the configured word limit.

6. Enhance projects

If the resume contains a Projects section without existing bullet descriptions, the updater can add a short project description using extracted skills.

7. Enforce resume structure

The final resume is organized using the following section order:

Summary
Technical Skills
Experience
Projects
Education
Languages

8. Generate the updated resume

The processed resume is returned as text and made available through the Streamlit download button.

Project structure

RESUMEUPDATER-main/
│
├── RESUME_UPDATER.py       # Resume processing and JD analysis logic
├── resume_app.py            # Streamlit web application
└── README.md                # Project documentation

Main functions

load_text()

Reads the contents of a text file.

extract_sections()

Analyzes the job description and groups lines into relevant categories.

classify_jd_line()

Determines which resume category a job-description line belongs to.

boost_summary()

Creates or updates the resume summary using extracted job-related skills.

merge_into_section()

Adds relevant job-description information to an existing resume section.

enhance_projects()

Adds a short project description when the Projects section lacks descriptions.

enforce_structure()

Organizes the resume into the expected section order.

update_resume()

Coordinates the complete resume-updating process.

Troubleshooting

streamlit is not recognized

Install Streamlit:

pip install streamlit

Then run:

python -m streamlit run resume_app.py

Python is not recognized

Verify that Python is installed and added to the system PATH:

python --version

If the command fails, install Python and enable the Add Python to PATH option.

Resume upload is rejected

The current Streamlit interface accepts only .txt files. Convert the resume to plain text before uploading.

No updated resume is generated

Make sure:

A resume file has been uploaded.

The job description text area is not empty.

The Streamlit application is still running.

The terminal does not show a Python exception.

Job description information is not added as expected

The current implementation uses keyword-based classification. A line that does not contain one of the configured keywords may not be assigned to a resume section.

Resume formatting changes unexpectedly

The current project processes plain text using regular expressions and section-based text manipulation. It is not a Word/PDF formatting engine, so complex formatting is not preserved.

Limitations

The current application supports .txt resumes rather than .pdf or .docx.

Job-description analysis is based on predefined keyword rules rather than a machine-learning or large-language-model pipeline.

The system does not independently verify whether a skill is actually present in the candidate's experience.

Extracted job-description information may need manual review before being used in a final resume.

Complex resume layouts, tables, images, columns, and formatting are not supported.

The application is intended as a resume-tailoring/demo project rather than a complete automated recruitment system.

Security and privacy notes

This project may process personal information contained in resumes. Do not upload sensitive resumes to an application or machine that you do not trust.

The project is designed for local development. Before deploying it to a public server:

Add appropriate authentication and authorization.

Validate uploaded files.

Restrict file size and file types.

Avoid storing resumes longer than necessary.

Protect temporary and generated files.

Review logging so that personal information is not exposed.

Use secure deployment and HTTPS configuration.

Do not commit resumes, personal information, credentials, or generated output files to Git.

Future enhancements

Possible extensions include:

PDF and DOCX resume support

Skill matching and keyword scoring

Job-description/resume similarity scoring

AI-based resume rewriting

ATS compatibility analysis

Missing-skill detection

Resume formatting and template support

Multiple resume versions for different job descriptions

Secure cloud deployment

Database-backed resume history
