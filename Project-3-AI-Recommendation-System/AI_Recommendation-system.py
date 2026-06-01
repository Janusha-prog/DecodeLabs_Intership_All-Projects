# Project 3: AI Recommendation Logic System

print("=== AI Tech Career Recommender ===\n")

# Import Libraries
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Dataset of career roles, skills, courses, and roadmaps
data = {

    "Role": [

        "Data Scientist",
        "Frontend Developer",
        "Backend Developer",
        "DevOps Engineer",
        "Machine Learning Engineer",
        "Cloud Engineer",
        "AI Engineer"
    ],

    "Skills": [

        "python machine learning sql data analysis",
        "html css javascript react frontend",
        "python django apis sql backend",
        "aws docker kubernetes linux devops",
        "python tensorflow deep learning ai",
        "cloud aws networking linux",
        "python ai deep learning neural networks"
    ],

    "Course": [

        "Machine Learning with Python",
        "Frontend Web Development",
        "Backend Development with Django",
        "DevOps Bootcamp",
        "Deep Learning Specialization",
        "AWS Cloud Practitioner",
        "AI Engineering Roadmap"
    ],

    "Next Skills": [

        "Pandas, NumPy, Deep Learning",
        "React, Tailwind CSS, UI Design",
        "REST APIs, MongoDB, Flask",
        "CI/CD, Jenkins, Terraform",
        "PyTorch, NLP, Computer Vision",
        "Azure, DevOps, Security",
        "LLMs, Generative AI, MLOps"
    ],

    "Roadmap": [

        "Python → ML → Deep Learning → AI Projects",
        "HTML → CSS → JavaScript → React",
        "Python → Django → APIs → Databases",
        "Linux → Docker → Kubernetes → Cloud",
        "Python → TensorFlow → Deep Learning",
        "Networking → AWS → Cloud Security",
        "Python → AI → LLMs → GenAI"
    ]
}

# Convert into DataFrame
df = pd.DataFrame(data)

# Display Available Roles
print("Available Career Roles:\n")
for role in df["Role"]:
    print("-", role)

# User Input
user_input = input(
    "\nEnter your skills separated by spaces:\n")

# Convert to lowercase
user_input = user_input.lower()

# Combine dataset skills + user skills
all_skills = df["Skills"].tolist()
all_skills.append(user_input)

# Convert text into numerical vectors
vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(all_skills)

# Calculate Cosine Similarity
similarity = cosine_similarity(
    vectors[-1],
    vectors[:-1]
)
scores = similarity.flatten()

# Add similarity scores to DataFrame
df["Similarity Score"] = scores

# Sort recommendations
recommendations = df.sort_values(
    by="Similarity Score",
    ascending=False)

# Find highest similarity score
highest_score = recommendations[
    "Similarity Score"].max()

# Filter best matching careers
best_matches = recommendations[
    recommendations["Similarity Score"]
    == highest_score]

# If no match found
if highest_score == 0:
    print("\nSorry 😔")
    print(
        "No matching career recommendation found."
    )
else:
    print("\n=== Best Career Recommendation ===\n")
    for index, row in best_matches.iterrows():
        print("Career Role:")
        print(row["Role"])

        print("\nMatch Score:")
        print(
            round(
                row["Similarity Score"] * 100,2),"%")
        print("\nRecommended Course:")
        print(row["Course"])

        print("\nSkills To Learn Next:")
        print(row["Next Skills"])

        print("\nCareer Roadmap:")
        print(row["Roadmap"])

        print("\nMotivation:")
        print("Keep learning consistently and build projects 🚀")
        print()
