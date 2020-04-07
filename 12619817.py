import csv

f = open("sample1.csv", "w")
writer = csv.DictWriter(
    f, fieldnames=["student", "subject","marks"])
writer.writeheader()
writer.writerows(
    [{"student": "a", "subject": "python","marks":"50"},
    {"student": "b", "subject": "python","marks":"60"},
     {"student": "c", "subject": "java","marks":"80"}])
f.close()
