def generate_recommendations(missing_skills):

    recommendations = []

    for skill in missing_skills:

        recommendation = (
            f"Consider learning or adding {skill} "
            f"to your resume if you have relevant experience."
        )

        recommendations.append(recommendation)

    return recommendations