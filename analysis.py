import pandas as pd

data = pd.read_csv("student_data.csv")

print(data)
subjects = ["Maths", "Python", "DBMS", "OS"]

data["Average"] = data[subjects].mean(axis=1)

print("\nStudent Average Marks:")
print(data[["Name", "Average"]])
top_student = data.loc[data["Average"].idxmax()]

print("\nHighest Scoring Student:")
print("Name:", top_student["Name"])
print("Average Marks:", top_student["Average"])
print("\nSubject-wise Average Marks:")

for subject in subjects:
    average = data[subject].mean()
    print(subject, ":", round(average, 2))
    print("\nAttendance vs Average Marks:")

print(data[["Name", "Attendance", "Average"]])
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))

plt.bar(data["Name"], data["Average"])

plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Average Marks")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
plt.figure(figsize=(8, 5))

plt.scatter(data["Attendance"], data["Average"])

plt.xlabel("Attendance (%)")
plt.ylabel("Average Marks")
plt.title("Attendance vs Average Marks")

plt.tight_layout()
plt.show()
data["Result"] = data[subjects].apply(
    lambda row: "Pass" if (row >= 40).all() else "Fail",
    axis=1
)

print("\nStudent Result:")
print(data[["Name", "Result"]])

print("\nTotal Pass:", (data["Result"] == "Pass").sum())
print("Total Fail:", (data["Result"] == "Fail").sum())
result_counts = data["Result"].value_counts()

plt.figure(figsize=(6, 6))

plt.pie(
    result_counts,
    labels=result_counts.index,
    autopct="%1.1f%%"
)

plt.title("Student Pass/Fail Distribution")
plt.show()
print("\n========== FINAL REPORT ==========")

print("Total Students:", len(data))
print("Highest Average:", round(data["Average"].max(), 2))
print("Lowest Average:", round(data["Average"].min(), 2))
print("Average Attendance:", round(data["Attendance"].mean(), 2), "%")
print("Total Pass:", (data["Result"] == "Pass").sum())
print("Total Fail:", (data["Result"] == "Fail").sum())
data.to_csv("student_analysis_result.csv", index=False)

print("\nAnalyzed data saved successfully!")
subject_averages = data[subjects].mean()

plt.figure(figsize=(8, 5))

plt.bar(subject_averages.index, subject_averages.values)

plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.title("Subject-wise Average Marks")

plt.tight_layout()
plt.show()
top_3 = data.nlargest(3, "Average")

print("\nTop 3 Students:")
print(top_3[["Name", "Average"]])