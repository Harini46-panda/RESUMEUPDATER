# AI Resume Updater

A lightweight resume-tailoring application that analyzes a job description, extracts relevant skills, responsibilities, qualifications, projects, and languages, and uses them to update a text-based resume. The project includes a Python resume-processing module and a Streamlit web interface for uploading a resume and providing a job description.

**Status:** This is a local-development/demo project. It is intended to run on one machine and currently works with plain-text (`.txt`) resumes. Review the limitations and security notes before using it with real personal information.

## Contents

* Features
* Technology Stack
* Architecture
* Prerequisites
* Installation
* Run Locally
* Input and Output
* Resume Updating Workflow
* Project Structure
* Main Functions
* Troubleshooting
* Limitations
* Security and Privacy Notes
* Future Enhancements

## Features

* Upload a resume in `.txt` format through the Streamlit interface.
* Accept a job description as pasted text.
* Classify job-description content into:

  * Technical Skills
  * Responsibilities
  * Qualifications
  * Projects
  * Languages
* Remove duplicate extracted items.
* Add relevant job-description skills to the resume.
* Generate or update a resume summary based on extracted skills.
* Merge relevant responsibilities, project information, qualifications, and languages into matching resume sections.
* Add a project description when the Projects section does not already contain one.
* Maintain a standard resume section order:
  `Summary → Technical Skills → Experience → Projects → Education → Languages`
* Download the updated resume as a `.txt` file.
* Provide a standalone Python module for resume updating.

## Technology Stack

* **Language:** Python
* **Web Framework:** Streamlit
* **Text Processing:** Python Standard Library (`os`, `re`)
* **Input Format:** Plain-text `.txt`
* **Output Format:** Plain-text `.txt`
* **Development Environment:** VS Code or any Python-compatible IDE

## Architecture

The project contains two main Python components:

| Component           | Responsibility                                       |
| ------------------- | ---------------------------------------------------- |
| `RESUME_UPDATER.py` | Resume processing and job-description analysis logic |
| `resume_app.py`     | Streamlit web application                            |

The basic workflow is:

```text
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
       Job Description Analysis
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
```

## Prerequisites

Install the following before running the project:

* Python 3.9 or later
* pip
* Streamlit
* VS Code or another Python IDE

Check the Python installation:

```powershell
python --version
```

Check pip:

```powershell
pip --version
```

## Installation

### 1. Extract or Clone the Project

Place the project in a convenient local folder.

Example:

```powershell
cd C:\path\to\RESUMEUPDATER-main
```

### 2. Install Streamlit

Run:

```powershell
pip install streamlit
```

If a `requirements.txt` file is available, use:

```powershell
pip install -r requirements.txt
```

## Run Locally

Open PowerShell or the VS Code terminal in the project folder.

### Start the Streamlit Application

Run:

```powershell
streamlit run resume_app.py
```

Streamlit will display a local URL in the terminal. Open the displayed URL in a browser.

The application provides:

1. Resume upload
2. Job description input
3. Resume update option
4. Updated-resume download option

### Typical Workflow

```text
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
```

## Input and Output

### Resume Input

The current application accepts:

```text
.txt
```

Example:

```text
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
```

### Job Description Input

Paste the complete job description into the Job Description text area.

The updater analyzes the text and identifies information related to skills, responsibilities, qualifications, projects, and languages.

### Output

The generated file is:

```text
updated_resume.txt
```

The Streamlit interface provides a download button after successful processing.

## Resume Updating Workflow

The core processing is implemented in `RESUME_UPDATER.py`.

### 1. Load Resume

The application reads the supplied resume text and prepares it for processing.

### 2. Analyze the Job Description

Each non-empty job-description line is examined and classified using keyword-based rules.

Examples of skill-related keywords include:

```text
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
```

Responsibility-related keywords include terms such as:

```text
develop
implement
design
maintain
test
execute
collaborate
debug
```

Qualification-related terms include:

```text
bachelor
degree
qualification
certification
graduate
```

### 3. Build Job Description Sections

The extracted information is grouped into:

```text
skills
responsibilities
qualifications
projects
languages
```

Duplicate entries are removed.

### 4. Update the Summary

A summary is generated using the extracted job-related skills. If an existing `Summary` or `Career Objective` section is detected, it is updated using the generated content.

### 5. Merge Relevant Information

Extracted information is added to matching resume sections such as:

```text
Technical Skills
Experience
Projects
Education
Languages
```

Long job-description lines are skipped when they exceed the configured word limit.

### 6. Enhance Projects

If the resume contains a Projects section without existing descriptions, the updater can add a short project description using relevant extracted skills.

### 7. Enforce Resume Structure

The final resume follows the expected section order:

```text
Summary
Technical Skills
Experience
Projects
Education
Languages
```

### 8. Generate Updated Resume

The processed resume is returned as text and made available through the Streamlit download button.

## Project Structure

```text
RESUMEUPDATER-main/
│
├── RESUME_UPDATER.py       # Resume processing and JD analysis logic
├── resume_app.py            # Streamlit web application
└── README.md                # Project documentation
```

## Main Functions

### `load_text()`

Reads the contents of a text file.

### `extract_sections()`

Analyzes the job description and groups lines into relevant categories.

### `classify_jd_line()`

Determines which resume category a job-description line belongs to.

### `boost_summary()`

Creates or updates the resume summary using extracted job-related skills.

### `merge_into_section()`

Adds relevant job-description information to an existing resume section.

### `enhance_projects()`

Adds a short project description when the Projects section lacks descriptions.

### `enforce_structure()`

Organizes the resume into the expected section order.

### `update_resume()`

Coordinates the complete resume-updating process.

## Troubleshooting

### `streamlit` is not recognized

Install Streamlit:

```powershell
pip install streamlit
```

Then run:

```powershell
python -m streamlit run resume_app.py
```

### Python is not recognized

Verify that Python is installed and added to the system PATH:

```powershell
python --version
```

If the command fails, install Python and enable the **Add Python to PATH** option during installation.

### Resume Upload Is Rejected

The current application accepts `.txt` files. Convert the resume to plain text before uploading.

### No Updated Resume Is Generated

Make sure:

* A resume file has been uploaded.
* The job description is not empty.
* The Streamlit application is still running.
* The terminal does not show a Python exception.

### Job Description Information Is Not Added

The current implementation uses keyword-based classification. A line that does not contain one of the configured keywords may not be assigned to a resume section.

### Resume Formatting Changes Unexpectedly

The project processes plain text using regular expressions and section-based text manipulation. It is not a Word or PDF formatting engine, so complex formatting is not preserved.

## Limitations

* The current application supports `.txt` resumes rather than `.pdf` or `.docx`.
* Job-description analysis is based on predefined keyword rules.
* The system does not independently verify whether a skill is actually present in the candidate's experience.
* Extracted job-description information may require manual review before being used in a final resume.
* Complex resume layouts, tables, images, columns, and formatting are not supported.
* The application is intended as a resume-tailoring/demo project rather than a complete automated recruitment system.

## Security and Privacy Notes

This project may process personal information contained in resumes. Do not upload sensitive resumes to an application or machine that you do not trust.

The project is designed for local development. Before deploying it to a public server:

* Add appropriate authentication and authorization.
* Validate uploaded files.
* Restrict file size and file types.
* Avoid storing resumes longer than necessary.
* Protect temporary and generated files.
* Review logging so that personal information is not exposed.
* Use secure deployment and HTTPS configuration.
* Do not commit resumes, personal information, credentials, or generated output files to Git.

## Future Enhancements

Possible extensions include:

* PDF and DOCX resume support
* Skill matching and keyword scoring
* Job-description/resume similarity scoring
* AI-based resume rewriting
* ATS compatibility analysis
* Missing-skill detection
* Resume formatting and template support
* Multiple resume versions for different job descriptions
* Secure cloud deployment
* Database-backed resume history
