import streamlit as st

from core.pdf_parser import extract_pdf_text
from core.analyzer import analyze_resume


st.set_page_config(
    page_title="CareerMatch AI",
    page_icon="📄",
    layout="wide"
)


st.title("CareerMatch AI")

st.subheader(
    "AI Resume & Job Matching System"
)


uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)


job_description = st.text_area(
    "Paste Job Description",
    height=250
)


if st.button("Analyze Resume"):

    if uploaded_file is None:

        st.error("Please upload your resume.")

    elif not job_description.strip():

        st.error("Please enter a job description.")

    else:

        with st.spinner("Analyzing..."):

            resume_text = extract_pdf_text(
                uploaded_file
            )

            result = analyze_resume(
                resume_text,
                job_description
            )

        st.success("Analysis completed!")

        st.metric(
            "Job Match Score",
            f"{result['final_score']}%"
        )

        st.subheader("Matched Skills")

        for skill in result["matched_skills"]:
            st.write(f"✅ {skill}")

        st.subheader("Missing Skills")

        for skill in result["missing_skills"]:
            st.write(f"❌ {skill}")

        st.subheader("Score Breakdown")

        st.write(
            f"Required Skills Match: "
            f"{result['required_score']}%"
        )

        st.write(
            f"Preferred Skills Match: "
            f"{result['preferred_score']}%"
        )

        st.write(
            f"TF-IDF Similarity: "
            f"{result['tfidf_score']}%"
        )

        st.write(
            f"Final Weighted Score: "
            f"{result['final_score']}%"
        )
        st.write(
            f"Match Interpretation: "
            f"{result['score_interpretation']}"
        )