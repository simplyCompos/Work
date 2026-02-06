grades = {
    "Abobus": [5, 4, 4, 5],
    "Amogus": [4, 5, 5, 5]
}

avg_dict = {}
unique_grades = set()

for name, marks in grades.items():
    avg = sum(marks) / len(marks)
    avg_dict[name] = avg
    unique_grades.update(marks)

print("Average grades:", avg_dict)
print("Unique grades:", unique_grades)
