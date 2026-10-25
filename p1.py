marks = [88, 45, 92, 67, 30, 75]
c = 0
for m in marks:
    if m >= 50:
        c += 1
print("Passed:",c)
average = sum(marks)/len(marks)
print(f"{average:.1f}")
#print(round(average, 1))
print("Highest",max(marks), "lowest",min(marks))