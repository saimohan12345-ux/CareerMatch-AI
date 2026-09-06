def calculate_final_score(
    required_score,
    preferred_score,
    tfidf_score
):
    """
    Calculate the final resume-JD matching score.

    Weights:
    Required Skills  -> 50%
    Preferred Skills -> 15%
    TF-IDF Similarity -> 35%
    """

    final_score = (
        required_score * 0.50
        + preferred_score * 0.15
        + tfidf_score * 0.35
    )

    return round(final_score, 2)


def get_score_interpretation(score):

    if score >= 80:
        return "Excellent Match"

    elif score >= 65:
        return "Strong Match"

    elif score >= 50:
        return "Moderate Match"

    elif score >= 35:
        return "Low Match"

    else:
        return "Very Low Match"