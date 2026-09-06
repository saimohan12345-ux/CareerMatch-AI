from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_tfidf_similarity(resume_text, jd_text):

    documents = [
        resume_text,
        jd_text
    ]

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    return round(similarity * 100, 2)


def compare_skills(resume_skills, jd_skills):

    resume_set = set(resume_skills)
    jd_set = set(jd_skills)

    matched = sorted(
        resume_set.intersection(jd_set)
    )

    missing = sorted(
        jd_set.difference(resume_set)
    )

    if len(jd_set) == 0:
        score = 0

    else:
        score = (
            len(matched) /
            len(jd_set)
        ) * 100

    return {
        "matched": matched,
        "missing": missing,
        "score": round(score, 2)
    }