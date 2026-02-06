import pandas as pd
df = pd.read_csv("students.csv")
subjects = ["subj1", "subj2", "subj3", "subj4", "subj5"]
df["average"] = df[subjects].mean(axis=1)
print("Students table whis average grade:")
print(df[["surname", "name", "average"]])
print("\nAverage group grade from subjects:")
for subj in subjects:
    print(f"{subj}: {df[subj].mean():.2f}")
