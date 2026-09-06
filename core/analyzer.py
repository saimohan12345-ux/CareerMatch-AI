from core.text_processor import clean_text

from core.skill_extractor import (
    extract_skills,
    normalize_skills
)

from core.similarity import (
    compare_skills,
    calculate_tfidf_similarity
)
from core.scorer import (
    calculate_final_score,
    get_score_interpretation
)


def analyze_resume(resume_text, jd_text):

    # --------------------------------------------------
    # 1. Clean resume and job description
    # --------------------------------------------------

    resume_clean = clean_text(resume_text)
    jd_clean = clean_text(jd_text)


    # --------------------------------------------------
    # 2. Extract skills
    # --------------------------------------------------

    resume_skills = normalize_skills(
        extract_skills(resume_clean)
    )

    jd_skills = normalize_skills(
        extract_skills(jd_clean)
    )


    # --------------------------------------------------
    # 3. Compare resume skills with JD skills
    # --------------------------------------------------

    skill_result = compare_skills(
        resume_skills,
        jd_skills
    )


    # --------------------------------------------------
    # 4. Calculate TF-IDF similarity
    # --------------------------------------------------

    tfidf_score = calculate_tfidf_similarity(
        resume_clean,
        jd_clean
    )


    # --------------------------------------------------
    # 5. Separate required and preferred skills
    # --------------------------------------------------

    preferred_keywords = [
        "docker",
        "aws",
        "azure",
        "gcp"
    ]

    preferred_skills = []

    for skill in jd_skills:

        if skill.lower() in preferred_keywords:
            preferred_skills.append(skill)


    required_skills = [
        skill for skill in jd_skills
        if skill not in preferred_skills
    ]


    # --------------------------------------------------
    # 6. Calculate required skill score
    # --------------------------------------------------

    matched_required = [
        skill for skill in skill_result["matched"]
        if skill in required_skills
    ]

    if len(required_skills) > 0:

        required_score = (
            len(matched_required)
            / len(required_skills)
        ) * 100

    else:

        required_score = 0


    # --------------------------------------------------
    # 7. Calculate preferred skill score
    # --------------------------------------------------

    matched_preferred = [
        skill for skill in skill_result["matched"]
        if skill in preferred_skills
    ]

    if len(preferred_skills) > 0:

        preferred_score = (
            len(matched_preferred)
            / len(preferred_skills)
        ) * 100

    else:

        preferred_score = 0


    # --------------------------------------------------
    # 8. Calculate final weighted score
    # --------------------------------------------------

    final_score = calculate_final_score(
        required_score,
        preferred_score,
        tfidf_score
    )

    score_interpretation = get_score_interpretation(
        final_score
    )


    return {

        "resume_skills":
            resume_skills,

        "jd_skills":
            jd_skills,

        "required_skills":
            required_skills,

        "preferred_skills":
            preferred_skills,

        "matched_skills":
            skill_result["matched"],

        "missing_skills":
            skill_result["missing"],

        "matched_required":
            matched_required,

        "matched_preferred":
            matched_preferred,

        "required_score":
            round(required_score, 2),

        "preferred_score":
            round(preferred_score, 2),

        "tfidf_score":
            tfidf_score,

        "final_score":
            final_score,

        "score_interpretation":
            score_interpretation
    }