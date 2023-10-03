import csv

# Read the CSV file using the csv module
with open('data/data.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    data = list(reader)

# Add the new column header to the first row
data[0].insert(4, "Synthetic or Semi-synthetic Opioids")

# Iterate through the data starting from the second row (index 1)
for row in data[1:]:
    indicator = row[4]
    synthetic_opioid = "synthetic" in indicator.lower() or "natural" in indicator.lower()

    if indicator.startswith("Number"):
        row.insert(4, "Data Value")
    elif indicator.startswith("Percent"):
        row.insert(4, "Data Value")
    else:
        row.insert(4, "Yes" if synthetic_opioid else "No")

# Write the updated data to a new CSV file
with open('data/clean_data.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(data)















