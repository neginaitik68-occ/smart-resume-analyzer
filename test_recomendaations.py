from utils.recomendaations import generate_recommendations


missing_skills = [
    "machine learning",
    "power bi",
    "docker"
]


recommendations = generate_recommendations(
    missing_skills
)


print("Resume Recommendations:")

for recommendation in recommendations:

    print("-", recommendation)