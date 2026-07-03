# ============================================
# Student Grade Calculator
# Developer: Moxil Virani
# Project: Phase 1 - Project 1
# ============================================

student_name = "Moxil"

# Subject-wise marks (Key: Subject, Value: Marks)
subjects = {
    "Java": 36,
    "SQL": 36,
    "Software Development": 36,
    "DBMS": 38,
    "Software Testing": 18,
    "IKS": 19,
    "English": 18
}

# ---- STEP 1: Total Marks Calculate ----
total = 0
for marks in subjects.values():
    total = total + marks

# ---- STEP 2: Percentage Calculate ----
total_possible = 275
percentage = round((total / total_possible) * 100, 2)

# ---- STEP 3: Grade Decide (Based on Percentage) ----
if percentage >= 75:
    grade = "Distinction A+"
elif percentage >= 70:
    grade = "Distinction"
elif percentage >= 60:
    grade = "First Class"
elif percentage >= 33:
    grade = "Pass"
else:
    grade = "Fail"

# ---- STEP 4: Subject-wise Pass/Fail Check ----
# Assume karo student pass hai — jab tak koi subject fail na mile
is_failed_in_any = False

for sub, marks in subjects.items():
    if marks < 33:
        print("Failed in Subject:", sub)
        is_failed_in_any = True

# Agar kisi bhi subject mein fail — overall grade update karo
if is_failed_in_any == True:
    grade = "Failed (ATKT)"

# ---- STEP 5: Final Result Print ----
print("========================")
print("   STUDENT RESULT CARD  ")
print("========================")
print("Student Name :", student_name)
print("Total Marks  :", total, "/", total_possible)
print("Percentage   :", percentage, "%")
print("Grade        :", grade)
print("========================")