# CareerMatch AI

## AI Resume & Job Matching System

CareerMatch AI is a Python and Streamlit-based application that analyzes a candidate's resume against a job description and generates an explainable job-match score using NLP, skill matching, and TF-IDF text similarity.

## Features

* Resume PDF text extraction
* Job description analysis
* Technical skill extraction
* Skill normalization using aliases
* Required and preferred skill classification
* Matched skill identification
* Missing skill identification
* Skill-gap analysis
* TF-IDF based text similarity
* Weighted job-match scoring
* Explainable score breakdown
* Overall match interpretation

## Technology Stack

* Python
* Streamlit
* Natural Language Processing (NLP)
* Scikit-learn
* TF-IDF
* PyPDF2
* Regular Expressions (Regex)
* JSON

## Project Structure

```text
CareerMatch-AI/
│
├── app.py
│
├── core/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── skill_extractor.py
│   ├── similarity.py
│   ├── scorer.py
│   ├── text_processor.py
│   ├── pdf_parser.py
│   └── llm_analyzer.py
│
├── data/
│   └── skills.json
│
├── requirements.txt
│
└── .gitignore
```

## System Architecture

```text
              Resume + Job Description
                         │
                         ▼
                  PDF Text Extraction
                         │
                         ▼
                    Text Cleaning
                         │
                         ▼
                  Skill Extraction
                         │
                         ▼
                 Skill Normalization
                         │
                         ▼
             Required / Preferred Skills
                    Classification
                         │
                         ▼
                   Skill Matching
                         │
                  ┌──────┴──────┐
                  ▼             ▼
             Skill Score    TF-IDF Score
                  │             │
                  └──────┬──────┘
                         ▼
                Weighted Final Score
                         │
                         ▼
              Match & Skill-Gap Report
```

## How It Works

1. The user uploads a resume in PDF format.
2. The system extracts the text from the resume.
3. The user provides a job description.
4. Resume and job-description text are cleaned and normalized.
5. Technical skills are extracted using a predefined skill dataset.
6. Skill aliases are normalized to improve matching accuracy.
7. Resume skills are compared with the skills identified in the job description.
8. The system identifies matched and missing skills.
9. TF-IDF is used to calculate textual similarity between the resume and job description.
10. Skill matching and TF-IDF similarity are combined using a weighted scoring method.
11. The application displays the final job-match score along with an explainable score breakdown and skill gaps.

## Installation

Clone the repository:

```bash
git clone https://github.com/saimohan12345-ux/CareerMatch-AI.git
cd CareerMatch-AI
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your default web browser.

## Example Output

CareerMatch AI provides:

* **Overall Job Match Score**
* **Matched Skills**
* **Missing Skills**
* **Required Skills Match**
* **Preferred Skills Match**
* **TF-IDF Similarity Score**
* **Final Weighted Score**
* **Match Interpretation**
* **Skill-Gap Analysis**

## Example

For a Software Developer job description, the system can identify skills such as:

```text
Matched Skills:
Python
Java
SQL
Git
Data Structures
OOP
```

and identify missing requirements such as:

```text
Missing Skills:
AWS
Docker
REST API
Unit Testing
SDLC
```

The system then combines the skill-match results and text similarity to generate an overall match score.

## Future Improvements

* Semantic similarity using sentence embeddings
* Advanced NLP-based skill extraction
* Improved job-role classification
* Resume improvement recommendations
* Resume keyword optimization
* Support for additional resume formats
* Job-role recommendations based on candidate skills
* Enhanced semantic resume-to-job matching
* Machine-learning-based scoring models

## Author

**Sai Mohan Budideti**

B.Tech Artificial Intelligence and Machine Learning

Annamacharya Institute of Technology and Sciences, Tirupati
