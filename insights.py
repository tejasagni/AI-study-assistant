def generate_insight(row):
    feedback = []

    if row['Math'] < 60:
        feedback.append("Improve Math with daily practice.")

    if row['English'] < 60:
        feedback.append("Focus on reading and writing skills.")

    if row['StudyHours'] < 3:
        feedback.append("Increase study time for better results.")

    if not feedback:
        feedback.append("Great performance! Keep it up.")

    return " ".join(feedback)