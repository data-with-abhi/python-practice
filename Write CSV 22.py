# Clean customer Name (strip + title)

import csv

cleaned_rows = [ ]
with open("ch-10.csv","r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["Name"] = row["Name"].strip().title()
        cleaned_rows.append(row)
    # print(cleaned_rows)

with open("clean.csv","w",newline = "") as f:
    writer = csv.DictWriter(f,fieldnames = reader.fieldnames)
    writer.writeheader()
    writer.writerows(cleaned_rows)

print("Cleaned CSV created - clean.csv")


