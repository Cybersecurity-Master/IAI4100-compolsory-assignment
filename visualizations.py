import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt(
    "Dataset/Student_Performance_Dataset.csv",
    delimiter=",",
    names=True,
    dtype=None,
    encoding="utf-8",
)

study_hours = data["Study_Hours_Per_Day"]
attendance = data["Attendance_Percentage"]
math_score = data["Math_Score"]
science_score = data["Science_Score"]
english_score = data["English_Score"]
previous_year = data["Previous_Year_Score"]
final_pct = data["Final_Percentage"]
gender = data["Gender"]
extracurricular = data["Extracurricular_Activities"]

# Task 1 - Average Final Percentage against Study Hours Per Day
unique_hours = np.unique(study_hours)
avg_final_by_hours = np.array(
    [np.mean(final_pct[study_hours == h]) for h in unique_hours]
)

plt.figure()
plt.plot(unique_hours, avg_final_by_hours)
plt.xlabel("Study Hours Per Day")
plt.ylabel("Average Final Percentage")
plt.title("Average Final Percentage vs Study Hours Per Day")
plt.savefig("plots/task1_avg_final_vs_study_hours.png")
plt.close()

# Task 2 - Scatter plot: Attendance Percentage vs Final Percentage
plt.figure()
plt.scatter(attendance, final_pct)
plt.xlabel("Attendance Percentage")
plt.ylabel("Final Percentage")
plt.title("Attendance Percentage vs Final Percentage")
plt.savefig("plots/task2_attendance_vs_final.png")
plt.close()

# Task 3 - Bar chart: average Math, Science and English scores
subjects = ["Math", "Science", "English"]
averages = [np.mean(math_score), np.mean(science_score), np.mean(english_score)]

plt.figure()
plt.bar(subjects, averages)
plt.ylabel("Average Score")
plt.title("Average Math, Science and English Scores")
plt.savefig("plots/task3_avg_subject_scores.png")
plt.close()

# Task 4 - Scatter plot: Previous Year Score vs Final Percentage
plt.figure()
plt.scatter(previous_year, final_pct)
plt.xlabel("Previous Year Score")
plt.ylabel("Final Percentage")
plt.title("Previous Year Score vs Final Percentage")
plt.savefig("plots/task4_previous_year_vs_final.png")
plt.close()

# Task 5 - Scatter plot: Study Hours vs Final Percentage by Gender
male = gender == "Male"
female = gender == "Female"

plt.figure()
plt.scatter(study_hours[male], final_pct[male], label="Male")
plt.scatter(study_hours[female], final_pct[female], label="Female")
plt.xlabel("Study Hours Per Day")
plt.ylabel("Final Percentage")
plt.title("Study Hours Per Day vs Final Percentage by Gender")
plt.legend()
plt.savefig("plots/task5_study_hours_vs_final_by_gender.png")
plt.close()

# Task 6 - Box plot: Final Percentage by Extracurricular Activities
participates = final_pct[extracurricular == "Yes"]
does_not = final_pct[extracurricular == "No"]

plt.figure()
plt.boxplot([does_not, participates], tick_labels=["No", "Yes"])
plt.xlabel("Extracurricular Activities")
plt.ylabel("Final Percentage")
plt.title("Final Percentage by Extracurricular Activities")
plt.savefig("plots/task6_final_by_extracurricular.png")
plt.close()

print("All plots saved in the plots folder.")
