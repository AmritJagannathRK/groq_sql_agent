import csv

# Define the data
data = [
    ["roll", "name", "age"],
    [1, "Arnab", 25],
    [2, "Amrit", 26],
    [3, "John", 22],
    [4, "Emily", 24],
    [5, "Michael", 27]
]

# Specify the CSV file name
csv_file_path = 'students.csv'

# Write data to the CSV file
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data)

print(f"CSV file '{csv_file_path}' created successfully.")