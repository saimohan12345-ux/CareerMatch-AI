# CareerMatch AI

## AI Resume & Job Matching System

CareerMatch AI is a Python and Streamlit-based application that analyzes a candidate's resume against a job description and generates an explainable job-match score.

## Features

- Resume PDF text extraction
- Job description analysis
- Technical skill extraction
- Skill normalization
- Required and preferred skill classification
- Matched skill identification
- Missing skill identification
- TF-IDF based text similarity
- Weighted job-match scoring
- Explainable score breakdown
- Skill-gap analysis

## System Architecture

```text
           ** Resume + Job Description
                      |
                      v
               Text Extraction
                      |
                      v
                 Text Cleaning
                      |
                      v
                Skill Extraction
                      |
                      v
               Skill Normalization
                      |
                      v
             R**equired / Preferred
                Classification
                      |
                      v
               Skill Matching
                      |
              +----------------+
              |                |
              v                v
         Skill Score      TF-IDF Score
              |                |
              +-------+--------+
                      |
                      v
              Weighted Final Score
                      |
                      v
              Match & Skill Gap Report
